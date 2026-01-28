import requests
url = "https://fanyi.baidu.com/sug"
dat ={
    "kw": input("请输入一个单词：")
}

resp = requests.post(url,data=dat)
print(resp.json())
