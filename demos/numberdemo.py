import math
import numpy as np
import random
from decimal import *
from scipy import stats
# from _decimal import Decimal
from fractions import Fraction
if __name__ == '__main__':
    print("=============integer | &============")
    print(1/3.0)
    print(0 or 1)
    print(2 or 0 or 1)
    print(2 and 0 and 1)
    print(0|1|2|3)
    print(0 & 2)
    print(1 & 2)
    print(0|-2)
    print(1|0)
    
    print("=============integer ============")
    print(int(3.14))
    print(int('3', base=10))
    print(int('10101', base=2))
    print(int('f01', base=16))
    c = 20
    print('bin(x):{},oct(x):{},hex(x):{}'.format(bin(c), oct(c), hex(c)))
    print('bin(x):{},oct(x):{},hex(x):{}'.format(format(c,'b'), format(c,'o'), format(c,'x')))
    print("=============np operators ============")
    # from scipy import stats
    b = 2
    if 5 > b > 1:
       print('sss')

    print(float(1/3))
    print(float(format(1/2, '0.4f')))
    print(type(("%.30f" % (1/3))))

    js = {
       "YLZC190": "0",
       "RMS003": '\"null\"',
       "YLZC201": "31757.88",
       "YLZC281": "深圳市",
       "YLZC285": "True",
    }
    print(js['RMS003'])
    print(js['YLZC285'].isnumeric())
    print(js['YLZC201'].isnumeric())
    for k,v in js.items():
       vv = v.replace(".","")
       print(f"{k}.value {v} is number?{vv.isnumeric()}")

    print("=============scipy.stats ============")  
    print(stats.hmean([1, 9, 5, 6, 6, 7]))
    print(stats.hmean([4, 11, 15, 16, 5, 7]))
    print(stats.gmean([1, 9, 5, 6, 6, 7]))
    print(stats.gmean([4, 11, 15, 16, 5, 7]))

    print(np.std([1, 9, 5, 6, 6, 7]))
    print(np.std([4, 11, 15, 16, 5, 7]))
    print(np.var([1, 9, 5, 6, 6, 7]))
    print(np.var([4, 11, 15, 16, 5, 7]))
    print("=============round *** ============")
    a = 1.2354555
    b = 2455.24455
    print('a.round(1) is {},round=-1 {},format(0.4f):{}'.format(round(a, 4), round(b, -1), format(a, '0.4f')))
    print('format(>10.1f):{},format(<10.1f):{},format(^10.1f):{},format(,):{}'.format(format(b, '>10.1f'), format(b, '<10.1f'), format(b, '<10.1f'), format(b, '^10.1f'), format(b, ',')))
    print('format(e):{}'.format(b, '0.2E'))
    print('a + b  result is ', a + b)

    print("=============decimal *** ============")
    a = Decimal('4.3')
    b = Decimal('2.1')
    print('a is {},b is {}, a+b is {},a/b is {}'.format(a, b, a + b, a/b))
    print('bool value is {}, decimal result is {}' .format((a+b) == 6.4, (a+b)==Decimal('6.4')))

    print(int(float("34.845".replace("%",""))/100*10000)/10000)
    print(int(50.56715*10000)/10000)
    print(float(50.5670))
    
    getcontext().prec=6
    print(Decimal(1))
    qz = Decimal('50.56755').quantize(Decimal('0.0000'), rounding=ROUND_DOWN)  # ROUND_UP
    qz1 = Decimal('50.56755').quantize(Decimal('.0001'), rounding=ROUND_DOWN)  # ROUND_UP
    print(qz)
    print(qz1)
    print(str(qz))

    print("=============inf / -inf / nan *** ============")
    a = float('inf')
    b = float('-inf')
    c = float('nan')
    print('a is {},is a equals inf?{},is c equals nan:{}'.format(a, math.isinf(a), math.isnan(c)))
    print('inf+int result is {},nan+ int result:{}'.format(a+10e6, c + 10e10))

    print("=============fractions operation ============")
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print('a is {},b is {}, a+b is {}'.format(a, b, a+b))

    print("=============array operation ============")
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print('ax*2:{},ax+10:{},ax+ay:{}'.format(ax*2, ax+10, ax+ay))

    print("=============random operation ============")
    vals = [1, 2, 3, 4, 5, 6, 7, 8]
    print('rd1:{},rd2:{},get rad 2 values:{}'.format(random.choice(vals), random.choice(vals), random.sample(vals, 2)))
    
    x = 256
    y = 256
    print('is x==y ?{}'.format(x is y))
    x = 257
    y = 257
    print('is x==y ?{}'.format(x is y))
    print("=============translate operation ============")
    x = 1234567890.123456
    swap_separators = {ord('.'): ',', ord(','): '.'}
    print(format(x, ',').translate(swap_separators))
    print('fortmat1 {}, format2 {},format3 {}'.format(('%0.2f' % x),('%10.3f'% x),('%-10.1f' % x)))
