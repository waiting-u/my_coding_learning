import requests
content = input("请输入要检索的内容：")
url = f"https://www.sogou.com/web?query={content}"
headers={
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0",
}

resp = requests.get(url,headers=headers,allow_redirects=True)
resp.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup = BeautifulSoup(resp.text, "html.parser")

print(soup.prettify())