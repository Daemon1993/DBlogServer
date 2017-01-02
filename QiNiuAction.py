__author__ = 'Daemon1993'

from qiniu import Auth, put_data, etag,BucketManager
import qiniu.config
a_k='d2ZWIj-W2b1NfddBDQtNRT_IsLFlIgbt1SxekFZ2'
s_k='8xv2Nb81ogMG5YCbF40NyBp2lNQ60g5MGIRROHH3'
q = Auth(a_k, s_k)


#要上传的空间
bucket_name = 'dblog'

def uploadServer(data,filename):

    #上传到七牛后保存的文件名
    key = filename;

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    ret, info = put_data(token, key, data)
    if(info.status_code==200):
        #数据库 记录 上传的文件名 在文章发布的时候 删掉无用图片
        return key
    else:
        return None

