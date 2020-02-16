import heapq
from itertools import groupby
from functools import reduce 
from operator import itemgetter
from collections import defaultdict, OrderedDict, ChainMap ,Iterable
#底层使用heap实现,仅实现了从小到大的顺序排列
if __name__ == "__main__":
    print("============different types============")
    print(len({ "apr": "35.5"}))
    dc = {None: 111, 'a': 0, 'c': {'c1': 3}}
    print(f"a in dc?{'a' in dc}")
    print(f"dc get aa key, result={dc.get('aa')}")
    print(1 if dc.get('cc',None) is not None else 2)
    dc['a']=3
    print(dc)
    print('b' in dc.keys())
    print(dc[None])
    print(dc['c']['c1'])
    print("============loop and filter============")
    the_dict = {'a': 1, 'b': 2, 'ae': 5, 'c': 4, 'd': 3}
    print('aa' in the_dict.keys())
    p1 = {key: value for key, value in the_dict.items() if value > 2}
    print('the_dict filter result:', p1)
    dict_names = {'a', 'ae', 'aa'}
    p2 = {key: value for key, value in the_dict.items() if key in dict_names}
    print('the_dict contains value:', p2)

    p3 = dict((key, value) for key, value in the_dict.items() if value > 3)
    print('dict(the_dict) filter result is:', p3)

    p4 = {key for key in the_dict.keys() if key in dict_names}
    print('the_dict contains value:', p4)
    # get the lagest item of the dict.
    heap = [(-value, key) for key, value in the_dict.items()]
    largest = heapq.nsmallest(2, heap)
    print("largest is ", largest)
    largest = [(key, -value) for value, key in largest]
    print('dict(largest) is ', dict(largest))
    print("============max min zip change position============")
    # 取最小的2个items
    heapsm = [(value, key) for key, value in the_dict.items()]
    print("heapsm：", heapsm)
    smallheap = heapq.nsmallest(2, heapsm)
    print("smallheap：", smallheap)
    # key,value调换
    smallheap = [(key, value) for value, key in smallheap]
    print("dict", dict(smallheap))
    # dict to list,then find what you want.
    print("first element of dict", list(dict(smallheap).items())[-1])
    # 取最大
    smallheap = max(heapsm)
    print("max(heapsm):", smallheap)
    # 或
    smallheap = max(zip(the_dict.values(), the_dict.keys()))
    print("max(zip(the_dict.values(), the_dict.keys())):", smallheap)
    # 取最小
    smallheap = min(heapsm)
    print("min(heapsm):", smallheap)
    # 或
    smallheap = min(zip(the_dict.values(), the_dict.keys()))
    print("min(zip(the_dict.values(), the_dict.keys())): ", smallheap)

    print("============zip two dicts ============")
    the_dic = {'a':12, 'bb':2, 'cc':2}
    d3 = {}
    d3.update(the_dict)
    d3.update(the_dic)
    p12 = {key: value for key, value in d3.items()}
    print(f'zip two dicts, p12 {p12}')
    zip_res = dict(the_dict, **the_dic)
    p11 = {key: value for key, value in zip_res.items()}
    # print('the_dict filter result:', p11)
    print(f'zip two dicts, p11 {p11}')
    print('===============merge 2 dicts===============')
    # merge 2 dicts
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    merged = dict(b)
    merged.update(a)
    print('merged result is ', merged)
    a['x']=11
    print('merged-changed result is ', merged)
    print('===============merge N dicts===============')
    x = {'a': 1, 'b': 2}
    y = {'b': 3, 'c': 4}
    v = {'a': 2, 'c': 5}
    w = {'d': 1, 'd': 2}
    z = {**x, **y, **v}
    print(z)
    print(w)
    print(f"merge x and y , result is {dict(x,**y)}")
    print(len(z.keys()))
    print(list(z.keys()))

    print("============sort by *** ============")
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1005}
    ]
    print(f"rows.len={len(rows)}")
    rows_by_fname1 = sorted(rows, key=lambda d: d["fname"])
    rows_by_fname2 = sorted(rows, key=itemgetter("fname"))
    print("rows_by_fname1:",rows_by_fname1)
    print("rows_by_fname2-itemgetter:", rows_by_fname2)
    rows_by_uid1 = sorted(rows, key=lambda d:d["uid"])
    rows_by_uid2 = sorted(rows, key=itemgetter("uid"))
    print("rows_by_uid1:",rows_by_uid1)
    print("rows_by_uid2-itemgetter:", rows_by_uid2)

    rows_by_lname_fname1 = sorted(rows, key=lambda d1: (d1["lname"], d1["fname"], d1["uid"]))
    rows_by_lname_fname2 = sorted(rows, key=itemgetter("lname", "fname", "uid"))
    print("rows_by_lname_fname1:",rows_by_lname_fname1)
    print("rows_by_lname_fname2:", rows_by_lname_fname2)

    rows_max = max(rows, key=lambda d: d["uid"])
    rows_min = min(rows, key=lambda d: d["uid"])
    print("rows_max:", rows_max)
    print("rows_min:", rows_min)
    print("rows_min_for:", min(s['uid'] for s in rows))

    rows_max_item = max(rows, key=itemgetter("uid"))
    rows_min_item = min(rows, key=itemgetter("uid"))
    print("rows_max_item:", rows_max)
    print("rows_min_item:", rows_min)


    print("============group by *** ============")
    rowgs = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    sortedrows1 = sorted(rowgs, key=itemgetter('date'))
    print("sortedrows is ", sortedrows1)

    # wrong used example
    # sortedrows = rowgs.sort(key=itemgetter('date'))
    # print("sortedrows is ", sortedrows)

    sortedgrprows = groupby(rowgs, key=itemgetter('date'))
    for date, items in sortedgrprows:
        print('---------err result:', date)
        for i in items:
            print(' ', i)
    # print("sortedgrprows is ", sortedgrprows)

    print('===============defaultdict===============')
    from collections import defaultdict
    rows_by_date = defaultdict(list)
    # print('rows_by_date is ', rows_by_date)
    for row in rowgs:
        rows_by_date[row['date']].append(row)
        # print('rows is ', row)
    for r in rows_by_date['07/04/2012']:
        print('r is ',r)


    print('===============dict sort and groupkey===============')
    d1={'name':'zhangsan', 'age': 20, 'country':'China'}
    d2={'name':'wangwu', 'age': 19, 'country':'USA'}
    d3={'name':'lisi', 'age': 22, 'country':'JP'}
    d4={'name':'zhaoliu', 'age': 22, 'country':'USA'}
    d5={'name':'pengqi', 'age': 22, 'country':'USA'}
    d6={'name':'lijiu', 'age': 22, 'country':'China'}
    lst=[d1, d2, d3, d4, d5, d6]

    #通过country进行分组：
    lst.sort(key=itemgetter('country')) #需要先排序，然后才能groupby。lst排序后自身被改变
    # lstg = groupby(lst, key=lambda x:x['country']) 等同于使用itemgetter()
    lstg = groupby(lst, itemgetter('country'))
    import copy
    lstgg = copy.deepcopy(lstg)
    for key, group in lstgg:
        print('---------', key)
        for g in group: #group是一个迭代器，包含了所有的分组列表
            print(key, g)
    print('list group :',  [(key, list(group)) for key, group in lstg])
    print('dict group :',  dict([(key, len(list(group))) for key, group in groupby(lst, lambda x: x['country'])]))
    print('dict groupkey count>=2 :',  [key for key, group in groupby(lst, itemgetter('country')) if len(list(group)) >= 2])

    print('===============ChainMap===============')
    from collections import ChainMap
    c = ChainMap(a,b)
    print('ChainMap(a,b) is %s,c[x] is %d,c[z] is %d,len(c) is %d,keys is %s' % (c, c['x'], c['z'], len(c), list(c.keys())))
    c['z'] = 40
    print('c is ', c)
    del c['z']
    print('c is ', c)
    c['w']=20
    print('a is ', a)

    v = ChainMap()
    v['x'] = 5
    v = v.new_child()
    v['x'] = 2
    print('v is ', v)
    v['x'] = 3
    v = v.parents
    print('v is %s, v[x] is %s' % (v, v['x']))

    print('===============dict and OrderedDict===============')
    d1 = dict([('a',1),('c',3),('b',2)])
    d = OrderedDict([('a',1),('b',2),('c',3)])
    print(d1)
    print(d)

    print('===============list(dict) aggregation===============')
    bank_list = [
        {'bank': 'CLARK', 'amount': '200', 'amountused': '2'},
        {'bank': '58TH', 'amount': '1000', 'amountused': '21'},
        {'bank': 'CLARK', 'amount': '2000', 'amountused': '22'},
        {'bank': 'RAVENSWOOD', 'amount': '2000', 'amountused': '22'},
        {'bank': '58TH', 'amount': '200', 'amountused': '2'},
    ]
    bank_list.sort(key=itemgetter('bank'))
    bank_gp = groupby(bank_list, key=itemgetter('bank'))

    # Iterable only loop once
    bgp = [(key,list(group)) for key,group in bank_gp]
    # print([(key,list(group)) for key,group in bank_gp])
    print(type(bgp))
    print(isinstance(bgp, Iterable))
    print('----')
    bk_list = dict(bgp)
    print(bk_list)
    for key in bk_list:
        print(bk_list[key])

    print('===============add default dict demo===============')
    var_config_lst = ['Lol', 'Lool', 'Look', 'loop', 'Loop']
    check_dict = defaultdict(list)
    for var_name in var_config_lst:
        check_dict[var_name.lower()].append(var_name)
    print(check_dict)

    duplicate_list = [l for l in check_dict.values() if len(l) > 1]
    if duplicate_list:
        for l in duplicate_list:
            print(f"variables {l} are duplicate!")
    
    print('===============dict.values to list===============')
    var_con_lst = {
        "a":{
            "aa":"aa.1",
            "aaa":"aaa.1"
        },
        "b":{
            "bb":"bb.1",
            "bbb":"bbb.1"
        }
    }
    var_co = {
        "c":{
            "cc":"cc.1",
            "ccc":"ccc.1"
        },
        "dd":{
            "dd":"dd.1",
            "ddd":"ddd.1"
        },
        "b":{
            "bb":"bb.1",
            "bbb":"bbb.1",
            "bbbb":"bbbb.1" #merge to var_con_lst.b
        }
    }
    print(var_con_lst.values())
    print(list(var_con_lst.values()))
    print(str(list(var_con_lst.values())))
    lst = list(var_con_lst.values()) + list(var_co.values())
    print(lst)
    print("-----flat and merge to dicts")
    print({**var_con_lst, **var_co})

    print('===============flatten given dict===============')
    ini_dict = [{'a':1}, {'b':2}, {'c':3}]
    print(f"use ChainMap: {ChainMap(*ini_dict) }")
    res = {k: v for d in ini_dict for k, v in d.items()}
    print(f"use lit: {res}")
    res = reduce(lambda d, src: d.update(src) or d, ini_dict, {})
    print(f"use reduce: {res}")

    res = {} 
    for d in ini_dict: 
        res.update(d) 
    print(f"use for: {str(res)}")

    #print('===============str to dict===============')
    