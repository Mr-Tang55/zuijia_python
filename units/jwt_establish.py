import jwt
import datetime

def jwt_establish(name,id):
    exp_date = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    return jwt.encode({'exp': exp_date,'id':id,'username': name}, 'secret', algorithm='HS256')
