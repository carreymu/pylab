import html

import logging
from multiprocessing import Pool
from functools import partial
from socketserver import StreamRequestHandler, TCPServer


def make_element(name, value, **attrs):
    keyvals =[' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name,attrs=attr_str,value = html.escape(value))
    return element

def rec(maxsize, *, block):
    print('receive a message')

def recs(maxsize, *p, block):
    print('receive a message')

def b(x, *args, y, **kwargs):
    pass

def add(x:int, y:int) -> int:
    return x + y

def returnTuple(brackets="square"):
    # return 1,2,3
    print(brackets)
    return (1,2,3) if(brackets=="round") else (4,12,6)

def spam(a,b,c,d):
    print(a,b,c,d)

def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r',result)


class echoHander(StreamRequestHandler):
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)
    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)


class ResultHandler:
    def __init__(self):
        self.sequence =0
    def handler(self,result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)
def add(x, y):
    return x+y


def sample():
    n = 0
    # Closure function
    def func():
        print('n=', n)
    def get_n():
        return n
    def set_n(value):
        nonlocal n
        n = value
    func.get_n= get_n
    func.set_n = set_n
    return func




if __name__ == '__main__':
    print("============ **parameter ============")
    print(make_element('item','Alba',size ='large',quality=6))

    print(make_element('p','<spam>'))

    print("============ 某些参数强制使用关键字参数传递 * ============")
    #error invoke
    # print(rec(1024, True))
    print(rec(1024, block=True))

    print(recs(1024, "10", block=True))

    print("============ doc helper ============")
    help(add)
    print("__annotations__:", add.__annotations__)

    print("============ return tuple ============")
    a1,a2 = 1,2
    (b1,b2) = 2,3
    bsk = "round"
    (a,b,c) = returnTuple(bsk)
    print("a:{},b:{},c:{}".format(a, b, c))

    print("============ Anonymous function ============")
    names = ['David Beazley', 'Crian Jones','Brian Jones1','Raymond Hettinger', 'Ned Batchelder']
    st_name = sorted(names, key = lambda name:name.split()[-1].lower())
    print(st_name)

    x=10
    a = lambda y: x + y
    x=20
    print(a(120))

    # a = lambda y, x=x: x + y

    print("============ static a parameter and subtract function parameters ============")

    s1= partial(spam, 1)
    s1(2,3,4)
    s1 = partial(spam, d=2)
    s1(1,3,4)
    s1 = partial(spam,1,c=2,d=4)
    s1(30)
    s1(10)

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add,(3,4),callback=partial(output_result,log=log))
    p.close()
    p.join()

    print("============ echo server ============")
    # sev = TCPServer(('',1500),partial(echoHander, ack='RECEIVED:'))
    # sev.serve_forever()

    r = ResultHandler()
    apply_async(add,(2,3),callback=r.handler)
    apply_async(add, ("hello", " world"), callback=r.handler)


    print("============ Closure function ============")
    f = sample()
    f()
    f.set_n(10)
    f()
    print(f.get_n())
