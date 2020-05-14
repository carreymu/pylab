import os
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
    str_s = '''
    {'loan': '1', 'insurance': '1', 'deliver_member': '1', 'credit_card': '1'}
    '''
    str_ss = '''
    [\"{\\\"category\\\": \\\"\\\\u6709\\\\u8d37\\\\u6b3e\\\", \\\"type\\\": \\\"1\\\", \\\"content\\\": \\\"\\\\u5c0a\\\\u656c\\\\u7684\\\\u5ba2\\\\u6237\\\\uff0c\\\\u60a8\\\\u5728\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u529e\\\\u7406\\\\u7684\\\\u4e2a\\\\u4eba\\\\u8d37\\\\u6b3e\\\\u9700\\\\u4e8e2019\\\\u5e7410\\\\u670810\\\\u65e517:00\\\\u524d\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u8fd8\\\\u6b3e\\\\u91d1\\\\u989d\\\\u672c\\\\u606f\\\\u5408\\\\u8ba13,292.95\\\\u5143\\\\uff0c\\\\u73b0\\\\u5c3e\\\\u53f71407\\\\u7684\\\\u8d26\\\\u6237\\\\u4f59\\\\u989d\\\\u4e0d\\\\u8db3\\\\uff0c\\\\u63d0\\\\u9192\\\\u60a8\\\\u6ce8\\\\u610f\\\\u3002\\\\u5982\\\\u60a8\\\\u672a\\\\u80fd\\\\u6309\\\\u65f6\\\\u8db3\\\\u989d\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u5c06\\\\u4f1a\\\\u5bf9\\\\u60a8\\\\u5728\\\\u4eba\\\\u6c11\\\\u94f6\\\\u884c\\\\u91d1\\\\u878d\\\\u4fe1\\\\u7528\\\\u4fe1\\\\u606f\\\\u57fa\\\\u7840\\\\u6570\\\\u636e\\\\u5e93\\\\u53ca\\\\u5176\\\\u4ed6\\\\u4f9d\\\\u6cd5\\\\u8bbe\\\\u7acb\\\\u7684\\\\u5f81\\\\u4fe1\\\\u673a\\\\u6784\\\\u4e2d\\\\u7684\\\\u5f81\\\\u4fe1\\\\u8bb0\\\\u5f55\\\\u4ea7\\\\u751f\\\\u4e0d\\\\u826f\\\\u5f71\\\\u54cd\\\\u3002\\\\u5982\\\\u60a8\\\\u5df2\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u8bf7\\\\u5ffd\\\\u7565\\\\u6b64\\\\u77ed\\\\u4fe1\\\\u3002\\\\u82e5\\\\u6709\\\\u7591\\\\u95ee\\\\u8bf7\\\\u54a8\\\\u8be2\\\\u60a8\\\\u529e\\\\u7406\\\\u4e1a\\\\u52a1\\\\u65f6\\\\u7684\\\\u8d37\\\\u6b3e\\\\u7ecf\\\\u529e\\\\u884c\\\\u6216\\\\u81f4\\\\u753595588\\\\u3002\\\\u3010\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u3011\\\", \\\"messagetime\\\": \\\"2019-10-05 08:33:27.715\\\"}\", \"{\\\"category\\\": \\\"\\\\u6709\\\\u94f6\\\\u884c\\\\u8d37\\\\u6b3e\\\", \\\"type\\\": \\\"1\\\", \\\"content\\\": \\\"\\\\u5c0a\\\\u656c\\\\u7684\\\\u5ba2\\\\u6237\\\\uff0c\\\\u60a8\\\\u5728\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u529e\\\\u7406\\\\u7684\\\\u4e2a\\\\u4eba\\\\u8d37\\\\u6b3e\\\\u9700\\\\u4e8e2019\\\\u5e7410\\\\u670810\\\\u65e517:00\\\\u524d\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u8fd8\\\\u6b3e\\\\u91d1\\\\u989d\\\\u672c\\\\u606f\\\\u5408\\\\u8ba13,292.95\\\\u5143\\\\uff0c\\\\u73b0\\\\u5c3e\\\\u53f71407\\\\u7684\\\\u8d26\\\\u6237\\\\u4f59\\\\u989d\\\\u4e0d\\\\u8db3\\\\uff0c\\\\u63d0\\\\u9192\\\\u60a8\\\\u6ce8\\\\u610f\\\\u3002\\\\u5982\\\\u60a8\\\\u672a\\\\u80fd\\\\u6309\\\\u65f6\\\\u8db3\\\\u989d\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u5c06\\\\u4f1a\\\\u5bf9\\\\u60a8\\\\u5728\\\\u4eba\\\\u6c11\\\\u94f6\\\\u884c\\\\u91d1\\\\u878d\\\\u4fe1\\\\u7528\\\\u4fe1\\\\u606f\\\\u57fa\\\\u7840\\\\u6570\\\\u636e\\\\u5e93\\\\u53ca\\\\u5176\\\\u4ed6\\\\u4f9d\\\\u6cd5\\\\u8bbe\\\\u7acb\\\\u7684\\\\u5f81\\\\u4fe1\\\\u673a\\\\u6784\\\\u4e2d\\\\u7684\\\\u5f81\\\\u4fe1\\\\u8bb0\\\\u5f55\\\\u4ea7\\\\u751f\\\\u4e0d\\\\u826f\\\\u5f71\\\\u54cd\\\\u3002\\\\u5982\\\\u60a8\\\\u5df2\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u8bf7\\\\u5ffd\\\\u7565\\\\u6b64\\\\u77ed\\\\u4fe1\\\\u3002\\\\u82e5\\\\u6709\\\\u7591\\\\u95ee\\\\u8bf7\\\\u54a8\\\\u8be2\\\\u60a8\\\\u529e\\\\u7406\\\\u4e1a\\\\u52a1\\\\u65f6\\\\u7684\\\\u8d37\\\\u6b3e\\\\u7ecf\\\\u529e\\\\u884c\\\\u6216\\\\u81f4\\\\u753595588\\\\u3002\\\\u3010\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u3011\\\", \\\"messagetime\\\": \\\"2019-10-09 08:42:33.359\\\"}\", \"{\\\"category\\\": \\\"\\\\u6709\\\\u8d37\\\\u6b3e\\\", \\\"type\\\": \\\"1\\\", \\\"content\\\": \\\"\\\\u60a8\\\\u5c3e\\\\u53f71407\\\\u536110\\\\u65e520:08\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u652f\\\\u51fa\\\\uff08\\\\u8d37\\\\u6b3e\\\\u8fd8\\\\u606f\\\\uff09735.19\\\\u5143\\\\uff0c\\\\u4f59\\\\u989d2,609.52\\\\u5143\\\\u3002\\\\u3010\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u3011\\\", \\\"messagetime\\\": \\\"2019-10-11 08:35:14.094\\\"}\", \"{\\\"category\\\": \\\"\\\\u6709\\\\u8d37\\\\u6b3e\\\", \\\"type\\\": \\\"1\\\", \\\"content\\\": \\\"\\\\u60a8\\\\u5c3e\\\\u53f71407\\\\u536110\\\\u65e520:08\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u652f\\\\u51fa\\\\uff08\\\\u8d37\\\\u6b3e\\\\u8fd8\\\\u672c\\\\uff092,557.76\\\\u5143\\\\uff0c\\\\u4f59\\\\u989d51.76\\\\u5143\\\\u3002\\\\u3010\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u3011\\\", \\\"messagetime\\\": \\\"2019-10-11 08:43:29.973\\\"}\", \"{\\\"category\\\": \\\"\\\\u6709\\\\u8d37\\\\u6b3e\\\", \\\"type\\\": \\\"1\\\", \\\"content\\\": \\\"\\\\u5c0a\\\\u656c\\\\u7684\\\\u5ba2\\\\u6237\\\\uff0c\\\\u60a8\\\\u5728\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u529e\\\\u7406\\\\u7684\\\\u4e2a\\\\u4eba\\\\u8d37\\\\u6b3e\\\\u9700\\\\u4e8e2019\\\\u5e7410\\\\u670810\\\\u65e517:00\\\\u524d\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u8fd8\\\\u6b3e\\\\u91d1\\\\u989d\\\\u672c\\\\u606f\\\\u5408\\\\u8ba13,292.95\\\\u5143\\\\uff0c\\\\u73b0\\\\u5c3e\\\\u53f71407\\\\u7684\\\\u8d26\\\\u6237\\\\u4f59\\\\u989d\\\\u4e0d\\\\u8db3\\\\uff0c\\\\u63d0\\\\u9192\\\\u60a8\\\\u6ce8\\\\u610f\\\\u3002\\\\u5982\\\\u60a8\\\\u672a\\\\u80fd\\\\u6309\\\\u65f6\\\\u8db3\\\\u989d\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u5c06\\\\u4f1a\\\\u5bf9\\\\u60a8\\\\u5728\\\\u4eba\\\\u6c11\\\\u94f6\\\\u884c\\\\u91d1\\\\u878d\\\\u4fe1\\\\u7528\\\\u4fe1\\\\u606f\\\\u57fa\\\\u7840\\\\u6570\\\\u636e\\\\u5e93\\\\u53ca\\\\u5176\\\\u4ed6\\\\u4f9d\\\\u6cd5\\\\u8bbe\\\\u7acb\\\\u7684\\\\u5f81\\\\u4fe1\\\\u673a\\\\u6784\\\\u4e2d\\\\u7684\\\\u5f81\\\\u4fe1\\\\u8bb0\\\\u5f55\\\\u4ea7\\\\u751f\\\\u4e0d\\\\u826f\\\\u5f71\\\\u54cd\\\\u3002\\\\u5982\\\\u60a8\\\\u5df2\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u8bf7\\\\u5ffd\\\\u7565\\\\u6b64\\\\u77ed\\\\u4fe1\\\\u3002\\\\u82e5\\\\u6709\\\\u7591\\\\u95ee\\\\u8bf7\\\\u54a8\\\\u8be2\\\\u60a8\\\\u529e\\\\u7406\\\\u4e1a\\\\u52a1\\\\u65f6\\\\u7684\\\\u8d37\\\\u6b3e\\\\u7ecf\\\\u529e\\\\u884c\\\\u6216\\\\u81f4\\\\u753595588\\\\u3002\\\\u3010\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u3011\\\", \\\"messagetime\\\": \\\"2019-10-09 08:42:33.359\\\"}\", \"{\\\"category\\\": \\\"\\\\u6709\\\\u94f6\\\\u884c\\\\u8d37\\\\u6b3e\\\", \\\"type\\\": \\\"1\\\", \\\"content\\\": \\\"\\\\u60a8\\\\u5c3e\\\\u53f71407\\\\u536110\\\\u65e520:08\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u652f\\\\u51fa\\\\uff08\\\\u8d37\\\\u6b3e\\\\u8fd8\\\\u672c\\\\uff092,557.76\\\\u5143\\\\uff0c\\\\u4f59\\\\u989d51.76\\\\u5143\\\\u3002\\\\u3010\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u3011\\\", \\\"messagetime\\\": \\\"2019-10-11 08:43:29.973\\\"}\", \"{\\\"category\\\": \\\"\\\\u6709\\\\u94f6\\\\u884c\\\\u8d37\\\\u6b3e\\\", \\\"type\\\": \\\"1\\\", \\\"content\\\": \\\"\\\\u5c0a\\\\u656c\\\\u7684\\\\u5ba2\\\\u6237\\\\uff0c\\\\u60a8\\\\u5728\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u529e\\\\u7406\\\\u7684\\\\u4e2a\\\\u4eba\\\\u8d37\\\\u6b3e\\\\u9700\\\\u4e8e2019\\\\u5e7410\\\\u670810\\\\u65e517:00\\\\u524d\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u8fd8\\\\u6b3e\\\\u91d1\\\\u989d\\\\u672c\\\\u606f\\\\u5408\\\\u8ba13,292.95\\\\u5143\\\\uff0c\\\\u73b0\\\\u5c3e\\\\u53f71407\\\\u7684\\\\u8d26\\\\u6237\\\\u4f59\\\\u989d\\\\u4e0d\\\\u8db3\\\\uff0c\\\\u63d0\\\\u9192\\\\u60a8\\\\u6ce8\\\\u610f\\\\u3002\\\\u5982\\\\u60a8\\\\u672a\\\\u80fd\\\\u6309\\\\u65f6\\\\u8db3\\\\u989d\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u5c06\\\\u4f1a\\\\u5bf9\\\\u60a8\\\\u5728\\\\u4eba\\\\u6c11\\\\u94f6\\\\u884c\\\\u91d1\\\\u878d\\\\u4fe1\\\\u7528\\\\u4fe1\\\\u606f\\\\u57fa\\\\u7840\\\\u6570\\\\u636e\\\\u5e93\\\\u53ca\\\\u5176\\\\u4ed6\\\\u4f9d\\\\u6cd5\\\\u8bbe\\\\u7acb\\\\u7684\\\\u5f81\\\\u4fe1\\\\u673a\\\\u6784\\\\u4e2d\\\\u7684\\\\u5f81\\\\u4fe1\\\\u8bb0\\\\u5f55\\\\u4ea7\\\\u751f\\\\u4e0d\\\\u826f\\\\u5f71\\\\u54cd\\\\u3002\\\\u5982\\\\u60a8\\\\u5df2\\\\u8fd8\\\\u6b3e\\\\uff0c\\\\u8bf7\\\\u5ffd\\\\u7565\\\\u6b64\\\\u77ed\\\\u4fe1\\\\u3002\\\\u82e5\\\\u6709\\\\u7591\\\\u95ee\\\\u8bf7\\\\u54a8\\\\u8be2\\\\u60a8\\\\u529e\\\\u7406\\\\u4e1a\\\\u52a1\\\\u65f6\\\\u7684\\\\u8d37\\\\u6b3e\\\\u7ecf\\\\u529e\\\\u884c\\\\u6216\\\\u81f4\\\\u753595588\\\\u3002\\\\u3010\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u3011\\\", \\\"messagetime\\\": \\\"2019-10-05 08:33:27.715\\\"}\", \"{\\\"category\\\": \\\"\\\\u6709\\\\u94f6\\\\u884c\\\\u8d37\\\\u6b3e\\\", \\\"type\\\": \\\"1\\\", \\\"content\\\": \\\"\\\\u60a8\\\\u5c3e\\\\u53f71407\\\\u536110\\\\u65e520:08\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u652f\\\\u51fa\\\\uff08\\\\u8d37\\\\u6b3e\\\\u8fd8\\\\u606f\\\\uff09735.19\\\\u5143\\\\uff0c\\\\u4f59\\\\u989d2,609.52\\\\u5143\\\\u3002\\\\u3010\\\\u5de5\\\\u5546\\\\u94f6\\\\u884c\\\\u3011\\\", \\\"messagetime\\\": \\\"2019-10-11 08:35:14.094\\\"}\"]
    '''
    print(json.loads(json.dumps(str_s)))

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
    print('username' in test[0])
    print(f'usernamesss {json.dumps(testSingle, ensure_ascii=False)}')
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

    # json object to python object
    json_to_python = json.loads(python_to_json)
    print("============json loads type ============")
    print(type(json_to_python))
    print("============json length============")
    print(len(json_to_python))
    for item in json_to_python:
        print(item["age"])
    print(json_to_python[1]['username'])

    print("============load json from file============")
    with open(os.path.abspath('file/jsonfile.json'), 'r') as f:
        # print(f.read())
        print(json.load(f))

    print("============json serialize============")
    p = Point(2, 3)
    s = json.dumps(p, default=serialize_instance)
    print(s)

    print("============json unserialize============")
    a = json.loads(s, object_hook=unserialize_object)
    print("a.x:{},a.y:{}".format(a.x, a.y))

    print('============distinct name============')
    t1 = [{"username": "测试", "age": 16, "isslut":False,"ismerry":None}, {"username": "测试122", "age": 12,"isslut":True,"ismerry":"yes"},
    {"username": "测试1", "age": 16,"isslut":False,"ismerry":None},{"username": "测试", "age": 17,"isslut":False,"ismerry":None}]
    t2 = [x['username'] for x in t1 if x['age']>12]
    print(set(t2))

    print('============list to tuple for sql.in============')
    in_params = {"req": {"fids": [1, 2, 3], "tids": ['4', '5', '6'], "fid": "m"}}
    print({k: tuple(v) for k, v in in_params["req"].items() if isinstance(v, list)})


