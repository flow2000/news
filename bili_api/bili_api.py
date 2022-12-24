import requests
import json
import time
API='https://app.bilibili.com/x/v2/search/trending/ranking'
headers={
    'Access-Control-Allow-Origin':'*',
    'Access-Control-Allow-Headers':'Content-Type',
    'Access-Control-Allow-Methods':'*',
    'Content-Type':'application/json;charset=utf-8'
}

def get_topic():
    try:
        dataList=[]
        data=requests.get(API,headers=headers,timeout=8)
        data=json.loads(data.text)
        data_json=data['data']['list']
        for i in range(0,len(data_json)):
            dic = {
                'title': data_json[i].get('show_name',''),
                'keyword': data_json[i].get('keyword',''),
                'url': 'https://search.bilibili.com/all?keyword=' + data_json[i].get('keyword',''),
                'icon': data_json[i].get('icon','')
            }
            dataList.append(dic)
        return dataList
    except Exception as e:
        print(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())),e)
        return None