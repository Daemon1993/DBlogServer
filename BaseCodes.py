__author__ = 'Daemon1993'


#权限不够 需要登陆
login_require={'code':100,'msg':'未登录'}
login_ok={'code':200,'msg':'已经登陆'}



def getOkCode(msg):
    return {'code':0,'msg':msg}

do_ok={'code':0,'msg':'ok'}
