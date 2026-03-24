#1.拿到contID
#2.拿到videoStatus返回的json. -> srcURL
#3.srcURL里面的内容进行修正
#4.下载视频
import requests
url = "https://www.pearvideo.com/video_1804596"
contId = url.split("_")[1]

videoStatus_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.47604102496587253"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0",
    #防盗链： 溯源，当前本次请求的上一级是谁
    "referer":url
}

resp = requests.get(videoStatus_url, headers=headers)
dic = resp.json()
srcURL = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcURL = srcURL.replace(systemTime, f"cont-{contId}")

#下载视频
with open("1.mp4", "wb") as f:
    f.write(requests.get(srcURL).content)