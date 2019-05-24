import re
import json
import os
import pandas as pd
import numpy as np
import scipy
from scipy import stats
from datetime import timedelta

def adder(ad1,ad2):
    return ad1+ad2

if __name__ == '__main__':
    print("============dict to df============")
    result = {
        "upa_score_interval_day": 1,
        "upa_trans_at_ttl_suc_in_is180d": 2,
        "upa_trans_at_ttl_suc_in_6monmax": 3,
    }
    print(pd.cut(np.array([0.2,1.4,2.5,6.2,9.7,2.1]),3,retbins=True))
    print(pd.cut(np.array([0.2, 1.4, 2.5, 6.2, 9.7, 2.1]), [1, 2, 3], retbins=True))
    # pd_fund_userinfo1 = pd.DataFrame.from_dict(result, orient='index')
    # pd_fund_userinfo1.reset_index(level=0, inplace=True)
    pd_fund_userinfo1 = pd.DataFrame(result, index=[0])
    print(pd_fund_userinfo1)

    strt = """
    [
        {
            "birthday": null,
            "ppduserid": 123,
            "gender": "1",
            "customer_number": null,
            "gjj_number": null,
            "begin_date": null,
            "id_card": "312425****11220418",
            "real_name": "luopengfei",
            "base_number": null,
            "corporation_name": null,
            "fund_balance": null,
            "last_pay_date": null,
            "userid": null,
            "monthly_customer_income": null,
            "pay_status": null,
            "subsidy_corporation_ratio": null,
            "balance": null,
            "home_address": null,
            "customer_ratio": null,
            "subsidy_balance": null,
            "monthly_total_income": null,
            "email": null,
            "subsidy_income": null,
            "monthly_corporation_income": null,
            "inserttime": 1519729222978,
            "mobile": null,
            "card_type": null,
            "corporation_number": null,
            "corporation_ratio": null,
            "subsidy_customer_ratio": null,
            "updatetime": 1520323523890
        },
        {
            "birthday": null,
            "ppduserid": 123,
            "gender": "1",
            "customer_number": null,
            "gjj_number": null,
            "begin_date": null,
            "id_card": "31242519921122041*",
            "real_name": "*小明",
            "base_number": null,
            "corporation_name": null,
            "fund_balance": null,
            "last_pay_date": null,
            "userid": null,
            "monthly_customer_income": null,
            "pay_status": null,
            "subsidy_corporation_ratio": null,
            "balance": null,
            "home_address": null,
            "customer_ratio": null,
            "subsidy_balance": null,
            "monthly_total_income": null,
            "email": null,
            "subsidy_income": null,
            "monthly_corporation_income": null,
            "inserttime": 1519729222978,
            "mobile": null,
            "card_type": null,
            "corporation_number": null,
            "corporation_ratio": null,
            "subsidy_customer_ratio": null,
            "updatetime": 1520323502216
        },
        {
            "birthday": null,
            "ppduserid": 123,
            "gender": "1",
            "customer_number": null,
            "gjj_number": null,
            "begin_date": null,
            "id_card": "32242519921122041*",
            "real_name": "luo****fei",
            "base_number": null,
            "corporation_name": null,
            "fund_balance": null,
            "last_pay_date": null,
            "userid": null,
            "monthly_customer_income": null,
            "pay_status": null,
            "subsidy_corporation_ratio": null,
            "balance": null,
            "home_address": null,
            "customer_ratio": null,
            "subsidy_balance": null,
            "monthly_total_income": null,
            "email": null,
            "subsidy_income": null,
            "monthly_corporation_income": null,
            "inserttime": 1519729222978,
            "mobile": null,
            "card_type": null,
            "corporation_number": null,
            "corporation_ratio": null,
            "subsidy_customer_ratio": null,
            "updatetime": 1520323532774
        },
        {
            "birthday": null,
            "ppduserid": 123,
            "gender": "1",
            "customer_number": null,
            "gjj_number": null,
            "begin_date": null,
            "id_card": "342425199211220418",
            "real_name": "luopengfe*",
            "base_number": null,
            "corporation_name": null,
            "fund_balance": null,
            "last_pay_date": null,
            "userid": null,
            "monthly_customer_income": null,
            "pay_status": null,
            "subsidy_corporation_ratio": null,
            "balance": null,
            "home_address": null,
            "customer_ratio": null,
            "subsidy_balance": null,
            "monthly_total_income": null,
            "email": null,
            "subsidy_income": null,
            "monthly_corporation_income": null,
            "inserttime": 1519729222978,
            "mobile": null,
            "card_type": null,
            "corporation_number": null,
            "corporation_ratio": null,
            "subsidy_customer_ratio": null,
            "updatetime": 1520322999109
        }
    ]
    """
    pd_fund_userinfo = pd.DataFrame(json.loads(strt))
    print("============filtered,sorted result============")
    df_sort = pd_fund_userinfo[["inserttime","updatetime","ppduserid","id_card"]].sort_values(by=["inserttime"], ascending=False)
    print(df_sort)
    print('===')
    df_fuserid = df_sort[(~df_sort['id_card'].str.contains('34|18'))]
    df_fuserid = df_fuserid[df_fuserid['id_card'].str.contains('32')]
    print(df_fuserid)
    print('===')
    df_sort1 = pd_fund_userinfo[["inserttime", "updatetime", "ppduserid", "id_card"]].sort_values(by="updatetime")#,ascending=1
    print(df_sort1)
    df_sort2 = pd_fund_userinfo[["inserttime","updatetime","ppduserid","id_card"]].sort_values(by=["inserttime",'updatetime'], ascending=[False,False])
    print(df_sort2)

    print("============crosstab============")
    dftb = pd_fund_userinfo[["real_name",'gender','id_card']]
    print(pd.crosstab(dftb.gender,dftb.real_name,margins=True))
    print(pd.crosstab([dftb.gender,dftb.id_card], dftb.real_name, margins=True))

    print("============get only one colum result============")
    print(pd_fund_userinfo["real_name"])
    print(pd_fund_userinfo[(pd_fund_userinfo["real_name"]=='luopengfei') &(pd_fund_userinfo["ppduserid"]==123)]["real_name"])

    print("============pandas unique result============")
    df_u = pd_fund_userinfo[["inserttime","real_name",'ppduserid']]
    df_u = df_u[df_u["real_name"].apply(lambda x: x[:3] == 'luo')]
    print(df_u['ppduserid'].unique())
    # import pdb;
    # pdb.set_trace()

    inp = [{'c1': 10, 'c2': 100}, {'c1': 11, 'c2': 110}, {'c1': 12, 'c2': 120}]
    df = pd.DataFrame(inp)
    print("============show all============")
    print(df)
    print("============loop 1============")
    for index, row in df.iterrows():
        print(row["c1"], row["c2"])

    # for row in df.itertuples(index=True, name='Pandas'):
    #     print(getattr(row, "c1"), getattr(row, "c2"))
    # for row in df.itertuples():
    #     print("c1:{},c2:{}".format(row['c1'], row['c2']))
    #print((row['c1']) for index, row in df.iteritems())

    strr = """
    [
            {
                "already_enforce_object_money": "ddddd",
                "closed_date": "已关闭",
                "enforce_object_money": "dddd",
                "closed_type": "关闭蕾西",
                "register_date": "2017-02-01",
                "case_state": "已申诉",
                "court": "500",
                "case_reason": "推迟",
                "userid": 24681567,
                "enforce_object": "dddd",
                "already_enforce_object": "ddddddd"
            },
            {
                "already_enforce_object_money": null,
                "closed_date": null,
                "enforce_object_money": null,
                "closed_type": null,
                "register_date": "2017-01-02",
                "case_state": null,
                "court": "100",
                "case_reason": null,
                "userid": 24681567,
                "enforce_object": null,
                "already_enforce_object": null
            }
        ]
    """


    dff = pd.DataFrame(json.loads(strr))
    print("============loop 2============")
    for row in dff[["userid", "register_date"]].itertuples(index=True, name='Pandas'):
        print("uid:{},regdate:{}".format(getattr(row, "userid"), getattr(row, "register_date")))

    print(dff)
    print("====")
    try:
        print(pd.to_datetime(dff[pd.notnull(dff["register_date"])]["register_date"]))
    except Exception as e:
        print(e)

    print("============group by,sort============")
    phoneinfo="""
    [
        {
            "callphonenumber": "02151865695",
            "calltime": 1449029556000,
            "calltypeid": 1,
            "creationdate": 1524473524000,
            "originalcalladdress": "上海",
            "phonenumber": "11715158282",
            "talktime": 6,
            "updatetime": 1524473524000,
            "userid": 9528
        },
        {
            "callphonenumber": "02151865695",
            "calltime": 1448963913000,
            "calltypeid": 0,
            "creationdate": 1524473524000,
            "originalcalladdress": "上海",
            "phonenumber": "11715158282",
            "talktime": 144,
            "updatetime": 1524473524000,
            "userid": 9528
        },
        {
            "callphonenumber": "18221927813",
            "calltime": 1449030375000,
            "calltypeid": 0,
            "creationdate": 1524473524000,
            "originalcalladdress": "上海",
            "phonenumber": "11715158282",
            "talktime": 122,
            "updatetime": 1524473524000,
            "userid": 9528
        },
        {
            "callphonenumber": "18221927813",
            "calltime": 1448930350000,
            "calltypeid": 0,
            "creationdate": 1524473524000,
            "originalcalladdress": "上海",
            "phonenumber": "11715158282",
            "userid": 9528
        },
        {
            "callphonenumber": "15921611089",
            "calltime": 1448969903000,
            "calltypeid": 1,
            "creationdate": 1524473524000,
            "originalcalladdress": "上海",
            "phonenumber": "11715158282",
            "talktime": 21,
            "updatetime": 1524473524000,
            "userid": 9528
        },
        {
            "callphonenumber": "02151865695",
            "calltime": 1448952632000,
            "calltypeid": 1,
            "creationdate": 1524473524000,
            "originalcalladdress": "上海",
            "phonenumber": "11715158282",
            "talktime": 8,
            "updatetime": 1524473524000,
            "userid": 9528
        },
        {
            "callphonenumber": "18221927813",
            "calltime": 1449037363000,
            "calltypeid": 0,
            "creationdate": 1524473524000,
            "originalcalladdress": "上海",
            "phonenumber": "11715158282",
            "talktime": 17,
            "updatetime": 1524473524000,
            "userid": 9528
        },
        {
            "callphonenumber": "02131658069",
            "calltime": 1449043926000,
            "calltypeid": 1,
            "creationdate": 1524473524000,
            "originalcalladdress": "上海",
            "phonenumber": "11715158282",
            "talktime": 80,
            "updatetime": 1524473524000,
            "userid": 9528
        },
        {
            "callphonenumber": "18221927813",
            "calltime": 1449048242000,
            "calltypeid": 0,
            "creationdate": 1524473524000,
            "originalcalladdress": "上海",
            "phonenumber": "11715158282",
            "talktime": 27,
            "updatetime": 1524473524000,
            "userid": 9528
        }
    ]
    """
    df_phoneinfo=pd.DataFrame(json.loads(phoneinfo))
    df_phoneinfo=df_phoneinfo[["callphonenumber","calltypeid","userid","talktime"]]
    print('----')
    print(df_phoneinfo)
    print('----groupby1')
    dfg_g1_phoneinfo = df_phoneinfo.groupby(['callphonenumber']).agg({'callphonenumber':['count'], 'talktime':['sum']})
    print(dfg_g1_phoneinfo)
    print('----groupby2')
    dfg_g2_phoneinfo = df_phoneinfo.groupby(df_phoneinfo['callphonenumber']).agg({'callphonenumber': ['count']})
    print(dfg_g2_phoneinfo)
    print('----groupby3')
    dfg_g3_phoneinfo = df_phoneinfo.groupby(['callphonenumber','calltypeid']).agg({'callphonenumber': ['count']})
    print(dfg_g3_phoneinfo)

    dfg_phoneinfo = df_phoneinfo.groupby(['callphonenumber']).size().reset_index(name='count').sort_values(['count'],ascending=False).head(2)
    print(dfg_phoneinfo)
    # import pdb;pdb.set_trace()
    print(dfg_phoneinfo[dfg_phoneinfo['callphonenumber'].apply(lambda x: '021' in str(x).lower())])
    print(dfg_phoneinfo.head(1).iloc[0]['callphonenumber'])

    print("============join 2 dataframes============")
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                       index = [0, 1, 2, 3])
    df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                        'D': ['D2', 'D3', 'D6', 'D7'],
                        'F': ['F2', 'F3', 'F6', 'F7']},
                       index = [2, 3, 6, 7])
    result_ax0 = pd.concat([df1, df4], axis=0, join='inner')
    print(result_ax0)
    result_ax1 = pd.concat([df1, df4], axis=1, join='inner')
    print(result_ax1)
    # result_ax2 = pd.concat([df1, df4])
    # print(result_ax2)
    print("============drop_duplicates of dataframe============")
    infos = """
    [{
        "Content":"Hello, Mr. Left！您【上海公积金】账户呵呵呵了？",
        "InsertTime":"2010-03-04T20:13:44.320",
        "MobileNumber":"13375205707",
        "UserId":9527
    },
    {
        "Content":"Hello, Mr. Left！您【东北蛤蟆屯公 积 金】哈哈哈了",
        "InsertTime":"2010-05-12T19:48:57.754",
        "MobileNumber":"12375205707",
        "UserId":9527
    },
    {
        "Content":"Hello, Mr. Right！您【东北蛤蟆公积金中心】哈哈了",
        "InsertTime":"2010-05-12T19:48:57.754",
        "MobileNumber":"95222",
        "UserId":9527
    },
    {
        "Content":"Hello, Mr. left！您【公积金咋地了",
        "InsertTime":"2010-05-12T19:48:57.754",
        "MobileNumber":"95222",
        "UserId":9527
    }
    ]
    """
    dff_dup = pd.DataFrame(json.loads(infos))
    dup = dff_dup.drop_duplicates(subset=['UserId', 'Content', 'InsertTime'], keep='first', inplace=False)
    print(dup)
    # http://pandas.pydata.org/pandas-docs/stable/reference/series.html
    r = (r"(【*公积金】|【*公 积 金】|【*公积金中心】)")
    dup = dup[dup['Content'].str.contains(r)]
    print(dup)
    print('---')
    dup = dup[dup['MobileNumber'].str[0:1:1] == '1']
    print(dup)

    print("============merge 2 dataframes============")
    appcontact ="""
    [
        {
            "InsertTime":"2017-04-13T19:00:23",
            "MobileNumber":"13375205707",
            "Name":"东大街",
            "UserID":346
        },
        {
            "InsertTime":"2017-04-13T19:00:23",
            "MobileNumber":"13245706663",
            "Name":"机关枪",
            "UserID":346
        },
        {
            "InsertTime":"2017-04-17T11:02:10",
            "MobileNumber":"13375205707",
            "Name":"东升科技",
            "UserID":346
        },
        {
            "InsertTime":"2017-04-13T19:00:23",
            "MobileNumber":"15370608777",
            "Name":"丰汇袁总",
            "UserID":346
        },
        {
            "InsertTime":"2017-04-13T19:00:23",
            "MobileNumber":"13813341527",
            "Name":"东升科技",
            "UserID":346
        },
        {
            "InsertTime":"2017-04-13T19:00:23",
            "MobileNumber":"15805239710",
            "Name":"万达江涛",
            "UserID":346
        }
    ]
    """
    usercontact ="""
        [
      {
        "phone": "15805239710",
        "realname": "万达江涛",
        "userid": 2307643
      },
      {
        "phone": "13813341527",
        "realname": "东升科技",
        "userid": 2307643
      },
      {
        "phone": "",
        "realname": "东大街",
        "userid": 2307643
      }
    ]
    """
    dff1 = pd.DataFrame(json.loads(appcontact))
    dff2 = pd.DataFrame(json.loads(usercontact))
    dff_strip = dff1[['MobileNumber','Name']].apply(lambda x: x.str.strip())
    print(dff_strip)
    print(dff1)
    print(dff2)
    print('-------drop duplicate rows')
    print(dff1.drop_duplicates(keep='last'))
    result_ax3 = dff1.merge(dff2, left_on='MobileNumber',right_on='phone', how='inner')[['realname','phone','MobileNumber']]
    result_ax4 = dff1.merge(dff2, left_on='Name', right_on='realname', how='inner')[['realname','phone','MobileNumber']]
    print('----result_ax3--count:',result_ax3.shape[0])
    print(result_ax3)
    print('----result_ax4--count:',result_ax4.shape[0])
    print(result_ax4[['realname']].drop_duplicates())
    print('----result_ax5')
    result_ax5 = pd.concat([result_ax3,result_ax4]).drop_duplicates()
    print(result_ax5)
    print(dff1['Name'].ix[1])

    print("============load json for dataframe============")
    # fileInfo = ''
    filepath = 'file/jsonfile.json'
    if os.path.exists(filepath):
        # with open(filepath, 'r', encoding="latin-1") as f:
        #     fileInfo = json.load(f)
        with open(filepath, 'r') as f:
            # print(f.read())
            fileInfo = json.load(f)
    if(len(fileInfo)>0):
        df_fileInfo = pd.DataFrame(fileInfo)
        print(df_fileInfo)
    else:
        print("load noting")

    print("============create dataframe from series============")
    data = np.array(['a','b','c','d','e','f'])
    s = pd.Series(data)
    print(s)
    print(s[0])
    print(s[:3])
    print(s[-4:])
    s = pd.Series(data, index=[1000, 1001, 1002, 1003, 1004, 1005])
    print(s)
    print('--'+s[1001])
    print('--' + s[[1000,1001]])
    data = {'a': 0., 'b': 1., 'c': 2.}
    s = pd.Series(data, index=['b', 'c', 'd', 'a'])
    print(s)
    s = pd.Series(7, index=[0, 1, 2, 3])
    print(s)

    print("============format dataframe columns============")
    d = {'Quarters': ['Quarter1', 'Quarter2', 'Quarter3', 'Quarter4'],
         'Revenue': [23400344.567, 54363744.678, 56789117.456, 4132454.987]}
    dfQuarters = pd.DataFrame(d)
    print(dfQuarters)

    pd.options.display.float_format = '{:,.2f}'.format #'{:.2f}'.format/'{:.2E}'.format
    print(dfQuarters)
    print(dfQuarters.tail(2))

    print("============describe of dataframe============")
    d = {'Name': pd.Series(['Alisa', 'Bobby', 'Cathrine', 'Madonna', 'Rocky', 'Sebastian', 'Jaqluine',
                            'Rahul', 'David', 'Andrew', 'Ajay', 'Teresa']),
         'Age': pd.Series([26, 27, 25, 24, 31, 27, 25, 33, 42, 32, 51, 47]),
         'Score': pd.Series([89, 87, 67, 55, 47, 72, 76, 79, 44, 92, 99, 69])}

    # Create a DataFrame
    df = pd.DataFrame(d)
    print(df.describe())
    print(df.describe(include='object'))
    print(df.describe(include='all'))
    # column mean of the dataframe
    print(df.mean(axis=0))
    # row mean of the dataframe
    print(df.mean(axis=1))
    # mean of the specific column
    print(df.loc[:,"Score"].mean())

    print("============median of dataframe============")
    print(df.median())
    print('---')
    print(df.median(axis=0))
    print('---')
    print(df.loc[:,'Score'].median())
    print("============mode of dataframe============")
    print(df.mode(axis=0))
    print(df.loc[:,'Score'].mode())
    print(df.mode())


    print("============median of dataframe============")

    # Create a DataFrame
    d = {
        'Name': ['Alisa', 'Bobby', 'Cathrine', 'Madonna', 'Rocky', 'Sebastian', 'Jaqluine',
                 'Rahul', 'David', 'Andrew', 'Ajay', 'Teresa'],
        'Score1': [62, 47, 55, 74, 31, 77, 85, 63, 42, 32, 71, 57],
        'Score2': [89, 87, 67, 55, 47, 72, 76, 79, 44, 92, 99, 69]}
    dc = {
        'nme': ['Andrew', 'Ajay', 'Teresa'],
        'score1': [32, 71, 57],
        'score2': [92, 99, 69]}
    df = pd.DataFrame(d)
    print(df)
    print(scipy.stats.hmean(df.iloc[:,1:3],axis=0))
    print(scipy.stats.hmean(df.loc[:,'Score1']))
    print(scipy.stats.gmean(df.iloc[:,1:3],axis=0))
    print(scipy.stats.gmean(df.loc[:,'Score1']))

    print(df.std())
    print(df.std(axis=0))
    print(df.std(axis=1))
    print(df.loc[:,'Score1'].std())

    print(df.var())
    print(df.var(axis=0))
    print(df.var(axis=1))
    print(df.loc[:, 'Score1'].var())

    print("============pipe/apply/applymap of dataframe============")
    print(df[['Score1','Score2']].pipe(adder,2))
    # row
    print(df[['Score1','Score2']].apply(np.mean,axis=1))
    # column
    print(df[['Score1', 'Score2']].apply(np.mean, axis=0))
    import math
    print(df[['Score1', 'Score2']].applymap(lambda x:math.sqrt(x)))

    print("============rename column of dataframe============")
    df.columns = ['Names', 'score1', 'score2']
    print(df)
    df.rename(columns={'Names':'name'},inplace=True)
    print(df)
    df.columns.values[0]='nme'
    print(df)

    # df.reindex([8, 11, 9, 2, 1, 0, 7, 5, 6, 4, 10, 3])
    # print(df)
    # columnsTitles = ['Score2', 'Score1', 'Score3']
    # df.reindex(columns=columnsTitles)
    print("============ contact/append 2 dataframes============")
    dfd = pd.DataFrame({
        'nme': ['Andrew', 'Ajay', 'Teresa'],
        'score1': [32, 71, 57],
        'score2': [92, 99, 69],
        'score3': [92, 99, 69]})
    dfc = pd.DataFrame(dc)
    print(dfc)
    print(pd.concat([df,dfc]))
    print(df.append(dfd))
    print("============ column bind in dataframe============")
    dfdd = pd.DataFrame({'score4': [92, 99, 69, 10]})
    print(pd.concat([dfc,dfdd],axis=1,ignore_index=True))
    print("============ assign new column to existing dataframe============")
    df['score4']=None
    col_name = df.columns.tolist()
    col_name.insert(1,'score')
    df.reindex(columns= col_name)
    # df.reindex(columns=list('score6'))
    pd.concat([df, pd.DataFrame(columns=list(['score5','score6']))])
    # pd.concat([df, pd.DataFrame(columns=list('DE'))])
    # print(df.assign(score4=[10,2,3]))
    df1 = pd.DataFrame({'A': range(1, 11), 'B': np.random.randn(10)})
    df1.assign(ln_A=lambda x: np.log(x.A))
    print(df1)

    print("============ find/drop duplicate rows in dataframe============")
    d = {
        'Name': ['Alisa', 'Bobby', 'jodha', 'jack', 'raghu', 'Cathrine',
                 'Alisa', 'Bobby', 'kumar', 'Alisa', 'Alex', 'Cathrine'],
        'Age': [26, 24, 23, 22, 23, 24, 26, 24, 22, 23, 24, 24],

        'Score': [85, 63, 55, 74, 31, 77, 85, 63, 42, 62, 89, 77]}

    df = pd.DataFrame(d, columns=['Name', 'Age', 'Score'])
    df['is_duplicate'] = df.duplicated()
    print(df)
    print(df.drop([1,2]))
    print(df[df.is_duplicate == True])

    print("============ drop columns in dataframe============")
    print(df.drop(df.index[:3]))
    print(df.drop('is_duplicate',axis=1))
    print(df.drop(df.columns[2],axis=1))
    del df['Age']
    print(df)

    print("============ max/min value in dataframe============")
    print(df.max())
    print(df['Score'].max())
    print(df['Score'].min())
    print("============ loc get index value of dataframe============")
    print(df.loc[df['Score'].idxmax()])
    print(df.loc[df['Score'].idxmin()])

    print("============ get the unique values in dataframe============")
    print(df.drop('is_duplicate',axis=1).drop_duplicates())
    print(df.drop('is_duplicate', axis=1).drop_duplicates(keep='last'))

    print("============ get list of column============")
    print(df.columns.values)
    print(list(df))

    print("============ get unique value of dataframe============")
    print(df.Name.unique())
    print(df.Score.unique())
    print("============ ix/iloc/loc of dataframe============")
    print(df.ix[:,'Score'])
    print(df.ix[2,1])
    # .loc[[Row_names], [column_names]]
    # .iloc[1:m, 1:n] 1 to m rows and 1 to n columns

    # top 2 rows
    print(df.iloc[:2])
    print(df.iloc[:2,])
    # 3rd to 5th rows
    print(df.iloc[2:5, ])
    # all rows except 3rd rows
    print(df.iloc[2:])

    #select first 2 columns
    print(df.iloc[:,:2])
    # select first 1st and 3th columns
    print(df.iloc[:,[0,2]])
    # select value by row label and column label using loc
    print(df.loc[[1,2,3,4,5],['Name','Score']])

    dfResult = [{
            "interestRate": "<0.12",
            "lastLendAmountRange": "0-2999",
            "inserttime": 1527737429398,
            "xttr1": "",
            "xttr3": "",
            "xttr2": "",
            "userid": 57723918,
            "resId": 156352089,
            "hasOverdue3m": 1,
            "lastLendTillDay": "<=30",
            "overdue": 1,
            "applyResult": 1,
            "updatetime": 1527737429398,
            "taskid": "536ae0f30eb94b5eadd10081be0e47ef"
        },{
            "interestRate": "<0.12",
            "lastLendAmountRange": "0-2999",
            "inserttime": 1527737429398,
            "xttr1": "",
            "xttr3": "",
            "xttr2": "",
            "userid": 57723918,
            "resId": 156352089,
            "hasOverdue3m": 1,
            "lastLendTillDay": "<=130",
            "overdue": 1,
            "applyResult": 1,
            "updatetime": 1527737429398,
            "taskid": "536ae0f30eb94b5eadd10081be0e47ef"
        }]
    pd_res = pd.DataFrame.from_dict(dfResult, orient='columns')
    print(pd_res.ix[:, 'lastLendTillDay'])

    print("============ long of dataframe============")
    d = {
        'countries': ['A', 'B', 'C'],
        'population_in_million': [100, 200, 120],
        'gdp_percapita': [2000, 7000, 15000]
    }
    df = pd.DataFrame(d, columns=['countries', 'population_in_million', 'gdp_percapita'])

    df2 = pd.melt(df, id_vars=['countries'], var_name='metrics', value_name='values')
    print(df2)
    print("============ pivot of dataframe============")
    d = {
        'countries': ['A', 'B', 'C', 'A', 'B', 'C'],
        'metrics': ['population_in_million', 'population_in_million', 'population_in_million',
                    'gdp_percapita', 'gdp_percapita', 'gdp_percapita'],
        'values': [100, 200, 120, 2000, 7000, 15000]
    }
    df = pd.DataFrame(d, columns=['countries', 'metrics', 'values'])
    print(df)
    df3 = df.pivot(index='countries', columns='metrics', values='values')
    print(df3)

    dd = {
        'Name': ['Alisa', 'Bobby', 'Cathrine', 'Alisa', 'Bobby', 'Cathrine',
                 'Alisa', 'Bobby', 'Cathrine', 'Alisa', 'Bobby', 'Cathrine'],
        'Exam': ['Semester 1', 'Semester 1', 'Semester 1', 'Semester 1', 'Semester 1', 'Semester 1',
                 'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2'],

        'Subject': ['Mathematics', 'Mathematics', 'Mathematics', 'Science', 'Science', 'Science',
                    'Mathematics', 'Mathematics', 'Mathematics', 'Science', 'Science', 'Science'],
        'Score': [62, 47, 55, 74, 31, 77, 85, 63, 42, 67, 89, 81]}

    ddf = pd.DataFrame(dd, columns=['Name', 'Exam', 'Subject', 'Score'])
    print(ddf)
    ddfpd = pd.pivot_table(ddf, index=['Exam', 'Subject'], aggfunc='mean')
    print(ddfpd)
    ddfpd = pd.pivot_table(ddf, index=['Name', 'Subject'], aggfunc='sum')
    print(ddfpd)
    ddfpd = pd.pivot_table(ddf, index=['Exam', 'Subject'], aggfunc='count')
    print(ddfpd)

    print("============ shift of dataframe============")
    shdf1 = df[['values']]
    print(shdf1)
    shdf2 = df[['values']].shift(1)
    print(shdf2)
    shdfres = shdf1 - shdf2
    print(shdfres)

    print("============ stack of dataframe============")
    header = pd.MultiIndex.from_product([['Semester1', 'Semester2'], ['Maths', 'Science']])
    d = ([[12, 45, 67, 56], [78, 89, 45, 67], [45, 67, 89, 90], [67, 44, 56, 55]])
    df = pd.DataFrame(d, index=['Alisa', 'Bobby', 'Cathrine', 'Jack'], columns=header)
    print(df)
    stacked_df = df.stack()
    print(stacked_df)
    unstacked_df = stacked_df.unstack()
    print(unstacked_df)
    stacked_df_lvl = df.stack(level=0)
    print(stacked_df_lvl)
    unstacked_df1 = stacked_df_lvl.unstack()
    print(unstacked_df1)

    print("============ agg of dataframe============")
    jsons = [{"callmonth": "2017-07", "callphonenumber": "95511", "maxcalltime": "2017-07-08T16:24:02",
              "mincalltime": "2017-07-03T20:07:39"},
             {"callmonth": "2017-03", "callphonenumber": "95522", "maxcalltime": "2017-03-14T18:20:10",
              "mincalltime": "2017-03-14T18:20:10"},
             {"callmonth": "2016-12", "callphonenumber": "95521", "maxcalltime": "2016-12-14T11:25:49",
              "mincalltime": "2016-12-14T11:25:49"},
             {"callmonth": "2015-11", "callphonenumber": "95528", "maxcalltime": "2015-11-05T16:32:00",
              "mincalltime": "2015-11-04T12:14:00"},
             {"callmonth": "2015-11", "callphonenumber": "95532", "maxcalltime": "2015-11-15T14:01:00",
              "mincalltime": "2015-11-15T10:28:00"},
             {"callmonth": "2015-12", "callphonenumber": "95533", "maxcalltime": "2015-12-14T10:02:00",
              "mincalltime": "2015-12-14T10:02:00"},
             {"callmonth": "2016-11", "callphonenumber": "95533", "maxcalltime": "2016-11-16T11:37:14",
              "mincalltime": "2016-11-16T11:37:14"},
             {"callmonth": "2016-12", "callphonenumber": "95533", "maxcalltime": "2016-12-13T10:59:35",
              "mincalltime": "2016-12-13T10:59:35"}]
    pd_jsons = pd.DataFrame.from_dict(jsons, orient='columns')
    print(pd_jsons)
    print("------")
    df_mobile_group = pd_jsons.groupby(['callphonenumber']).agg([max, min])[
        ['maxcalltime', 'mincalltime']].reset_index()
    print(df_mobile_group)

    print("============ contains of dataframe============")
    s1 = pd.Series(['Mouse', 'dog', 'house and parrot', '23', np.NaN])
    print(s1.str.contains('house|dog'))
    print(s1)

    print("============ loc============")
    df = pd.DataFrame([[1, 2], [4, 5], [7, 8]], index=['cobra', 'viper', 'sidewinder'], columns=['max_speed', 'shield'])
    print(df)
    df.loc[df['max_speed'] == 4, 'pp'] = 'home_1'
    print(df)
    df.columns
    # df.loc[df['max_speed'] == 4, 'pp'] = 'home_1'
    # print(df)

    print("============ readcsv to pd============")
    # mobileDev_2.csv
    # userid, boAppNum, cellphoneConn, dellphoneIMEIConn, ignoreColumn
    # 31924036, aa0, bb0, cc0, dd
    df = pd.read_csv('/data/code/mobileDev_2.csv', header=None, names=["userid","boAppNum","cellphoneConn","dellphoneIMEIConn"])
    print(df['dellphoneIMEIConn'])

    print("============ df_result operations============")
    json_dict_list = """
        [
        {"userId":9527,"subject":"发出催款通知，逾期","body":"本人75","creationDate":"2018-09-15 10:15:01","dunStatusTypeId":0,"causeType":0,"repayDate":null,"contactStatus":0,"callNumber":null},
        {"userId":9527,"subject":"发出催款通知，逾期","body":"未接通","creationDate":"2018-09-15 10:15:10","dunStatusTypeId":0,"causeType":0,"repayDate":"2018-09-15 10:15:10","contactStatus":8,"callNumber":"152****6975"},
        {"userId":9527,"subject":"发出催款通知，逾期","body":"联系人","creationDate":"2018-09-15 10:15:15","dunStatusTypeId":0,"causeType":0,"repayDate":"","contactStatus":0,"callNumber":"null"}]
        """
    dun_records = json.loads(json_dict_list)
    df_result = pd.DataFrame(columns=['userid', 'creationdate', 'dunstatustypeid'])
    df_temp_list = []

    if dun_records:
        df_temp = pd.DataFrame(data=dun_records)
        df_temp.columns = df_temp.columns.str.strip().str.lower()
        df_temp['creationdate'] = pd.to_datetime(df_temp['creationdate'])
        print('all len:'+str(df_temp.shape[0]))
        df_temp = df_temp[~pd.isnull(df_temp['callnumber'])]
        print(df_temp)
        print('all len without callnumber is null:' + str(df_temp.shape[0]))
        df_temp = df_temp[df_temp["repaydate"].str.len() > 0]
        df_temp = df_temp[['userid', 'creationdate', 'dunstatustypeid']]
        df_temp_list.append(df_temp)
    if len(df_temp_list):
        df_result_temp = pd.concat(df_temp_list)
        df_result = df_result_temp.drop_duplicates().reset_index(drop=True)
    print(df_result)
    aadf = df_result[df_result['dunstatustypeid'] > 0].max()
    print(aadf['dunstatustypeid'])
    print(aadf.shape[0])

    df_records = df_result
    date_list = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]
    print(date_list[2])
    return_list = []
    bad_set = {20, 22, 23, 24, 26, 29, 33, 39}
    listingtime = pd.to_datetime('2018-09-15 10:15:01')
    for k in range(len(date_list)):
        look_time = listingtime - timedelta(days=date_list[k])
        df_record_per_userid = df_records[
            (df_records['creationdate'] < listingtime) & (df_records['creationdate'] >= look_time) & (
            df_records['dunstatustypeid'].isin(bad_set))]
        if len(df_record_per_userid):
            df_record_per_userid = df_record_per_userid.drop_duplicates(['userid', 'creationdate'])
            return_list.append(len(df_record_per_userid))
        else:
            return_list.append(0)
    print(return_list)