from functools import wraps,update_wrapper
from random import randint
import time
import logging
class fc(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decoration running')
        self._func()
        print('class decoration ending')

def log(f):
    print("============Simple decorator before invoking============")
    def wrapper():
        print('Simple decorator log~~')
        f()
        print('Simple decorator log~~')
    return wrapper()

@log
def fa():    
    print('this is fa')
@fc
def fb():
    print('this is fb')

def logs(level="low"):
    def deco(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if level == 'warn':
                print('logs_warn'+'$' * 10)
                print('logs_warn: %s is running..' % func.__name__)
            elif level == 'info':
                print('logs_info'+'*' * 10)
                print('logs_info: %s is running..' % func.__name__)
            return func(*args,**kwargs)
        # wrapper.__name__ = func.__name__
        # func.__name__ 函数的名字
        # func.__doc__ 函数文档字符串
        # func.__module__ 函数所属模块名称
        # func.__dict__ 函数的属性字典
        # func.__defaults__ 默认参数元组
        # func.__closure__ 函数闭包
        # update_wrapper(wrapper, func, ('__name__','__doc__'), ('__dict__',))
        return wrapper
    return deco


@logs(level ='info')
def foo(names):
    print('-' * 10)
    print('I am your %s' % (names))


def time_counting(timeout):
    # python3中，使用nonlocal访问嵌套作用域中的变量引用,或者在python2中列表方式,这样就不会在函数本地新建一个局部变量
    # customized timeout = [timeout]
    print("init timeout(%ss) was given...." % timeout)
    def setTimeout(k):
        nonlocal timeout
        # timeout[0] = k
        timeout=k
        print("reset timeout(%ss)...." % timeout)
    def deco(func):
        def wrapper(*args,**kwargs):
            start = time.time()
            res = func(*args,**kwargs)
            used = time.time() -start
            if used > timeout:
                msg = '"%s" : %s > %s'%(func.__name__,used,timeout)
                logging.warn(msg)
            return res

        
        wrapper.setTimeout = setTimeout
        return wrapper
    return deco

@time_counting(0.5)
def timeout_test():
    print("in time_counting test...")
    while randint(0,1):
        time.sleep(0.5)

if __name__ == '__main__':
    # AOP，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景，装饰器是解决这类问题的绝佳设计

    print("============simple decorator fb============") 
    fb = log(fb)
    print("============log-decorator with parameters============") 
    foo(names='fcker')
    print("============timeout-decorator with parameters============") 
    for _ in range(10):
        timeout_test()

    timeout_test.setTimeout(1)
    print("after set to 1....")
    for _ in range(10):
        timeout_test()