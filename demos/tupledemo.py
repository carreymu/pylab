from collections import namedtuple

def dict_to_placeholderSub(s):
    return placeholderSub._replace(**s)
def compute_costIndex(records):
    total = 0.0
    for rec in records:
        total = rec[1] + rec[2]
    return total

# 耦合太高了吧
Stock = namedtuple('stock', ['name', 'shares', 'price'])
def compute_costNameTuple(records):
    total = .0
    for rec in records:
        s = Stock(*rec)
    total += s.shares * s.price
    return total


if __name__=='__main__':

    # 命名元组,字典的替代,不像字典那样,一个命名元组是不可更改
    subscribe = namedtuple('subscriber', ['addr', 'joined', 'caca'])
    print('subscribe is ', subscribe)
    sub = subscribe('jonesy@example.com', '2012-10-19', 1)
    print('sub is ', sub)
    add, email, num ,length= sub.addr, sub.joined, sub.caca, len(sub)
    print('add,email is %s and %s' % (add, email))

    sub = sub._replace(caca='cao')
    print('replaced sub is ', sub)

    placeholderSub = subscribe('', '', 0)
    print('placeholderSub is ', placeholderSub)

    setSub = {'addr':'acme', 'caca': 200, 'joined':'jerry@email.com'}
    dict_to_placeholderSub(setSub)



    tuple_demo = (("one",1), ("two",2), ("three",3), ("four",4))
    print(tuple_demo[0])
    print(len(tuple_demo))
    print(len(tuple_demo[0]))
    i = 0
    flt_tuple = [x for x in tuple_demo if x[1] == 2 or x[1] == 3]
    print(flt_tuple)
    print(len(flt_tuple))
    for i in tuple_demo:
        print(i[0])
