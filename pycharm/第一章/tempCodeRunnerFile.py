import requests

url = "https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie"

data = {
    "start": "0",
    "limit": "20",
    "category": "热门",
    "type": "全部"
}

headers = {
    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    "referer": "https://movie.douban.com/explore?support_type=movie&is_all=false&category=%E7%83%AD%E9%97%A8&type=%E5%85%A8%E9%83%A8" 
    #有时候可能会有反爬 需要增加referer
}

response = requests.get(url, params=data, headers=headers)

print(response.request.url)

for item in response.json()['items']:
    print("剧名:\t",item['title'],"\t\t标签:\t",item['card_subtitle'],"\t\t评分:\t",item['rating']['value'])
