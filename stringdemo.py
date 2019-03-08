import re
import base64

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

if __name__ == "__main__":
    (a,b,c) = ("-1.0",)*3
    # wrong (a, b, c) = ("-1.0") * 3
    print(a,b,c)
    print(len('少年宪法对'))
    print("============String split============")
    line = 'asdf fjdk; afed, fjek,asdf, | foo'
    flds = re.split(r'[;\|,\s]\s*', line)
    print('flds string ', flds)
    vals = flds[::2]
    print('vals is ', vals)
    flds1 = re.split(r'(;|\||,|\s)\s*', line)
    print('flds1 string ', flds1)
    dellimiters = flds1[1::2]
    print('dellimiters string ', dellimiters)

    flds2 = '---'.join(v+d for v, d in zip(vals, dellimiters))
    print('vals is %s,dellimiters is %s ' % (vals, dellimiters))
    print('flds2 string ', flds2)

    a, b, c = 'a', 'b', 1
    print(a, b, c, sep=',')

    print("============String endswith/startswith============")
    url = "http://www.baidu.com"
    print('is url start with http?', url.startswith('http'))
    print('is url end with http?', url.endswith('http'))

    urls = ["http://www.baidu.com",'https://www.google.com']
    [print('is %s startswith %s?%s' % (url, 'http', url.startswith('https'))) for url in urls]
    lstStart = ['http', 'https', 'ftp']
    url = "baidu.com"
    res = url.startswith(tuple(lstStart))
    print('startswith use list.', res)
    if(any(name.endswith(('com','cz'))) for name in urls):
        print('any matched, do sth.')

    print("============String replace in formating============")
    s = '{name} has {n} messages.'
    print("s = '{name} has {n} messages.'", s.format(n=2, name='Jerry'))
    nm = "tom"
    n = 10
    print(f"s = '{nm} has {n} messages.'")
    n = 2
    name = "Marry"
    bs = s.format_map(vars())
    print("bs is ", bs)

    obj = Info(name='Carrey', n=3)
    print('object replace result is:', s.format_map(vars(obj)))

    print("============add blanks to String============")
    import textwrap
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."
    print('rextwrap result is:', textwrap.fill(s, 700))
    print('rextwrap result is:', textwrap.fill(s, 700, initial_indent= " --"))

    print("============encode String with base64============")
    t = 'Hello World'
    print('first letter is:', t[0])
    encodet = base64.b64encode(b'Hello World')
    print('encode result', encodet)
    # print('encode result is '+ t.encode('base64', 'strict'))
    print('decode result', base64.b64decode(encodet))


    print("============first loop to String============")
    for i in range(len(t)):
        print('letter{} is:{}'.format(i, t[i]))
    print("------------")
    for i in range(2,len(t)):
        print('letter2{} is:{}'.format(i, t[i]))
    print("============second loop to String============")
    for i, ch in enumerate(t):
        print("letter{} is：{}".format(i, ch))
    # print(('result is :'+c for c in t))
    for c in t:
        print("DDD", c)

    queerChars = "・*？|.�@"
    if('�' in queerChars):
        print('yes')
    else:
        print('no')

    strs = "www.runoob.com"
    print(strs.upper().find("RUN"))  # 把所有字符中的小写字母转换成大写字母
    print(strs.lower())  # 把所有字符中的大写字母转换成小写字母
    print(strs.capitalize())  # 把第一个字母转化为大写字母，其余小写
    print(strs.title())  # 把每个单词的第一个字母转化为大写，其余小写

    print("============second loop to String============")
    string2 = "Test String leading space to be added"
    string_length = len(string2) + 10  # will be adding 10 extra spaces
    string_revised = string2.rjust(string_length)
    print(string_revised)
    string_revised = string2.ljust(string_length)
    print(string_revised)
    string_revised = string2.center(string_length)
    print(string_revised)
    print('  '.join(string2))

    print('这个是用 |连接起来的'.find('严重逾期| 已经逾期|逾期已超'))

    print('这个是用 |连接起来的严重逾期| 已经逾期|逾期已超'.find('严重逾期| 已经逾期|逾期已超'))

    #{"Phrase":"finish","Remark":"已上传","Status":100}
    str_demo = {"Phrase":"finish","Remark":"已上传","Statuss":100}
    if str(str_demo) != '[]':
        print(str_demo.get('Status',-1))
    else:
        print('yes')
