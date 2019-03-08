import math
from datetime import datetime, timedelta
from itertools import compress
from itertools import groupby
from operator import itemgetter
if __name__ == "__main__":
    print("============group by *** ============")
    #自定义分组
    a = 2
    lstt=[2, 8, 11, 25, 43, 6, 9, -1, 29, 51, 66, 62, -2, -10]

    first, *mid, last = lstt
    print('first is {}, middle is {},last is {}'.format(first, mid, last))
    _, *lasts = lstt
    print('lasts is {}'.format(lasts))
    var_unionpay = ['mon_12_var1',
                    'tfr_in_accts_cnt_is180d',
                    'trans_at_ttl_suc_out_6monmax',
                    'recentintervald_trans',
                    'is_taoxian_mct_freq_6m',
                    'in_avg',
                    'withdraw_amt_ratio',
                    'out_0_6_ratio',
                    'out_max_ratio',
                    ]
    var_unionpay_bins = {'mon_12_var1': [-float('inf'), 3, 6, 11, float('inf')],
                         'tfr_in_accts_cnt_is180d': [-float('inf'), 1, float('inf')],
                         'trans_at_ttl_suc_out_6monmax': [-float('inf'), 359.79, 2290.198, float('inf')],
                         'recentintervald_trans': [-float('inf'), 12, 15.5, 32, float('inf')],
                         'is_taoxian_mct_freq_6m': [-float('inf'), 5.5, float('inf')],
                         'in_avg': [-float('inf'), 1.5499845, 1691.882989, 2981.479322, float('inf')],
                         'withdraw_amt_ratio': [-float('inf'), 0.365306046, float('inf')],
                         'out_0_6_ratio': [-float('inf'), 0.025300051, 0.133928407, float('inf')],
                         'out_max_ratio': [-float('inf'), 0.349669115, 0.814364906, float('inf')]
                         }
    for i in var_unionpay:
        i_bins = var_unionpay_bins.get(i)
        print(i_bins)


    aa = [x for x in lstt if a == x]
    print(aa)
    def gb(num):
        if num <= 10:
            return 'less'
        elif num >= 30:
            return 'great'
        else:
            return 'middle'

    print(sorted(lstt))
    print(sorted(lstt, reverse=False))
    print(sorted(lstt,reverse=True))
    print('customer group', [(k, list(g)) for k, g in groupby(sorted(lstt), key=gb)])

    jsons = [{"callintimes": 0, "callmonth": "2017-07", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 2,
              "callphonenumber": "95511", "cityname": "西安", "duration": 354, "maxcalltime": "2017-07-08T16:24:02",
              "mincalltime": "2017-07-03T20:07:39", "phonenumber": "15339165005"},
             {"callintimes": 1, "callmonth": "2017-03", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 0,
              "callphonenumber": "95522", "cityname": "西安", "duration": 84, "maxcalltime": "2017-03-14T18:20:10",
              "mincalltime": "2017-03-14T18:20:10", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2016-12", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 1,
              "callphonenumber": "95527", "cityname": "西安", "duration": 163, "maxcalltime": "2016-12-14T11:25:49",
              "mincalltime": "2016-12-14T11:25:49", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2015-11", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 2,
              "callphonenumber": "95528", "cityname": "西安", "duration": 164, "maxcalltime": "2015-11-05T16:32:00",
              "mincalltime": "2015-11-04T12:14:00", "phonenumber": "15339165005"},
             {"callintimes": 2, "callmonth": "2015-11", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 0,
              "callphonenumber": "95533", "cityname": "西安", "duration": 166, "maxcalltime": "2015-11-15T14:01:00",
              "mincalltime": "2015-11-15T10:28:00", "phonenumber": "15339165005"},
             {"callintimes": 1, "callmonth": "2015-12", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 0,
              "callphonenumber": "95533", "cityname": "西安", "duration": 40, "maxcalltime": "2015-12-14T10:02:00",
              "mincalltime": "2015-12-14T10:02:00", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2016-11", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 1,
              "callphonenumber": "95533", "cityname": "西安", "duration": 101, "maxcalltime": "2016-11-16T11:37:14",
              "mincalltime": "2016-11-16T11:37:14", "phonenumber": "15339165005"},
             {"callintimes": 1, "callmonth": "2016-12", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 0,
              "callphonenumber": "95533", "cityname": "西安", "duration": 81, "maxcalltime": "2016-12-13T10:59:35",
              "mincalltime": "2016-12-13T10:59:35", "phonenumber": "15339165005"},
             {"callintimes": 2, "callmonth": "2017-01", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 1,
              "callphonenumber": "95533", "cityname": "西安", "duration": 397, "maxcalltime": "2017-01-21T14:15:42",
              "mincalltime": "2017-01-11T11:31:28", "phonenumber": "15339165005"},
             {"callintimes": 2, "callmonth": "2017-03", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 1,
              "callphonenumber": "95533", "cityname": "西安", "duration": 323, "maxcalltime": "2017-03-11T16:50:48",
              "mincalltime": "2017-03-02T15:26:49", "phonenumber": "15339165005"},
             {"callintimes": 1, "callmonth": "2017-04", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 0,
              "callphonenumber": "95533", "cityname": "西安", "duration": 117, "maxcalltime": "2017-04-12T09:41:48",
              "mincalltime": "2017-04-12T09:41:48", "phonenumber": "15339165005"},
             {"callintimes": 2, "callmonth": "2017-07", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 3,
              "callphonenumber": "95533", "cityname": "西安", "duration": 435, "maxcalltime": "2017-07-12T11:41:40",
              "mincalltime": "2017-07-10T10:32:39", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2016-12", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 1,
              "callphonenumber": "95561", "cityname": "西安", "duration": 7, "maxcalltime": "2016-12-31T15:23:56",
              "mincalltime": "2016-12-31T15:23:56", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2015-10", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 1,
              "callphonenumber": "95588", "cityname": "西安", "duration": 123, "maxcalltime": "2015-10-25T13:12:00",
              "mincalltime": "2015-10-25T13:12:00", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2016-12", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 1,
              "callphonenumber": "95588", "cityname": "西安", "duration": 273, "maxcalltime": "2016-12-02T14:01:04",
              "mincalltime": "2016-12-02T14:01:04", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2017-03", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 7,
              "callphonenumber": "95588", "cityname": "西安", "duration": 933, "maxcalltime": "2017-03-19T09:50:56",
              "mincalltime": "2017-03-03T21:15:32", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2017-04", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 5,
              "callphonenumber": "95588", "cityname": "西安", "duration": 704, "maxcalltime": "2017-04-20T15:42:14",
              "mincalltime": "2017-04-06T20:35:00", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2017-05", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 1,
              "callphonenumber": "95588", "cityname": "西安", "duration": 142, "maxcalltime": "2017-05-07T08:45:24",
              "mincalltime": "2017-05-07T08:45:24", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2017-06", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 3,
              "callphonenumber": "95588", "cityname": "西安", "duration": 679, "maxcalltime": "2017-06-06T19:39:43",
              "mincalltime": "2017-06-04T17:24:45", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2017-07", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 3,
              "callphonenumber": "95588", "cityname": "西安", "duration": 881, "maxcalltime": "2017-07-14T18:23:46",
              "mincalltime": "2017-07-08T16:49:49", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2015-10", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 2,
              "callphonenumber": "95595", "cityname": "西安", "duration": 273, "maxcalltime": "2015-10-25T18:00:00",
              "mincalltime": "2015-10-25T17:57:00", "phonenumber": "15339165005"},
             {"callintimes": 1, "callmonth": "2016-12", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 0,
              "callphonenumber": "95595", "cityname": "西安", "duration": 19, "maxcalltime": "2016-12-04T11:13:29",
              "mincalltime": "2016-12-04T11:13:29", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2017-03", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 1,
              "callphonenumber": "95595", "cityname": "西安", "duration": 168, "maxcalltime": "2017-03-12T09:42:16",
              "mincalltime": "2017-03-12T09:42:16", "phonenumber": "15339165005"},
             {"callintimes": 4, "callmonth": "2017-05", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 0,
              "callphonenumber": "95595", "cityname": "西安", "duration": 225, "maxcalltime": "2017-05-24T14:35:27",
              "mincalltime": "2017-05-17T09:19:27", "phonenumber": "15339165005"},
             {"callintimes": 2, "callmonth": "2017-06", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 0,
              "callphonenumber": "95595", "cityname": "西安", "duration": 91, "maxcalltime": "2017-06-02T17:31:41",
              "mincalltime": "2017-06-01T15:28:41", "phonenumber": "15339165005"},
             {"callintimes": 4, "callmonth": "2017-07", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 0,
              "callphonenumber": "95595", "cityname": "西安", "duration": 464, "maxcalltime": "2017-07-17T12:49:14",
              "mincalltime": "2017-07-17T10:13:58", "phonenumber": "15339165005"},
             {"callintimes": 0, "callmonth": "2017-08", "calloutlimit5s": 0, "callouttime0_6": 0, "callouttimes": 1,
              "callphonenumber": "95595", "cityname": "西安", "duration": 150, "maxcalltime": "2017-08-06T22:53:39",
              "mincalltime": "2017-08-06T22:53:39", "phonenumber": "15339165005"}]

    *_, ljson = jsons
    print('last duration is :{}'.format(ljson['duration']))
    jsons.sort(key=itemgetter('callphonenumber'))
    lstg = groupby(jsons, itemgetter('callphonenumber'))

    # (fres1,fres2) = [(x['callintimes'],x['callouttime0_6']) for x in lstg]
    # print(fres1,fres2)
    ss = [x['callintimes'] for x in jsons]
    sum_list = sum([x['callintimes'] for x in jsons])
    print(sum(ss))
    print('sum_list---')
    print(sum_list)

    jg_1 = [{key:list(group)} for key,group in lstg]
    # print(jg_1)
    # {key for key in the_dict.keys() if key in dict_names}

    # for key, group in jg_1:
    #     for g in group:  # group是一个迭代器，包含了所有的分组列表
    #         print(key, g)

    for x in jg_1:
        # for g in group:
        key = list(x.keys())[0]
        vals = list(x.values())[0]
        # print(key,vals)
        maxcalltime = max([y['maxcalltime'].replace('T',' ') for y in vals])
        mincalltime = min([y['mincalltime'].replace('T',' ') for y in vals])
        print(f'key:{key},max:{maxcalltime},min:{mincalltime}')
        # maxcalltime = x.values()
        # x.keys()

    jg_2 = dict([(key, list(group)) for key, group in lstg])
    print(jg_2)


    print("============aggregation before filter items============")
    print('sum(n<0) ', sum(x for x in lstt if x < 0))

    print("============for ============")
    print("math.sqrt for is :", [math.sqrt(n) for n in lstt if n > 10])
    print("n for is :", [n if n < 0 else 0 for n in lstt])
    print("n for_ifif is :", [n if n < 0 else 0 for n in lstt if n < -1])
    print("n for_if is :", [n > 0 for n in lstt if n < 0])

    address = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'g1']
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    more = [n > 5 for n in counts]
    print("more is :{},first is {}".format(more, counts[0]))
    print("compress is :", list(compress(address, more)))

    print("============sort by len ============")
    List2 = ['alex', 'zampa', 'micheal', 'jack', 'milton']
    List2.sort(reverse=True, key=len)
    print(List2)

    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(list(filter(lambda x: x % 2, a)))

    jArr = [
            {
                "final_score": 1047,
                "risk_type": "suspiciousLoan_reject",
                "policy_set_name": "借款事件_网站",
                "inserttime": 1515666222778,
                "final_decision": "Reject",
                "policy_name": "借款事件_网站",
                "seq_id": "1486360132843686F0B5679C93618668",
                "updatetime": "2018-06-06 20:23:48",
                "upserttime": "2018-06-06T20:23:48",
                "maxcalltime": "2015-11-15T14:01:00",
                "mincalltime": "2015-11-15T10:28:00",
                "userid": 50188157,
                "seqid": 1,
                "taskid": None
            },
            {
                "final_score": 1047,
                "risk_type": "suspiciousLoan_reject",
                "policy_set_name": "借款事件_网站",
                "inserttime": 1513082115530,
                "final_decision": "Review",
                "policy_name": "借款事件_网站",
                "seq_id": "1486360132843686F0B5679C93618668",
                "updatetime": "2018-06-01 20:23:48",
                "upserttime": "2018-06-01T20:23:48",
                "maxcalltime": "2015-11-15T14:01:00",
                "mincalltime": "2015-11-15T10:28:00",
                "userid": 50188157,
                "seqid": 1,
                "taskid": None
            },
            {
                "final_score": 1047,
                "risk_type": "suspiciousLoan_reject",
                "policy_set_name": "借款事件_网站",
                "inserttime": 1513082115530,
                "final_decision": "Review",
                "policy_name": "借款事件_网站",
                "seq_id": "1486360132843686F0B5679C93618668",
                "updatetime": "2018-06-02 20:23:48",
                "upserttime": "2018-06-02T20:23:48",
                "maxcalltime": "2015-11-15T14:01:00",
                "mincalltime": "2015-11-15T10:28:00",
                "userid": 50188157,
                "seqid": 1,
                "taskid": None
            }
        ]
    a = jArr[0]['final_decision'] if 'final_decision' in jArr[0].keys() else -1
    print(f'a is {a}')
    fa1 = [x for x in jArr if x['final_decision']=='Reject']
    print(fa1)
    fa2 = (x for x in jArr if x['final_decision']=='Reject')
    print(fa2)
    fa3 = [x['inserttime'] for x in jArr if datetime.strptime(x['updatetime'], '%Y-%m-%d %H:%M:%S') - datetime.strptime('2018-06-01', '%Y-%m-%d')>timedelta(hours=24)]
    print(fa3)
    #[datetime.strptime(x['upserttime'].replace('T',' '), '%Y-%m-%d %H:%M:%S') for x in jArr]
    fatime = [x['upserttime'].replace('T',' ') for x in jArr]
    print(min(fatime))
    print('------')
    print(fa1[0]['final_score'])

    # fa4 = jArr.sort(key=lambda x:x['updatetime'])
    fa4 = sorted(jArr, key=lambda x: x['updatetime'], reverse=True)
    print(fa4)
    print([x.pop('seqid',None) for x in jArr])
    print(jArr)
    fa3 = filter(lambda x: x['final_decision'] == 'Reject', jArr)
    print('fa3:--')
    print(fa3)

    print("============any ============")
    keywords = ['小baby', '大宝贝', '小红帽']
    strs = '他是你的小宝贝，你是他的小红帽'
    print(not any(x for x in keywords if x in strs))

    print( 5 in [4,15,6])