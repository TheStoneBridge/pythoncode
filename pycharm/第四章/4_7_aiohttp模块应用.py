# requests.get() 同步的代码  -> 异步操作aiohttp
#pip install aiohttp

import asyncio
import aiohttp

urls = [
    "https://s.panlai.com/zb_users/upload/2026/02/bizhihui_com_202602101770656501139187.jpg",
    "https://s.panlai.com/zb_users/upload/2026/01/bizhihui_com_202601291769674202895309.jpg",
    "https://s.panlai.com/zb_users/upload/2026/01/bizhihui_com_202601261769437985238046.png"
]

async def aiodownload(url):
    name = url.rsplit("/",1)[1] # 从右边分割字符串，分割一次，取第二部分（文件名）
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:  #  with  是会自动添加上下文管理器  会自动关闭 例如自动关闭文件
            #resp.content.read()  <==>resp.content
            #resp.test() <==>resp.text
            #resp.json() <==>resp.json()
            with open(name, "wb") as f:
                f.write(await resp.content.read()) # 读取内容是异步的，需要await挂起
    print(f"下载完成{name}")         
    #s = aiohttp.ClientSession()  <==>  requests
    # request.get()    .post()
    # s.get()  .post()
    #  发送请求
    # 得到图片内容
    # 保存到文件
async def main():
    tasks = [asyncio.create_task(aiodownload(url)) for url in urls]
    await asyncio.wait(tasks)

if __name__ == "__main__":
    asyncio.run(main()) 