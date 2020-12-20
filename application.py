from flask import Flask,request,jsonify,make_response
from utils.autherization import required_token
from Config import config
import jwt_token
from functools import wraps
from flask_cors import CORS
import json
import itertools
from werkzeug.datastructures import ImmutableMultiDict
from base64 import b64encode
application=app=Flask(__name__)
CORS(app)
accepted_format=['image/jpeg','image/jpg','image/gif','image/png','image/txt']
#it is format of image

@app.route('/api/upload',methods=['GET'])
@required_token
def upload_image():
    try:

        img=request.files
        if img:
           data=ImmutableMultiDict(img)
           dict_data=data.to_dict(flat=False)
           upload=str(dict_data['image'][0])
           upload_file=upload.replace("FileStorage:", " ")
        if not img:
            return jsonify({'message':'please  upload image'}),401
        if upload_file:
            return jsonify({'message':' {} image sucessflly uploaded'.format(upload_file)}),201
        else:
            return jsonify({'message':'image not uploaded '}),400
    except Exception as err:
        print(err)
        return jsonify({'message':'something going wrong'}),500
if __name__ == "__main__":
   app.run(debug=True)
