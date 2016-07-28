import json

class MySerializer(object):

    jsonstr = {'y': 2, 'x': 1, 'z': 3}

    @classmethod
    def deserializer(cls, jsonstr):
        #load from json to dict
        #initialize object, return
        json_data = json.loads(jsonstr)

        return cls(**json_data)

    def serializer(self):
        # iterate over self.my_attrs
        #get attrs, set into dictionary
        #return dumps(dictionary)
        pass
