import time
from datetime import datetime, timedelta, date
# from dateutil import parser

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
        day_num = start_date.weekday()
        day_num_target = weekdays.index(dayname)
        days_ago = (7 + day_num - day_num_target) % 7
        if days_ago == 0:
            days_ago = 7
        target_date = start_date - timedelta(days=days_ago)
    return target_date

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt


def datetime_timestamp(dt):
    # dt为字符串
    # 中间过程，一般都需要将字符串转化为时间数组
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
    # 将"2012-03-28 06:53:40"转化为时间戳
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)

def datediff_timestamp(starttime, endtime=None, rnd=True):
    """
    SQL的datediff函数是四舍五入的
    """
    if endtime is None:
        endtime = datetime.now()
    td = endtime - datetime.fromtimestamp(starttime // 1000)
    if rnd:
        result = round(td.days + td.seconds/86400)
    else:
        result = td.days + td.seconds/86400
    return result

if __name__ == "__main__":
    start = int(round(time.time() * 1000))
    print('start:{}'.format(start))  # 毫秒级时间戳
    print("============init date *** ============")
    a = timedelta(days=3, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print('c.days is :{},c.seconds:{}'.format(c.days, c.seconds))

    print(datetime.now().date())
    #parser.parser('2012-09-22T23:10:11')#
    a = datetime(2012, 9, 22, 23, 10, 11)
    print(a.date())
    b = datetime(2012, 9, 25, 23, 00, 10)
    now = datetime.today()
    print(date.today())

    for i in range(1, 6):
        print(i)

    print('a is :{},b - a:{},today:{},add minitus:{}'.format(a, (b-a).days, now, now + timedelta(days=-30)))

    print('today:{}'.format(datetime.now()))
    print('last Monday:{}'.format(get_previous_byday('Monday')))

    print("============add days to date *** ============")
    # text = '2018/10/10'
    y = datetime.strptime('12/04/2018', "%m/%d/%Y")
    print('string to date:%Y-%m-%d,diff:%d', y, datetime.today()-y)
    yp = datetime.strptime('20080819', "%Y%m%d")
    yf = datetime.strftime(yp, "%Y%m%d")
    print(f'yp:{yp},type of yp:{type(yp)},yf:{yf},type of yf:{type(yf)},diff:{datetime.today() - yp}')
    print(f'is bigger:{yp>y}')

    print("============long to datetime ============")
    your_timestamp = 1547379258906
    str = "2019-01-01 12:01:01"
    print('starttime is :'+str.split()[0])
    starttime = datetime.strptime(str.split()[0], "%Y-%m-%d")
    # starttime1 = datetime.strptime("2019-01-01 12:01:01", "%Y-%m-%d") # wrong convert
    # print('----')
    # print(starttime1)
    date = datetime.fromtimestamp(your_timestamp / 1e3)
    print(date)
    print((date-starttime).days)

    end = int(round(time.time() * 1000))
    print('end:{}'.format(end))  # 毫秒级时间戳
    print('time span:{}'.format(end-start))  # 毫秒级时间戳

    print("============get  days between unixtimes============")
    udays = datediff_timestamp(your_timestamp)
    print(udays)

    reg = "2016-01-24 21:15:47"
    tm = datetime.fromtimestamp(reg / (10 ** 9)) if isinstance(reg, int) else datetime.strptime(reg, "%Y-%m-%d %H:%M:%S")
    dt = datetime.now()
    age = (dt - tm).days
    print(age)
