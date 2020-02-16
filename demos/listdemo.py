import json
import math
import numpy as np
from datetime import datetime, timedelta
from itertools import compress
from itertools import groupby
from operator import itemgetter
if __name__ == "__main__":
    # print(json.loads({"instidlist":"\['123','567'\]"}))
    str_lst = list("0101003")
    print(str_lst)
    print("============list operations ============")
    print('法大' in '陈环（旅发委执法大队副队长）|陈雪')
    l1 = ['法大','电大']
    l2 = ['陈环（旅发委执法大队副队长）', '陈雪']
    print('法大' in '.'.join(l2))
    print(set(l2).issubset(set(l1)))

    #自定义分组
    a = 2
    lstt = [2, 8, 11, 25, 43, 6, 9, -1, 29, 51, 66, 62, -2, -10]
    dmp = json.dumps(lstt)
    print(type(dmp))
    print(dmp)
    lds = json.loads(dmp)
    print(type(lds))
    print(lds)

    print(lstt[:10])
    print(max(lstt))
    del lstt[0]
    lstt.remove(-10)
    first, *mid, last = lstt
    print('first is {}, middle is {},last is {}'.format(first, mid, last))
    _, *lasts = lstt
    print('lasts is {}'.format(lasts))
    print("============group by *** ============")
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
    print(sorted(lstt, reverse=True))
    print('customer group', [(k, list(g)) for k, g in groupby(sorted(lstt), key=gb)])

    jsons = [{"callintimes": 2, "callmonth": "2015-11", "callouttimes": 0,
              "callphonenumber": "95533", "duration": 166, "maxcalltime": "2015-11-15T14:01:00",
              "mincalltime": "2015-11-15T10:28:00", "phonenumber": "11715158282"},
             {"callintimes": 1, "callmonth": "2015-12", "callouttimes": 0,
              "callphonenumber": "95533", "duration": 40, "maxcalltime": "2015-12-14T10:02:00",
              "mincalltime": "2015-12-14T10:02:00", "phonenumber": "11715158282"},
             {"callintimes": 0, "callmonth": "2016-11", "callouttimes": 1,
              "callphonenumber": "95533", "duration": 101, "maxcalltime": "2016-11-16T11:37:14",
              "mincalltime": "2016-11-16T11:37:14", "phonenumber": "11715158282"},
             {"callintimes": 1, "callmonth": "2016-12", "callouttimes": 0,
              "callphonenumber": "95533", "duration": 81, "maxcalltime": "2016-12-13T10:59:35",
              "mincalltime": "2016-12-13T10:59:35", "phonenumber": "11715158282"},
             {"callintimes": 2, "callmonth": "2017-01-02", "callouttimes": 1,
              "callphonenumber": "95533", "duration": 397, "maxcalltime": "2017-01-21T14:15:42",
              "mincalltime": "2017-01-11T11:31:28", "phonenumber": "11715158282"}
             ]
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

    # jsons['mincall'] = map(lambda x: x['mincalltime'].replace('T',' '), jsons)
    ttt = map(lambda x: x['mincalltime'].replace('T', ' '), jsons)
    for x in ttt:
        print(x)

    print('list_t---')
    def removeT(x):
        x['mincalltime'] = x['mincalltime'][0:10]
        return x
    list_t = [removeT(x) for x in jsons]
    print(list_t)
    
    # print(map(lambda x: x['mincalltime'].replace('T',' '), jsons))
    # jsons['maxcall'] = jsons.map(lambda x: x['maxcalltime'].sub)
    call2 = groupby(ljson, itemgetter('callmonth'))
    # sss = [{key: len(list(group))} for key, group in call2]
    # print(sss)

    jg_1 = [{key: list(group)} for key, group in lstg]
    print('----jg1')
    print(jg_1)
    print('----')

    lstg2 = groupby(jsons, itemgetter('callmonth'))
    jg_2 = dict([(key, len(list(group))) for key, group in lstg2])
    # jg_2 = [{key: len(list(group))} for key, group in lstg2]
    print('----jg2')
    print(jg_2)
    jg = {key: value for key, value in jg_2.items() if value > 2}
    print('the_dict filter result:', len(jg.keys()))
    print('----')
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

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = np.array(a)
    print(np.median(b))
    print(np.percentile(b, 25))
    print(np.percentile(b, 50))
    print(np.percentile(b, 75))
    print('*'*5)
    a.pop(a.index(2))  # remove 3
    print(a)
    print(list(filter(lambda x: x % 2, a)))
    print('*' * 10)
    a.remove(9)
    print(a)

    jArr = [{
                "final_score": 1041,
                "inserttime": 1515666222778,
                "final_decision": "Reject1",
                "updatetime": "2018-06-06 20:23:48",
                "upserttime": "2018-06-06T20:23:48",
                "maxcalltime": "2015-11-15T14:01:00",
                "mincalltime": "2015-11-15T10:28:00",
                "userid": 50188157
            },
            {
                "final_score": 1042,
                "inserttime": 1515666222779,
                "final_decision": "Reject：",
                "updatetime": "2018-06-06 20:23:48",
                "upserttime": "2018-06-01T20:23:48",
                "maxcalltime": "2015-11-15T14:01:00",
                "mincalltime": "2015-11-15T10:28:00",
                "userid": 50188157
            },
            {
                "final_score": 1047,
                "inserttime": 1513082115530,
                "final_decision": "Review：",
                "updatetime": "2018-06-02 20:23:48",
                "upserttime": "2018-06-02T20:23:48",
                "maxcalltime": "2015-11-15T14:01:00",
                "mincalltime": "2015-11-15T10:28:00",
                "userid": 50188157
            }]
    for it in jArr:
        it['final_decision'] = it['final_decision'].replace("：","")
    print(f'jArr is {jArr}')
    print(f'max list:{max(jArr, key=lambda x: x.get("inserttime") or "")}')
    a = jArr[0]['final_decision'] if 'final_decision' in jArr[0].keys() else -1
    print(f'a is {a}')
    fa1 = [x for x in jArr if x['final_decision'] == 'Reject']
    print(fa1)
    fa2 = (x for x in jArr if x['final_decision'] == 'Reject')
    print(fa2)
    fa3 = [x['inserttime'] for x in jArr if datetime.strptime(x['updatetime'], '%Y-%m-%d %H:%M:%S') - datetime.strptime('2018-06-01', '%Y-%m-%d')>timedelta(hours=24)]
    print(fa3)
    #[datetime.strptime(x['upserttime'].replace('T',' '), '%Y-%m-%d %H:%M:%S') for x in jArr]
    fatime = [x['upserttime'].replace('T',' ') for x in jArr]
    print(min(fatime))
    print('------')
    print(fa1[0]['final_score'])

    # fa4_item = jArr.sort(key=lambda x: x['updatetime'])
    # print(fa4_item[0])
    print("============sort by key(s) ============")
    fa4 = sorted(jArr, key=lambda x: x['updatetime'], reverse=True)[0]
    print(fa4)
    fa5 = sorted(jArr, key=lambda x: str(x['updatetime'])+str(x['final_score']), reverse=True)
    print('fa5:--')
    print(fa5)
    print('fa5:--')
    print([x.pop('seqid', None) for x in jArr])
    print(jArr)
    fa3 = filter(lambda x: x['final_decision'] == 'Reject', jArr)
    print('fa3:--')
    print(fa3)

    print("============any ============")
    keywords = ['小baby', '大宝贝', '小红帽']
    strs = '他是你的小宝贝，你是他的小红帽'
    print(not any(x for x in keywords if x in strs))

    print(5 in [4,15,6])

    lst = [['账单提醒', '中国联通'], ['邮储银行'],['邮储银行'],['留言提醒', '中国移动\u3000和留言']]
    print(f"fst is {[x[0] for x in lst]}")
