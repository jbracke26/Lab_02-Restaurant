from utils import loadjson, savejson, randomage, randomname, randomhobby
from flask import jsonify
class user:
    def __init__(self):
        pass
    def usergenerate(self):
        users = loadjson()
        new_user = {
            "name" : randomname(),
            "age" : randomage(),
            "hobby" : randomhobby()
        }
        users.append(new_user)
        savejson("userdata.json", users)
        return jsonify(new_user)