import webbrowser
import os
import requests
import bs4

#url='https://www.zoro.to/home'
#url='https://kissanime.com.ru/Login?redirect_to=/'
#url='http://facebook.com'
f1=open('AnimeUrlList.txt','r')
f2=open('AnimeUpdateOld.txt','r+')
f3=open('AnimeUpdateNew.txt','r+')
f5=open('C:\\Users\\tirth\\OneDrive\\Desktop\\Anime.txt','a+')
k=0
status='0'
Link=f1.readlines()
print(Link)
EpisodeList=f2.readlines()
limit=len(EpisodeList)
#print(EpisodeList)
f2.truncate(0)
f2.seek(0)
garbage=f3.read()
f2.write(garbage)
f3.seek(0)

f3.truncate(0)
for url in Link:
    
    #print(url)
    Murl=url.replace('\n','')
    res=requests.get(Murl)
    res.raise_for_status()
    f4=open('HTML.txt','wb')
    for i in res.iter_content(1000000):
        f4.write(i)

    soup=bs4.BeautifulSoup(res.content,'html.parser')
    elem=soup.find_all('a', class_='ssl-item ep-item')
    #print(elem)
    name=soup.find('a',class_='text-white dynamic-name')
    title=name.get('title')
    #print(title)
    #print(len(elem))
    #print(elem[len(elem)-1])
    if k<limit:
        EpisodeList[k]=EpisodeList[k].replace('\n','')
        ep=EpisodeList[k]
        k=k+1
    else:
        ep=0
    #print(ep)
    ep=int(ep)
    if(ep==len(elem)):
       print(title+': ',len(elem),'No Update')
       status='No Update'
    else:
       print(title+': ',len(elem),'Latest')
       status='New Release'

    value=str(len(elem))
    f3.write(value)
    f3.write('\n')
    f5.write(title+': ')
    f5.write(value)
    f5.write(' '+status+'\n')





