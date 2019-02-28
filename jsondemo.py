import json
from pprint import pprint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d

classes = {"Point": Point}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        # Make instance without calling __init__
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

if __name__ == '__main__':
    # 将python对象test转换json对象
    test = [{"username": "测试", "age": 16,"isslut":False,"ismerry":None}, {"username": "测试122", "age": 12,"isslut":True,"ismerry":"yes"}]
    testSingle = {
      "email": "email",
      "idNumber": "idNumber",
      "mobile": "mobile",
      "qq": "qq",
      "realName": "realName",
      "userId": "userId",
      "userName": "userName"
    }
    sJson = json.loads(json.dumps(testSingle, ensure_ascii=False))
    print(sJson)
    for item in sJson:
        print(item[0])
    print(type(test))
    python_to_json = json.dumps(test, ensure_ascii=False)
    print("============json type convert result============")
    print(python_to_json)
    pprint(python_to_json)
    print(type(python_to_json))

    print("============json loads OrderedDict ============")
    # from collections import OrderedDict
    # dt = '{"username": "测试", "age": 16,"isslut":False,"ismerry":None}'
    # data = json.loads(dt, object_pairs_hook=OrderedDict)
    # print(data)

    # 将json对象转换成python对象
    json_to_python = json.loads(python_to_json)
    print("============json loads type ============")
    print(type(json_to_python))
    print("============json length============")
    print(len(json_to_python))
    for item in json_to_python:
        print(item["age"])
    print(json_to_python[1]['username'])

    print("============load json from file============")
    with open('file/jsonfile.json', 'r') as f:
        # print(f.read())
        print(json.load(f))

    print("============json serialize============")
    p = Point(2, 3)
    s = json.dumps(p, default=serialize_instance)
    print(s)

    print("============json unserialize============")
    a = json.loads(s, object_hook=unserialize_object)
    print("a.x:{},a.y:{}".format(a.x, a.y))

    print('---------distinct---------')
    t1 = [{"username": "测试", "age": 16,"isslut":False,"ismerry":None}, {"username": "测试122", "age": 12,"isslut":True,"ismerry":"yes"},{"username": "测试1", "age": 16,"isslut":False,"ismerry":None},{"username": "测试", "age": 17,"isslut":False,"ismerry":None}]

    # dict([d.items()[0] for d in t1]).items()之外的部分纯粹是把列表内还原成一个字典
    t2 = [x['username'] for x in t1 if x['age']>12]
    print(len(set(t2)))


