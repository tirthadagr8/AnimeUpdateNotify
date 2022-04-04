import webbrowser
import os
import requests
import bs4
###################################################  ONLY ANIMEHEAVEN.PRO LINKS SUPPORTED  #####################################################
#url='https://www.zoro.to/home'
#url='https://kissanime.com.ru/Login?redirect_to=/'
#url='http://facebook.com'
f1=open('AnimeUrlList.txt','r')
f2=open('AnimeUpdateOld.txt','r+')
f3=open('AnimeUpdateNew.txt','r+')
f5=open('C:\\Users\\tirth\\OneDrive\\Desktop\\Anime.txt','w')
k=0
Link=f1.readlines()
#print(Link)
EpisodeList=f2.readlines()
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
    elem=soup.find_all('a', class_='nav-link btn btn-sm btn-secondary eps-item')
    name=elem[0].get('title')
    name=name.replace('Episode 1','')
    #print(name+': ',len(elem))
    EpisodeList[k]=EpisodeList[k].replace('\n','')
    ep=EpisodeList[k]
    k=k+1
    #print(ep)
    ep=int(ep)
    #print('ep=',ep)
    #len(elem)
    status='0'
    #print(size)
    if(ep==len(elem)):
       print(name+': ',len(elem),'No Update')
       status='No Update'
    else:
       print(name+': ',len(elem),'Latest')
       status='New Release'
    value=str(len(elem))
    f3.write(value)
    f5.write(name+': ')
    f5.write(value)
    f5.write(' '+status+'\n')
    f3.write('\n')
       
    
    elem.clear()







