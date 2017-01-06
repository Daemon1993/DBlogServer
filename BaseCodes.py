__author__ = 'Daemon1993'
import json


#json 中文
def getJsonStr(msg):
    return json.dumps(msg,ensure_ascii=False)


#权限不够 需要登陆
login_require=getJsonStr({'code':100,'msg':'未登录'})
login_ok=getJsonStr({'code':200,'msg':'已经登陆'})


#自定义返回吗 msg
def getOkCode(msg):
    return getJsonStr({'code':0,'msg':msg})


do_ok=getJsonStr({'code':0,'msg':'ok'})


