import requests
import json
import time

API='https://weibo.com/ajax/side/hotSearch'
headers={
    'Access-Control-Allow-Origin':'*',
    'Access-Control-Allow-Headers':'Content-Type',
    'Access-Control-Allow-Methods':'*',
    'Content-Type':'application/json;charset=utf-8'
}


def get_topic():
    try:
        dataList=[]
        data=requests.get(API,headers=headers,timeout=5)
        data=json.loads(data.text)
        data_json=data['data']['realtime']
        jyzy = {
            '电影': '影',
            '剧集': '剧',
            '综艺': '综',
            '音乐': '音',
            '盛典': '盛',
        }
        for i in range(0,len(data_json)):
            hot = ''
            if 'is_ad' in data_json[i]:
                continue; 
            if 'flag_desc' in data_json[i]:
                hot = jyzy.get(data_json[i]['flag_desc'],'')
            if 'is_boom' in data_json[i]:
                hot = '爆'
            if 'is_hot' in data_json[i]:
                hot = '热'
            if 'is_fei' in data_json[i]:
                hot = '沸'
            if 'is_new' in data_json[i]:
                hot = '新'
            dic = {
                'title': data_json[i].get('note',''),
                'url': 'https://s.weibo.com/weibo?q=%23' + data_json[i].get('word','') + '%23',
                'num': data_json[i].get('num',''),
                'hot': hot
            }
            dataList.append(dic)
        return dataList
    except Exception as e:
        print(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())),e)
        return None