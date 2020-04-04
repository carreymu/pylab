

def f(*args, con=' & '):
    print(isinstance(args, tuple))
    print('Hello', con.join(args))
    for arg in args:
        print(arg)

def fc(a2='dd', dc: dict={}, *args, **kwargs):
    print(f"a2=={a2}")
    print(f"dc=={dc}")
    print('=='*10)
    print("args", args)
    print("kargs", kwargs)
    print("fp:{} & Scripts: {},".format(kwargs.get('fp'), "/".join(args)))

    for arg in args:
        print(arg)

    fcc(**kwargs)
    # for key, value in kwargs.items():
    #     print("%s == %s" % (key, value))

def fcc(**kwargs):
    print("fcc ==" * 10)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    print("fcc ==" * 10)

def ff(sql_info: dict, fmt: str = "json", **sql_params):
    print(f"sql_info=={sql_info}")
    print('==' * 10)
    print(f"fmt=={fmt}")
    print('==' * 10)
    print(sql_params)
    print('=='*10)

def myf(arg1, arg2, arg3):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('arg3:', arg3)

if __name__ == "__main__":
    print("============init date *** ============")
    f("python", "c", "C++", con='/')
    print('---')
    fc("Python", {"d1": 1, "d2": "2"}, "Javascript", ms="C++", fp="Haskell")

    args = ('python', 'c++', 'java')
    myf(*args)

    fargs={'arg1': 'golang'}
    ff(fargs,  ms="C++")

    kwargs = {'arg1': 'golang', 'arg2': 'c#', 'arg3': 'scala'}
    myf(**kwargs)