#coding:utf-8
import urllib2
import csv
import re
from bs4 import BeautifulSoup
#设置默认encoding
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#看下最大页数  切换关键词即可
for k in range(1,38):
    url="http://news.baidu.com/ns?word=国产皮卡&pn=%s&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0&rsv_page=-1"%((k-1)*20)
    csvfile = file('guochanpika.csv','ab+')
    writer = csv.writer(csvfile)

    content=urllib2.urlopen(url).read()
    #use soup parse
    soup =BeautifulSoup(content,'lxml')
    list0=[]
    list1=[]
    list2=[]
    list3=[]
    #recognize hot news
    for i in range(0,20):
        hotnews = soup.find_all('div',{'class','result'})[i]
        a1 = hotnews.find(name="a",attrs={'target':re.compile('_blank')})
        list0.append(a1.text)
        a2 = hotnews.find(name="p",attrs={"class":re.compile("c-author")})
        t1 = a2.text.split()[0]
        list1.append(t1)
        t2 = a2.text.split()[1]
        list2.append(t2)

        if t2.find(u'年') == 4 :
            t3 =a2.text.split()[2]
            list3.append(t3)
        else:
            list3.append('')

    #write into csv
    data=[]
    for i in range(0,20):
        data.append((list0[i],list1[i],list2[i],list3[i]))
        writer.writerows(data)
        # csvfile.close()
    print "第" + str(k) + "页完成"
