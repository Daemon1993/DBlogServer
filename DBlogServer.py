import os
import pymongo
from flask import Flask, request
from functools import wraps
from flask import make_response
import QiNiuAction

app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

print(APP_ROOT)

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst

    return wrapper_fun


@app.route('/publish',methods=['POST'])
@allow_cross_domain
def publish():
    print('publish start')
    if request.method == 'POST':
        
        return 'Hello World!'


@app.route('/upload', methods=['POST'])
@allow_cross_domain
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
            data={'_id':result}
            qiniu_upload_images.save(data)
        else:
            result='error'

        print(result)
        return result



client=pymongo.MongoClient('localhost',27017)
db=client['Dblog']
qiniu_upload_images=db['qiniu_upload_images']

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)


