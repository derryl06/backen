from flask import Flask
from flask_restful import Api, Resource
import json
app = Flask(__name__)
api = Api(app)


class Tribun(Resource):
    def get(self):
        tribun = open("tribun.json", "r")
        jsonTribun = json.load(tribun)
        return {"tribun": jsonTribun}

class Tribuntrend(Resource):
    def get(self):
        tribuntrend = open("tribuntrend.json", "r")
        jsonTribuntrend = json.load(tribuntrend)
        return {"tribuntrend": jsonTribuntrend}

class Epaper(Resource):
    def get(self):
        epaper = open("epaper.json", "r")
        jsonEpaper = json.load(epaper)
        return {"epaper": jsonEpaper}


api.add_resource(Tribun, '/tribun/')
api.add_resource(Tribuntrend, '/tribuntrend/')
api.add_resource(Epaper, '/epaper/')


if __name__ == '__main__':
    app.run()
