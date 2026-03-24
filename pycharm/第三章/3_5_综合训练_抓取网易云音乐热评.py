#1. 找到未加密的参数                           #window.asrsea(参数,XXX,XXX,XXX)
#2. 想办法把参数进行加密（必须参考网易的逻辑），params   => encText  ,encSecKey  =>encSecKey
#3. 请求到网易，拿到评论信息


#需要安装pycrypto: pip install pycryptodome
from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 请求方式是post
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}

#服务于d的
f= '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
e = '010001'
g = '0CoJUm6Qyw8W8jud'
i =  "XtI57IjhXqfs9unk"  #手动固定的，那么encText就是固定的  c()函数的结果就是固定的

def get_encSecKey():
    return "5ff0a1184d199b5fd59f4d95ff6fe10934eb926116e7700a36d6e6db5f528adcce0a82a155d5c96c0bd69ca714f8b025198d001881d454416a01dbb29097da0aca934926797ad512eac1a65e512f6357a54a84ef4f13f4fdca63343b8515d384dd90a0e142cbfa37687397f7033a9288b4e149774f5e0a513e85faba1a37cf41"


#把参数进行加密
def get_params(data):   #默认这里接收到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second  #返回的是params

#转换成16的倍数，为下方的加密算法服务
def to_16(data):  #补全函数
    pad = 16 - len(data) %16
    data += pad * chr(pad)
    return data
#加密过程
def enc_params(data, key): #加密过程
    iv = "0102030405060708"
    data = to_16(data)  #补全
    aes = AES.new(key=key.encode("utf-8"),mode=AES.MODE_CBC,iv=iv.encode("utf-8"))  #创建加密器
    #AES.encrypt() 方法必须接收二进制字节流（bytes 类型）    加密,加密的数据必须是16的倍数
    bs =aes.encrypt(data.encode("utf-8"))#加密  aes.encrypt(data) 输出的 bs 是 二进制字节流（bytes 类型），而 utf-8 是「字符编码格式」—— 只有符合 utf-8 编码规则的字节流才能转成字符串，AES 加密后的二进制流是随机的、不符合任何字符编码规则的，强行用 utf-8 转换会抛出 UnicodeDecodeError 错误。
    return str(b64encode(bs),"utf-8")  #转成字符串返回




#处理加密过程
"""
    function a(a=16) {   #  随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)      # 循环16次
            e = Math.random() * b.length,  #随机数
            e = Math.floor(e),          #向下取整
            c += b.charAt(e);            # 获取随机字符
        return c
    }
    function b(a, b) {  # a是要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b)    # b是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)   #e是数据
          , f = CryptoJS.AES.encrypt(e, c, {     #c是密钥
            iv: d,   #偏移量
            mode: CryptoJS.mode.CBC   #模式CBC
        });
        return f.toString()
    }
    function c(a, b, c) {  #c 里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  d:  数据 为data , e: '010001' , f: 很长 , g:'0CoJUm6Qyw8W8jud'
        var h = {}  #  定义空变量
          , i = a(16);   #i 是随机的16位字符串
        return h.encText = b(d, g),      # g是密钥
        h.encText = b(h.encText, i), # 返回的是params      i是密钥
        h.encSecKey = c(i, e, f),    # 返回的是encSecKey    e和f是固定的  如果此时把i定死 
        h
        #等价于
        '''
        h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        return h
        '''
        #encText是经过了两次加密的结果  数据+g =》 b =>第一次加密的结果    第一次加密结果 + i =》 b =>第二次加密结果
    }
"""

#发送请求得到评论结果
resp = requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
})
print(resp.text)