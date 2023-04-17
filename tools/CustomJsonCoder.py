#-*- coding: utf-8 -*-

import json as _json


from dataType.ListChained import ListChained


class JsonEncoder(_json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ListChained):
            return {"__class__" : "ListChained","data" : o.to_json()}
        
        return _json.JSONEncoder.default(self, o)
    

class JsonDecoder(_json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        _json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if '__class__' in obj:
            if obj['__class__'] == 'ListChained':
                temp = ListChained()
                temp.from_json(obj['data'])
                return temp
        return obj  