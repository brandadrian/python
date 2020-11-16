import os
import json
from pymongo import MongoClient
from flask import Flask, request

app = Flask(__name__)
usr = 'root' #os.environ['MONGO_DB_USER']
pwd = 'root' #os.environ['MONGO_DB_PASS']
client = MongoClient('mongodb+srv://' + usr + ':' + pwd + '@cluster0.srbj2.mongodb.net/running-event-db?retryWrites=true&w=majority')
db = client['running-event-db']
collection = db['running-event']

@app.route('/running-event')
def get():
    documents = collection.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)

@app.route('/running-event', methods=['POST'])
def post():
    req_data = request.get_json()
    collection.insert_one(req_data).inserted_id
    return ('', 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
