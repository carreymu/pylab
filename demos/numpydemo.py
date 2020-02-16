import random
from copy import deepcopy
import time
import string
import pandas as pd
import numpy as np
import math

if __name__ == '__main__':
    # print(np.pi)

    time1 = time.time()

    def ops(a_latitude, b_latitude, a_longitude, b_longitude):
        # res = np.round(
        #     6378.138 * 2 * math.asin
        #     (np.sqrt
        #      (
        #         np.power(np.sin((a_latitude * np.pi / 180 - b_latitude * np.pi / 180) / 2), 2)
        #       + np.cos(a_latitude * np.pi / 180) * np.cos(b_latitude * np.pi / 180) * np.power(np.sin((a_longitude * np.pi / 180 - b_longitude * np.pi / 180) / 2), 2))) * 1000)
        ress = 6378.138 * 2 * np.arcsin(np.sqrt(np.power(np.sin((a_latitude * np.pi / 180 - b_latitude * np.pi / 180) / 2), 2) + np.cos(a_latitude * np.pi / 180) * np.cos(b_latitude * np.pi / 180) * np.power(np.sin((a_longitude * np.pi / 180 - b_longitude * np.pi / 180) / 2), 2)))*1000
        # print(ress)
        return np.round(ress)

    uc = [['中国地质大学（北京）', 116.35, 39.99], ['北京经济技术职业学院', 116.47, 39.98], ['北京经济管理职业学院', 116.47, 39.98]] *900
    # print(uc)
    data = pd.DataFrame(uc, columns=['school_name', 'longitude', 'latitude'])
    time1 = time.time()
    # print(data)
    uc1 = [[1520323523890, 116.35, 39.99], [1520323523891, 116.47, 39.98]] * 100
    data1 = pd.DataFrame(uc1, columns=['inserttime', 'Longitude', 'Latitude'])
    # print(data1)
    data['tmp'] =1
    data1['tmp'] = 1
    df = pd.merge(data, data1, on=['tmp'])
    df = df.drop('tmp', axis=1)
    ops_res = ops(df['Latitude'].values, df['latitude'].values, df['longitude'].values, df['Longitude'].values)
    print('*'*20)
    print(ops_res)
    df['dis'] = ops_res
    print('df time span:{}'.format(time.time() - time1))
    print(df)


    a = np.array([1.1, 2, 3, 4, 5, 6])
    print(type(a))
    b = np.array([1, 4, 5, 2, 3, 4])
    print(a / 2)
    print(a * b)

    print(math.pi*a - math.pi*b)
    print(math.pi * a - math.pi * b)
    # print(a > b)
    c = np.in1d(a, b)
    # print(c)

    print(np.array([1, 1, 1]) > np.array([0, 2, 3]))

    A = np.random.random([300, 12])
    B = np.random.random([12, 256])


    print("============ df vector number operations============")

    a = pd.DataFrame([(random.randint(0, 100), random.randint(0, 100)) for _ in range(1000)], columns=['a', 'b'])
    # print('a1*'*10)
    # print(a)

    # print('c1*' * 10)
    '''python的list循环遍历'''
    a['c'] = -1
    time1 = time.time()
    for row in range(0, len(a)):
        a['c'].iloc[row] = a['a'].iloc[row] if a['a'].iloc[row] > a['b'].iloc[row] else a['b'].iloc[row]
    print('just loop time span:{}'.format(time.time() - time1))
    # print(a)


    # print('a2*' * 10)
    '''iterrows()为每一行返回一个Series，它以索引对的形式遍历DataFrame，以Series的形式遍历感兴趣的列.
    DataFrame.iterrows() 的作用是将 dataframe的每行转换成为一个 Series，可以理解为 针对于每一行，做了行列转置.
    python的for循环耗时占了大头.
    '''
    time2 = time.time()
    sec = a.iterrows()
    # print(time.time() - time2)
    for index, row in sec:
        row['c'] = row['a'] if row['a'] > row['b'] else row['b']
    # print(a)
    print('iterrows time span:{}'.format(time.time() - time2))


    '''apply遍历列.apply本质上是一个函数.语法fun.apply(thisArg, [argsArray]),简单可用匿名函数实现.'''

    '''具体实现可参考下面:
    Function.prototype.myApply = function(context, arr) {
        var context = context || global;
        context.fn = this;
        var result;
        if (!arr) {
            result = context.fn(); //直接执行
        } else {
            var args = [];
            for (var i=0,len=arr.length;i<len;i++) {
                args.push("arr[" + i + "]");
            }
            result = eval("context.fn([" + args.toString() + "])");
        }
        //将this指向销毁
        delete context.fn;
        return result;
    }
    '''
    time3 = time.time()
    a['c'] = a.apply(lambda x: x['a'] if x['a'] > x['b'] else x['b'], axis=1)
    print('apply time span:{}'.format(time.time() - time3))
    # print(a)

    '''
    使用loc进行标签索引行数据，在索引中做判断
    '''
    # print('a3*' * 10)
    # print('iterrows time span:')
    c = deepcopy(a)
    time4 = time.time()
    c['c'] = c['b']
    c.loc[c['a'] > c['b'], 'c'] = c['a']

    print('loc time span:{}'.format(time.time() - time4))
    # print(a)
    # print('c2*' * 10)
    # print(c)
    # print(a == c)

    '''
    结合numpy的向量计算.
    速度比较快的原因,numpy是c写的.
    
    a.解释执行
    
    python是解释执行.
    eg:x = 1234+5678 耗时对比.
    编译型语言指令(2~4条):
    1.读入数据,short int 1234到寄存器
    2.读入操作数据,short int 5678到寄存器
    3.通知cpu执行对应操作+
    4.输出到寄存器或内存到x对应的单元
    
    解释性语言(66条指令):
    第一次:
    while 每个字符:
        1.读入数据x
        2.比较数据
        3.根据比较结果跳转（可能还得跳转回来）
        4.累加循环计数器
        5.检查循环计数器是否到达终值
        6.根据比较结果跳转
    
    第二次:
    文本代码编译成“字节码”,（存储于扩展名为pyc的文件里），从而直接处理整型的“指令代码”，不再需要从头开始分析文本。
    但是，从“字节码”翻译到实际CPU代码这步，仍然是省不下的。
    这个消耗，可看作“利用虚拟机”执行异构CPU上的程序。有人证明过，哪怕优化到极致，这也需要10倍的性能消耗。
    这个消耗也有办法缩减。这就是JIT技术。
    
    JIT说白了，就是在第一遍执行一段代码前，先执行编译动作，然后执行编译后的代码。
    
    b.存储:
    
    1.可变类型
    对每个数据进行类型判断,C/C++里面是这样声明:
    https://docs.microsoft.com/zh-cn/windows/win32/api/oaidl/ns-oaidl-variant
    简单说，这玩意儿的思路就是“利用一个tag指示数据类型，真正的数据存储在下面的union里；访问时，依据tag指示转换/返回合适类型”
    
    2. 存储
    对C/C++来说，就存在“数组”里；而它的数组，就是赤裸裸的一片连续内存区域；区域中每若干个字节就存储了一个数值数据。   
    这种结构CPU处理起来最为方便快捷，且cache友好（若cache不友好就可能慢数倍甚至数十倍）。
    由于可变类型变成了结构体,因此而且一旦存了某些类型的数据，就不得不通过指针跳转到另一块区域才能访问（如果原地存储，浪费的空间就太恐怖了）。
    并且，它也极度的cache不友好.
    
    除此之外，还有python内部如何管理/索引/访问脚本中的全局/局部变量的问题（一般会用dict）、用户数据和物理机存储器严重不匹配引起的缓存未命中问题、
    python内部状态机/执行现场管理等等方面管理的问题——对编译型语言，这些统统不存在，CPU/内存自己就把自己照顾的很好了；
    但对解释性语言，这些都会成为“迟缓度倍增”的元凶。
    '''
    # print('a4*' * 10)
    time5 = time.time()
    # print(a['a'].values > a['b'].values)
    a['c'] = np.where(a['a'].values > a['b'].values, a['a'].values, a['b'].values)
    print('pandas with np time span:{}'.format(time.time() - time5))
    # print(a)
    # print('c3*' * 10)
    # print(c)
    # print(a == c)




    print("============ df vector str operations============")
    def rad_str(rng):
        return ''.join(random.sample(string.ascii_letters + string.digits, 8))
        # seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
        # sa = []
        # for i in range(rng):
        #     sa.append(random.choice(seed))
        # salt = ''.join(sa)
        # return salt
    aa = pd.DataFrame([(rad_str(rng=100), rad_str(rng=100)) for _ in range(1000)], columns=['a', 'b'])
    # print(aa)
    cc = deepcopy(aa)
    time_1 = time.time()
    cc['c'] = cc['b']
    print(time.time() - time_1)
    cc.loc[cc['a'].str.contains('a'), 'c'] = cc['a']
    print(time.time() - time_1)

    time2 = time.time()
    # print(a['a'].values > a['b'].values)
    aa['c'] = np.where(aa['a'].values > aa['b'].values, aa['a'].values, aa['b'].values)
    # aa['d'] = np.where('3' in aa['a'].values, aa['a'].values, aa['b'].values)
    print('pandas with np time span:{}'.format(time.time() - time2))
    # print(cc)