import json

class MySerializer(object):

    @classmethod
    def deserializer(cls, jsonstr):
        #load from json to dict
        #initialize object, return
        json_data = json.loads(jsonstr)

        return cls(**d)

