from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from bulbMethods import getBulbStatus, turnOnBulb, turnOffBulb, getBulbIpAddress, toggleBulb
from dbcontroller import dbInit
from routes import routes
import asyncio

app = Flask(__name__)
api = Api(app)
        
class BulbStatus(Resource):
    def get(self):
        result = {'data': getBulbStatus()}
        return jsonify(result)

class BulbOn(Resource):
    def get(self):
        result = {'data': turnOnBulb()}
        return jsonify(result)

class BulbOff(Resource):
    def get(self):
        result = {'data': turnOffBulb()}
        return jsonify(result)

class BulbToggle(Resource):
    def get(self):
        result = {'data': toggleBulb()}
        return jsonify(result)

api.add_resource(BulbStatus, routes['bulbStatus'])
api.add_resource(BulbOn, routes['bulbOn'])
api.add_resource(BulbOff, routes['bulbOff'])
api.add_resource(BulbToggle, routes['bulbToggle'])


if __name__ == '__main__':
     dbInit()
     getBulbIpAddress()
     app.run(port='5002')
