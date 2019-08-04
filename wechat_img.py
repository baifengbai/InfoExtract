
import requests
import urllib
from bs4 import BeautifulSoup

def getImg(url):
    html=requests.get(url)
    page=html.read()
    soup=BeautifulSoup(page,"html.parser")
    imglist = soup.select('#js_content > p > img')

    lenth=len(imglist)
    print lenth
    x=0
    for i in range(lenth):
        print imglist[i].attrs['data-src']
        urllib.urlretrieve(imglist[i].attrs['data-src'],'%s.jpg'%x)
        x+=1

url ='http://mp.weixin.qq.com/s/dDVTzZEzA-I1bNdmTTg9mA'
getImg(url)