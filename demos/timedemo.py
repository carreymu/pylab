from datetime import datetime, timedelta
import time

if __name__ == "__main__":
    nowtime = datetime.now()
    print(nowtime)

    start = int(round(time.time()))
    print(f'start:{start}')
    print(f'start time:{time.time()}')
    lasthour = datetime(2018, 5, 7, 23, 11, 12, 926763)
    lasthour_str = str(lasthour)
    print(lasthour_str)

    lasthour_new = datetime.strptime(lasthour_str, '%Y-%m-%d %H:%M:%S.%f')

    your_timestamp = 1525271006858
    dat = datetime.fromtimestamp(your_timestamp / 1e3)

    print('==========isinstance==========')
    print(isinstance(1538306854000, int))
    print(isinstance(lasthour_new, datetime))
    print(isinstance(dat, datetime))
    print(isinstance(str(dat), str))
    print(dat)
    td = lasthour - dat
    result = round(td.days + td.seconds / 86400)
    print(result)
    print(str(dat))
    print('==========')


    print(lasthour_new)

    res = nowtime - lasthour_new > timedelta(minutes=1)
    res1 = nowtime - lasthour_new
    print(res1.days)
    print(res)
    print(timedelta(hours=1))
