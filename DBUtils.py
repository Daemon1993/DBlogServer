import threading
from functools import wraps

def asyncAction(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('asyncAction action')
        thread=threading.Thread(target=func, args=args, kwargs=kwargs,name='asyncThread')
        thread.start()
    return wrapper


@asyncAction
def saveImagetoDB(table,data):
    print(threading.current_thread().name)
    try:
        table.save(data)
    except Exception as e:
        print('本地存储失败 七牛存储成功 .{0}'.format(e))

