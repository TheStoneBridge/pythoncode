"""
流程:
1.获取网页源代码
2.从源代码中提取到m3u8的url
3.下载m3u8
4.读取m3u8文件,下载视频
5.合并视频
"""


import requests
import asyncio  
import aiohttp
import os
import subprocess
from urllib.parse import urljoin,urlparse

#配置项
m3u8_url ="https://vip.dytt-music.com/20250330/33001_3c2039db/3000k/hls/mixed.m3u8"
download_dir = "video_framents"  #分片保存目录
final_video = "final_video.ts" #合并后的视频文件
final_video_mp4 = "final_video.mp4" #最终输出的mp4文件
max_concurrent = 10 #最大并发数（可根据网络调整）
timeout = 30 #请求超时时间
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
}

#创建目录
os.makedirs(download_dir, exist_ok=True)

async def download_m3u8_file(session,url,save_path):  # 下载m3u8文件
    try:
        async with session.get(url, headers=headers, timeout=timeout) as response:
            response.raise_for_status()
            content = await response.text()
            with open(save_path, 'w', encoding='utf-8') as f:  # 保存m3u8文件
                f.write(content)
            print(f"下载m3u8文件成功: {save_path}")
            return content
    except Exception as e:
        print(f"下载m3u8文件失败: {e}")
        raise

def parse_m3u8_content(m3u8_content,base_url):  # 解析m3u8内容，提取所有分片url
        fragments = []
        lines = m3u8_content.strip().split('\n')
        for line in lines:
            line = line.strip()
            #跳过注释和空行
            if not line or line.startswith('#'):
                continue    
            #拼接完整的分片url
            fragments_url = urljoin(base_url, line)
            fragments.append(fragments_url)
        print(f"解析m3u8文件成功,共找到{len(fragments)}个分片")
        return fragments    
async def download_fragment(session,url,save_path,semaphore):  # 下载单个分片 
    async with semaphore:  # 限制并发数
        try:
            async with session.get(url, headers=headers, timeout=timeout) as response:
                response.raise_for_status()
                content = await response.read()
                with open(save_path, 'wb') as f:
                    f.write(content)
                print(f"下载分片成功: {os.path.basename(save_path)}")
        except Exception as e:
            print(f"下载分片失败{url}: {e}")
            raise

def merge_fragments(fragments_dir,output_file):  # 合并所有分片
    fragments_files = sorted(
        [f for f in os.listdir(fragments_dir) if f.endswith((".ts",".m4s"))],
        key = lambda x : int(x.split(".")[0]) if x.split(".")[0].isdigit() else x
    )
    if not fragments_files:
        print("没有找到分片文件")
        return
    #合并所有分片
    with open(output_file,"wb") as out_f:
        for i, frag_file in enumerate(fragments_files):
            frag_path = os.path.join(fragments_dir, frag_file)
            with open(frag_path, "rb") as in_f:
                out_f.write(in_f.read())
            print(f"合并分片{i+1}/{len(fragments_files)}: {frag_file}")    
    print(f"合并完成: {output_file}")

def convert_to_mp4(ts_file,mp4_file):
    """使用ffmpeg将ts文件转换为mp4文件"""
    if not os.path.exists(ts_file):
        print(f"ts文件不存在: {ts_file}")
        return False
    # ffmpeg命令(-c copy表示直接复制视频流，不进行重新编码，速度更快)
    ffmpeg_path = r"D:\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"  # 如果ffmpeg不在系统路径中，需要指定完整路径
    cmd = [
        ffmpeg_path,
        "-i",ts_file, # 输入文件
        "-c", "copy",#直接拷贝编码(快速转换)
        "-y", # 覆盖已存在的输出文件
        mp4_file # 输出文件
    ]
    try:
        # 执行ffmpeg命令
        subprocess.run(
            cmd,
            stdout=subprocess.PIPE, #隐藏标准输出
            stderr=subprocess.PIPE, #隐藏错误输出
            check=True, #如果命令执行失败则抛出异常
            encoding="utf-8"
        )
        print(f"转换完成: {mp4_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {e}")
        return False
    except FileNotFoundError:
        print("ffmpeg未找到，请安装ffmpeg")
        return False
    
def clean_temp_files(fragments_dir,ts_file):
    """清理临时文件:分片文件、合并的ts文件、m3u8文件""" 
    #删除分片文件
    for f in os.listdir(fragments_dir):
        if f.endswith((".ts",".m4s",".m3u8")):
            os.remove(os.path.join(fragments_dir,f))
    #删除合并的ts文件
    if os.path.exists(ts_file):
        os.remove(ts_file)





    
async def  main():
    #1.创建异步会话
    async with aiohttp.ClientSession() as session:
        #2.下载m3u8文件
        m3u8_save_path = os.path.join(download_dir,"playlist.m3u8")
        m3u8_content = await download_m3u8_file(session,m3u8_url,m3u8_save_path)

        #3.解析m3u8文件，获取所有分片url
        base_url = urljoin(m3u8_url,"./") #获取m3u8文件的基础url
        fragments = parse_m3u8_content(m3u8_content,base_url)
        
        #4. 并发下载分片(使用信号量控制并发数)
        semaphore = asyncio.Semaphore(max_concurrent) #asyncio.Semaphore 是 asyncio 库提供的信号量 工具，本质是一个 “并发计数器”
        download_tasks = []
        
        for idx, frag_url in enumerate(fragments):  
        #enumerate 是 Python 内置函数，直译是枚举 / 列举，
        # 作用是遍历可迭代对象（如列表、元组、字符串等）时，
        # 同时获取每个元素的「索引（位置）」和「元素本身」，
        # 避免手动维护索引变量（比如用 i += 1 计数）。
            frag_filename = f"{idx}.ts"
            frag_save_path = os.path.join(download_dir,frag_filename)
            
            #创建下载任务
            task = asyncio.create_task(
                download_fragment(session,frag_url,frag_save_path,semaphore)
            )
            download_tasks.append(task)
            
        await asyncio.wait(download_tasks) #等待所有下载任务完成
    
    #5.合并分片
    merge_fragments(download_dir,final_video)
            
    #6.转换为MP4格式
    if convert_to_mp4(final_video,final_video_mp4): 
        #清理临时文件（转换成功后才清理）
        clean_temp_files(download_dir,final_video)
    else:
        print("转换失败")
        
        
if __name__ == '__main__':
    # 解决windows下asyncio的事件循环问题
    if  os.name =='nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    #运行主协程
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("下载被用户中断")
    except Exception as e:
        print(f"下载失败: {e}")
    