import requests
from bs4 import BeautifulSoup
def user_index():
    url = 'http://space.bilibili.com/2441133/#!/index'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",

    }
    #aUrl = 'http://www.bilibili.com/video/av5964441/'
    avHtml = requests.get(url,headers=headers)
    avPage = BeautifulSoup(avHtml.text,"html.parser")
    print(avPage)
    small_item = avPage.find_all("div",attrs={"class":"small-item"})
    print(small_item)

if __name__ == '__main__':
    user_index()


