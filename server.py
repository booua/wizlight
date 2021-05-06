from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from bulbMethods import getBulbStatus, turnOnBulb, turnOffBulb, getBulbIpAddress, toggleBulb, displayBulbScene
from dbcontroller import dbInit
from scenes import scenes
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
        result = ""
        try:
            turnOnBulb()
            result = "on"
        except:
            result = "error"
        return jsonify(result)

class BulbOff(Resource):
    def get(self):
        result = ""
        try:
            turnOffBulb()
            result = "off"
        except:
            result = "error"
        return jsonify(result)

class BulbToggle(Resource):
    def get(self):
        result = ""
        try:
            toggleBulb()
            result = "ok"
        except:
            result = "error"
        return jsonify(result)

class BulbScene(Resource):
    def get(self, sceneID):
        result = ""
        try:
            displayBulbScene(sceneID)
            result = scenes[int(sceneID)]
        except Exception as error:
            result = str(error)
        return jsonify(result)

api.add_resource(BulbStatus, routes['bulbStatus'])
api.add_resource(BulbOn, routes['bulbOn'])
api.add_resource(BulbOff, routes['bulbOff'])
api.add_resource(BulbToggle, routes['bulbToggle'])
api.add_resource(BulbScene, routes['bulbScene'])


if __name__ == '__main__':
     dbInit()
     getBulbIpAddress()
     app.run(port='5002')
