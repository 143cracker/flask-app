import jwt
from Config import config
from functools import wraps
from flask import request,jsonify
accesstoken=config.API_KEY
def required_token(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        token=None
        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']
        if token!=accesstoken and token!=None:
            return jsonify({'message':'token is invailid '}),402
        if not token:
           return jsonify({'message':'token missing'}),401
        try:
            #data=jwt.decode(token,config.SECRETE_KEY)
            pass

        except Exception as err:
            print(err)
            return jsonify({'message':'token is invailid '}),402
        return f(*args,**kwargs)
    return decorator
