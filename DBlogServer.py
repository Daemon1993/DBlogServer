import os
import pymongo
import json
from flask import Flask, request,session,g
from functools import wraps
from flask import make_response
import QiNiuAction
import BaseCodes

app = Flask(__name__)
app.secret_key =os.urandom(24)
print(app.secret_key)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

print(APP_ROOT)

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        print(' allow_cross_domain wrapper_fun')
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = 'http://localhost:9999'
        rst.headers['Access-Control-Allow-Credentials'] = 'true'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        print('域名 func over')
        return rst

    return wrapper_fun

def login_require(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('login_require {0}'.format(g))

        if 'username' in session:
            return func(*args, **kwargs)

        print('未登录 {0}'.format(BaseCodes.login_require))

        return json.dumps(BaseCodes.login_require,ensure_ascii=False)

    return wrapper



@app.route('/publish',methods=['POST'])
@allow_cross_domain
@login_require
def publish():

    if request.method == 'POST':
        return 'Hello World!'



@app.route('/login',methods=['POST'])
@allow_cross_domain
def login():
    print('login start {0}'.format(session))

    if 'username' in session:
<<<<<<< HEAD
        return 'Logged in ok '+session['username']
=======
         return json.dumps(BaseCodes.login_ok,ensure_ascii=False)
>>>>>>> 7712d637756c839c654f45bafef507484142fb7e

    if request.method == 'POST':
        session['username']=request.form['username']
        return json.dumps(BaseCodes.do_ok,ensure_ascii=False)




@app.route('/upload', methods=['POST'])
@allow_cross_domain
@login_require
def upload_file():
    print('upload coming')
    if request.method == 'POST':
        print(request.form)
        f = request.files['file']

        print(request.form['filename'])
        # f.save(os.path.join(UPLOAD_FOLDER, request.form['filename']))
        result=QiNiuAction.uploadServer(f,request.form['filename'])
        if(result is not None):
             #插入数据库
<<<<<<< HEAD
            data={'_id':result}
            print(data)
            # qiniu_upload_images.save(data)
=======
            data={'_id':result,'use':False}
            qiniu_upload_images.save(data)
>>>>>>> 7712d637756c839c654f45bafef507484142fb7e
        else:
            result='error'
        return json.dumps(BaseCodes.getOkCode(result))

<<<<<<< HEAD
        print('result '+result)
        return result
=======
>>>>>>> 7712d637756c839c654f45bafef507484142fb7e



client=pymongo.MongoClient('localhost',27017)
db=client['Dblog']
qiniu_upload_images=db['qiniu_upload_images']
publish_article_list=db['publish_article_list']

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)


