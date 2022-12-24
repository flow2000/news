# -*- coding:utf-8 -*-
# @Author: flow2000
import requests
import json
import random
import sys
import os
import time

from fastapi import FastAPI,File, UploadFile, Header, Depends, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from colorama import init
init(autoreset=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from weibo_api import weibo_api
from bili_api import bili_api
from sixty_api import sixty_api
from bing_api import bing_api
from api import FlowResponse

VERSION="2.0.0"

app = FastAPI()

# 设置CORS
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/version",tags=["VERSION"], summary="获取版本信息")
async def index():
    '''
    响应字段说明：
    - code:状态码
    - msg:部署信息
    - current_version:当前版本
    - latest_version:最新版本
    '''
    latest_version=""
    try:
        latest_version=requests.get('https://static.panghai.top/txt/version/news.txt',timeout=3).text
    except Exception as e:
        print(e)
        return FlowResponse.error(msg="NEWSAPI获取不到最新版本，但仍可使用，请联系：https://github.com/flow2000/news",data={"current_version":VERSION})
    data={
        "current_version":VERSION,
        "latest_version":latest_version
    }
    return FlowResponse.success(msg="news部署成功，查看接口文档：https://news.panghai.top/docs",data=data)

async def fetch(session, url):
    async with session.get(url, verify_ssl=False) as response:
        return await response.text()

@app.get("/weibo",tags=["微博热搜API"], summary="获取热搜json数据")
async def weibo():
    '''
    微博热搜API
    '''
    res=weibo_api.get_topic()
    if res!=None:
        return FlowResponse.success(data=res)
    else:
        return FlowResponse.error('系统发生错误')

@app.get("/bili",tags=["B站热搜API"], summary="获取热搜json数据")
async def bili():
    '''
    B站热搜API
    '''
    res=bili_api.get_topic()
    if res!=None:
        return FlowResponse.success(data=res)
    else:
        return FlowResponse.error('系统发生错误')

@app.get("/60s",tags=["60秒新闻API"], summary="获取今日新闻json数据")
async def sixty(offset: int = 0):
    '''
    请求字段说明：
    - offset:偏移量（可选参数：0,1,2,3），默认0表示今天，1表示昨天，2表示前天，3表示大前天。
    '''
    res=sixty_api.get_topic(offset)
    if res!=None:
        return FlowResponse.success(data=res)
    else:
        return FlowResponse.error('系统发生错误')

@app.get("/bing",tags=["必应壁纸API"], summary="获取必应壁纸json数据")
async def bili():
    '''
    必应壁纸API
    '''
    res=bing_api.get_bing()
    if res!=None:
        return FlowResponse.success(data=res)
    else:
        return FlowResponse.error('系统发生错误')

def iterfile(file_path):
    with open(file_path, "r", encoding='utf-8') as file_like:
        yield from file_like

@app.get("/",tags=["静态资源"], summary="首页", response_class=HTMLResponse)
async def index():
    res=''
    with open(os.getcwd()+'/index.html', "r", encoding='utf-8') as f:
        res=f.read()
        f.close()
    return res

@app.get("/index.js",tags=["静态资源"], summary="js")
async def js():
    return StreamingResponse(iterfile(os.getcwd()+'/index.js'), media_type="application/javascript")

@app.get("/news.css",tags=["静态资源"], summary="css")
async def css():
    return StreamingResponse(iterfile(os.getcwd()+'/news.css'), media_type="text/css")

@app.get("/favicon.svg",tags=["静态资源"], summary="图标")
async def favicon():
    return StreamingResponse(iterfile(os.getcwd()+'/favicon.svg'), media_type="image/svg+xml")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888)
