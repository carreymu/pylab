

def f(*args, con=' & '):
    print(isinstance(args, tuple))
    print('Hello', con.join(args))
    for arg in args:
        print(arg)

def fc(*args, **kwargs):
    print("args", args)
    print("kargs", kwargs)
    print("fp:{} & Scripts: {},".format(kwargs.get('fp'), "/".join(args)))

    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

def myf(arg1, arg2, arg3):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('arg3:', arg3)

if __name__ == "__main__":
    print("============init date *** ============")
    f("python", "c", "C++", con='/')
    print('---')
    fc("Python", "Javascript", ms="C++", fp="Haskell")

    args = ('python', 'c++', 'java')
    myf(*args)

    kwargs = {'arg1': 'golang', 'arg2': 'c#', 'arg3': 'scala'}
    myf(**kwargs)