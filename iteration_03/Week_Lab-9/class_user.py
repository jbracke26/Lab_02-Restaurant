from utils import loadjson, savejson, randomage, randomname, randomhobby
class user:
    def __init__(self):
        pass
    def usergenerate(self):
        userdata = loadjson()
        new_user = {
            "name" : randomname(),
            "age" : randomage(),
            "hobby" : randomhobby()
        }
        userdata.append(new_user)
        savejson(userdata)