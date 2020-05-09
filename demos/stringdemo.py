import re
import base64

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

if __name__ == "__main__":
    sql = "select top 100 , nc_id , category_name  a_b,none, FROM  From news_category where status={status}".lower()
    sql_trim = sql[7: sql.find(' from ')].strip()
    li = sql_trim.split(',')
    print(sql_trim)
    print([x.strip().split(' ')[-1] for x in li if len(x) > 0 and 'top ' not in x])

    print("============String compare============")
    print('201808'.isdigit())
    print('201808' > '201807')
    print('201808' > '201809')
    
    d1,d2 = "area.provinceid".split(".")
    print(f"d1:{d1}, d2:{d2}")
    print(1 if '0' else 0)
    ration ='tongdun_Small_loan_3m_num_phone_ration'
    print(re.sub(r'\.|\-|\_', '',ration))
    ration_7 = ration[:-7]
    print(ration_7)
    *_, ruleid, _, match_type = ration_7.split("_")
    print("*"*20)
    match_type = {
        "express":"快递",
        "takeout":"外卖",
        "takeout_send": "外卖员",
        "takeout_receive": "外卖用户",
        "express_send": "快递员"
    }
    print(1 if match_type.get("express_send",None) else 0)
    str1 = "if_100_surname_express"
    str2 = "if_6_phone_in_nlp_takeout_receive"
    num, *_,hh, match = str1[3:].split("_")
    print(int(num)-2)
    print(hh)
    print(match)
    n,*_,h,m = str2[3:].split("_")
    print(int(n)-2)
    print(h)
    print(m)
    print("*"*20)

    (a, b, c) = ("-1.0",) *3
    # wrong (a, b, c) = ("-1.0") * 3
    print(a, b, c)
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

    delimiters = "a", "...", "(C)"
    regexPattern = '|'.join(map(re.escape, delimiters))  # 'a|\\.\\.\\.|\\(C\\)'
    line = "stackoverflow (C) is awesome... isn't it?"
    print(re.split(regexPattern, line))

    print('.' in '3.')
    head, tail = '3.'.split(".")
    res = float('3'+'.'+'445')
    print(f'head:{head},tail:{tail},result:{res}')

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
    if(any(name.endswith(('com', 'cz'))) for name in urls):
        print('any matched, do sth.')

    print("============String replace in formating============")
    s = '{name} has {n} messages.'
    print("s = '{name} has {n} messages.'", s.format(n=2, name='Jerry'))
    nm = "tom"
    n = 10
    print('$$' * 5)
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
