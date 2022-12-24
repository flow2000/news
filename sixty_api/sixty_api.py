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
            if i == 0:
                continue
            if i == 1:
                res['time']=text
                continue
            if i == 2:
                res['topic']=text
                continue
            if i == len(day_news)-1:
                res['weiyu']=text
                continue
            new_list.append(text)
        res['news']=new_list
    except Exception as e:
        print(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())),e)
        return None
    return res