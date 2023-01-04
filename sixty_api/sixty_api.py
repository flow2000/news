import requests
from bs4 import BeautifulSoup
import json
import time


API='https://www.zhihu.com/api/v4/columns/c_1261258401923026944/items?limit=1&offset='
headers={
    'Access-Control-Allow-Origin':'*',
    'Access-Control-Allow-Headers':'Content-Type',
    'Access-Control-Allow-Methods':'*',
    'Content-Type':'application/json;charset=utf-8'
}


def get_topic(offset=0):
    res={}
    new_list=[]
    try:
        data=(requests.get(API+str(offset), headers=headers,timeout=5).json())
        html = data['data'][0]['content']
        soup = BeautifulSoup(html, 'html.parser')
        day_news = soup.find_all('p')
        for i in range(len(day_news)):
            text=day_news[i].get_text()
            if text!="":
                new_list.append(text)
        if len(new_list)>2:
            res['time']=new_list[0]
            res['topic']=new_list[1]
            res['weiyu']=new_list[len(new_list)-1]
            res['news']=new_list[2:-1]
        else:
            res['time']=""
            res['topic']=""
            res['weiyu']=""
            res['news']=[]
    except Exception as e:
        print(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())),e)
        return None
    return res