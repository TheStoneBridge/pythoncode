 img_resp = requests.get(href1)
    with open(f"d:\pythoncode\pycharm\第二章-数据解析与提取\08_02_bs图片\{n}.jpg", "wb") as f:  #此时写入到文件的是字节  所以用wb
         f.write(img_resp.content)