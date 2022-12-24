from fastapi.responses import JSONResponse

def success(msg="操作成功",data=None):
    res_json = {}
    res_json['code']=200
    res_json['msg']=msg
    if data!=None:
        res_json['data']=data
    return JSONResponse(status_code=200, content=res_json)

def error(msg="操作失败",data=None):
    res_json = {}
    res_json['code']=500
    res_json['msg']=msg
    if data!=None:
        res_json['data']=data
    return JSONResponse(status_code=500, content=res_json)
