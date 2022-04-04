import webbrowser
import os
import requests
import bs4
import datetime
import time
Now = datetime.datetime.now()
################################################  ONLY KISSAIME.CO LINKS SUPPORTED  ######################################################
#url='https://www.zoro.to/home'
#url='https://kissanime.com.ru/Login?redirect_to=/'
#url='http://facebook.com'
f1=open('AnimeUrlList.txt','r')
f2=open('AnimeUpdateOld.txt','r+')
f3=open('AnimeUpdateNew.txt','r+')
f5=open('C:\\Users\\tirth\\OneDrive\\Desktop\\AnimeLog.txt','a+')
f6=open('Timer.txt','r+')
f7=open('r_Timer.txt','r+')
k=0
point=0
status='0'
Link=f1.readlines()
#print(Link)
EpisodeList=f2.readlines()
limit=len(EpisodeList)
#print(EpisodeList)
f2.truncate(0)
f2.seek(0)
garbage=f3.read()
f2.write(garbage)
f3.seek(0)
f3.truncate(0)
time_read=f6.readlines()
print(time_read)
time.sleep(1)
os.system('cls')
f6.truncate()
f6.seek(0)
dump=f7.read()
#print('dump=',dump)
#f6.write(dump)
f7.truncate()
f7.seek(0)

#def printSpace(x):

for url in Link:
    time_read[point]=time_read[point].replace('\n','')
    last_release_time=datetime.datetime.strptime(time_read[point], '%Y-%m-%d %H:%M:%S')
    future_release_time=last_release_time+datetime.timedelta(days=7)
    present_time=datetime.datetime.now()
    time_left=future_release_time-present_time
    time_left_str=str(time_left)
    if time_left_str[0]=='-':
        print('NEGATIVE')
        last_release_time=future_release_time
        f6.write(str(last_release_time))
        f6.write('\n')
        future_release_time+=datetime.timedelta(days=7)
        time_left=future_release_time-present_time
        f7.write(str(future_release_time))
        f7.write('\n')
    else:
        f7.write(str(last_release_time))
        f7.write('\n')
        f6.write(str(last_release_time))
        f6.write('\n')
    count=0
    #print(url)
    Murl=url.replace('\n','')
    res=requests.get(Murl)
    res.raise_for_status()
    f4=open('HTML.txt','wb')
    for i in res.iter_content(1000000):
        f4.write(i)

    soup=bs4.BeautifulSoup(res.content,'html.parser')
    elem=soup.find_all('span', class_='jtitle')
    #print(elem)
    title=elem[0].get('data-jtitle')
    for jp in elem:
        name_=jp.get('data-jtitle')
        #print(name_)
        if title==name_:
            count+=1

    count-=1
    point+=1
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
    spaces=60-len(title)
    print(spaces)
    if(ep==count):
       print(title+':',' '*spaces,'No Update:       ',count, '      ',time_left)#,printSpace(spaces),'No Update  ',count,'      ',time_left)
       status='No Update'
    else:
       print(title+':',' '*spaces,'Latest Release:  ',count, '      ',time_left)#   +': No Update   ',count,'      ',time_left)
       status='New Release'

    value=str(count)
    f3.write(value)
    f3.write('\n')
    f5.write(title+': ')
    f5.write(value)
    f5.write(' '+status+'\n')

#input()

