from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ASDF123'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token') #http://127.0.0.1:5000/protected?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiIiwiZXhwIjoxNTkzOTM4MDM5fQ.qxoVo9dxfhMJUPU8xc8DBOF0CQ8JGRNAx0KIoCtVQhM

        if not token:
            return jsonify({'message' : 'Token is missing'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid'}), 403

        return f(*args, **kwargs)
    
    return decorated
        

@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'anyone can view this...'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'This is only available with valid tokens...'})

@app.route('/login')
def login():
    auth = request.authorization
    
    if auth and auth.password == 'root':
        token = jwt.encode({'user': auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')})
        
    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(debug=True)
