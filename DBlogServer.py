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

        return BaseCodes.login_require

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
        return BaseCodes.login_ok


    if request.method == 'POST':
        session['username']=request.form['username']
        return BaseCodes.do_ok




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
            data={'_id':result}
            print(data)
            data={'_id':result,'use':False}
            try:
                qiniu_upload_images.save(data)
            except Exception as e:
                return BaseCodes.getOkCode(e)
        else:
            result='error'
        return BaseCodes.getOkCode(result)




client=pymongo.MongoClient('localhost',27017)
db=client['Dblog']
qiniu_upload_images=db['qiniu_upload_images']
publish_article_list=db['publish_article_list']

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)


