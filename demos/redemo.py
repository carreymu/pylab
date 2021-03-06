import re
def phone(n):
    #n = input("请输入一个手机号：")
    re_phone = r"^.*[1][3-9][0-9]{9}.*$"
    re_tel = r"^(010\d{8})|(0[2-9]\d{9})$"
    re_tel_phone = r"(0[0-9]{2,3}\-)?([2-9][0-9]{6,7})+(\-[0-9]{1,4})?$"
    if re.match(r'1[3,4,5,6,7,8]\d{9}',n):
        print("您输入的的手机号码是：\n",n)
        #中国联通：
        # 130，131，132，155，156，185，186，145，176
        if re.match(r'13[0,1,2]\d{8}',n) or \
            re.match(r"15[5,6]\d{8}",n) or \
            re.match(r"18[5,6]",n) or \
            re.match(r"145\d{8}",n) or \
            re.match(r"176\d{8}",n):
            print("该号码属于：中国联通")
        #中国移动
        # 134, 135 , 136, 137, 138, 139, 147, 150, 151,
        # 152, 157, 158, 159, 178, 182, 183, 184, 187, 188；
        elif re.match(r"13[4,5,6,7,8,9]\d{8}",n) or \
            re.match(r"147\d{8}|178\d{8}",n) or \
            re.match(r"15[0,1,2,7,8,9]\d{8}",n) or \
            re.match(r"18[2,3,4,7,8]\d{8}",n):
            print("该号码属于：中国移动")
        else:
            #中国电信
            #133,153,189
            print("该号码属于：中国电信")
    else:
        print("请输入正确的手机号")

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace

if __name__ == "__main__":
    print("============find all match String ============")
    print('200'>'50')
    datepat = re.compile(r'\d+/\d+/\d+')
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    allMatch = datepat.findall(text)
    print("allMatch is :", allMatch)
    string = "[('您好：验证码为764951，您正在进行手机注册，若非本人操作64951，还7天逾期。',)]查询返回的是这个"
    print("allMatch10 is :", re.findall(r"还.*?天逾期*", string)[0])

    str_s = '尊敬的客户，您于2018年05月25日00时15分，已成功充值+30.01元。和包充话费，省钱更优惠。回复“HB”或点击http://dx.10086.cn/UYjYbeq，新注册即可领取50元话费券+500M省内流量。【中国移动】'
    # (-?\d+)(.\d+) 
    # ([+-]?(\d+|\d*\.\d{2}))
    # [\\+\\-]?[\\d]+(\\.[\\d]+)?
    print("str_add_e is :", re.findall(r"(充值|交费|缴纳了|为本机充值|成功缴费|成功交纳话费|充值（交费）|成功缴费/充值)([+-]?(\d+|\d*\.\d{1,2}))(元+)", str_s))
    print("str_s is :", re.findall(r"(余额|余额为|余额是|账户余额为|可用额度为)([+-]?(\d+|\d*\.\d{1,2}))(元+)", str_s))
    regx = re.compile(r"【(.*?)】")
    print("【str_s is】 :", regx.findall(str_s)[0])

    string = "[('您好：取验证为764951，您正在进行手机成功注册，若非本人操作64951，还7天逾期。',)]查询返回的是这个"
    print("allMatch11 is :", re.findall(r"(^取验证码)[成功注册|注册成功|成功激活]*", string))

    string = "[('您好：验证码为764951，您正在进行手机注册，若非本人操作64951，请及时联系我。',)]查询返回的是这个"
    print("allMatch12 is :", re.findall(r"\d+\.?\d*", string))
    # tp = re.compile(r'(\d+)')
    # res = tp.sub(r'\1', textx)
    # print("res11 is ", res)

    print("============replace matched String============")
    re_com = re.compile(r"\d+\.?\d*")
    result, number = re_com.subn('--($_$)!!', string)
    print(f'find matched num:{number}, replaced string:{result}')

    print("============find all match group ============")
    aaa = "aa额度: dafdaf调度: fdafdaf费率: fdafdaf"
    d = re.compile(r'.*?额度: (.*)调度')
    dm = d.match(aaa)
    print(dm.groups())

    datepa = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = datepa.match('11/27/2012')
    print(" m.group() is %s,m.group(0) is %s, m.group(1) is %s, m.group(2) is %s" % (m.groups(), m.group(0), m.group(1), m.group(3)))
    month, day, year = m.groups()
    print("month:{}, day,:{} year:{}".format(month, day, year))

    print("============find accurate match String ============")
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
    print("datepat.match('11/27/2012abcdef') is :", datepat.match('11/27/2012abcdef'))
    print("datepat.match('11/27/2012') is :", datepat.match('11/27/2012'))
    print("re.findall(r'(\d+)/(\d+)/(\d+)', text) is ", re.findall(r'(\d+)/(\d+)/(\d+)', text))

    print("============find match String and replace ============")
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.取联系人电话mobilephone,还钱20'
    repStr = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print("repStr.format is ", repStr)
    datep = re.compile(r'(\d+)/(\d+)/(\d+)')
    res = datep.sub(r'\3-\1-\2',text)
    print("res is ", res)

    cmp = re.compile(r'^.*(还钱|欠钱).*$')
    matchObj = cmp.search(text)
    if matchObj:
        print("repStr.1 is ", matchObj.group())
    else:
        print("Do not find match string")

    aa = re.search("1[34578]\\d{9}$", "13020280822")
    re_tel = r"^(010\d{8})|(0[2-9]\d{9})$"
    bb = re.search(re_tel, '0086400291')
    print(('none' if bb is None else bb[0]))



    print("============ignore upper/lowercase and replace string ============")
    text = 'UPPER PYTHON, lower python, Mixed Python'
    print("findall result:", re.findall('python', text, flags=re.IGNORECASE))
    print("find and replace string,ignore upper/lowercase:", re.sub('python', 'java', text, flags=re.IGNORECASE))
    print("find and replace string,not ignore upper/lowercase:", re.sub('python', matchcase('java'), text, flags=re.IGNORECASE))

    print("============re greedy and not greedy string ============")
    str_pat1 = re.compile(r'\"(.*)\"')
    str_pat2 = re.compile(r'\"(.*?)\"')
    text2 = 'Computer says "no." Phone says "yes."'
    print('greedy info:', str_pat1.findall(text2))
    print('shortest info:', str_pat2.findall(text2))

    print("============trim string ============")
    s = ' hello world \n'
    print("strip result:", s.strip())
    print('lstrip result:', s.lstrip())
    print('rstrip result:', s.rstrip())

    t = '-----hel=lo=====ooollll'
    print('lstrip char', t.strip('-'))
    print('lstrip char', t.strip('-=lo'))

    print("============translate string ============")
    s = 'pýtĥöñ\fis\tawesome\r\n'
    remap = {
        ord('\f'): " ",
        ord('\t'): " ",
        ord('\r'): " "
    }
    print('translate result is :', s.translate(remap))

    print("============translate string ============")
    print('add blanks on the left:', t.ljust(20))
    # print('add blanks on the left:', s.rjust(20, '=='))

    print("============check input string, only contains alphabets、numbers and length>8 ============")
    line = "a123044%"
    res = re.search('^(?![A-Z]+$)(?![a-z]+$)(?!\d+$)(?![\W_]+$)\S{8,}$', line)
    print(res.group())
    if res:
        print('YES')
    else:
        print("NO")

    r = re.compile('^[a-z]+$', re.I)
    line2 = "A"
    print(len('zhangsan'))
    print(len('张三'))
    if r.match(line2):#re.search('^(?![A-Z]+$)(?![a-z]+$)$', line2):
        print('YES')
    else:
        print("NO")

    print("============check phone number is available ============")
    phone("13888888829")
