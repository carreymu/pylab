

def log(f):
    def wrapper():
        print('Hey log~~')
        f()
        print('Bey log~')
    return wrapper()


@log
def fa():
    print('#' * 10)
    print('this is fa')


def fb():
    print('this is fb')


def u_log(level):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if level == 'warn':
                print('$' * 10)
                print('warn: %s is running..' % f.__name__)
            elif level == 'info':
                print('*' * 10)
                print('info: %s is running..' % f.__name__)
            return f(*args)
        return wrapper()
    return decorator


@u_log(level='info')
def foo(name='foo'):
    print('-' * 10)
    print('I am %s' % name)


if __name__ == '__main__':
    print('*' * 20)
    fb = log(fb)
    # fb()
    print('*' * 20)
    # u_log(foo(name='fck'))
