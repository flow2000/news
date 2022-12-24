import requests
import json
import time


API='https://bing.com/HPImageArchive.aspx?n=7&format=js&idx=0&mkt=zh-CN'
headers={
    'Access-Control-Allow-Origin':'*',
    'Access-Control-Allow-Headers':'Content-Type',
    'Access-Control-Allow-Methods':'*',
    'Content-Type':'application/json;charset=utf-8'
}


def get_bing():
    res_list=[]
    try:
        data=(requests.get(API, headers=headers,timeout=5).json())
        bing_list = data['images']
        for item in bing_list:
            tmp={}
            tmp['title']=item['title']
            tmp['url']='https://cn.bing.com'+item['urlbase']+'_1920x1080.jpg'
            tmp['copyright']=item['copyright']
            str_time=item['enddate']
            tmp['time']=str_time[0:4]+"-"+str_time[4:6]+"-"+str_time[6:8]
            res_list.append(tmp)
    except Exception as e:
        print(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())),e)
        return None
    return res_list