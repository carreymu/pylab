from functools import partial


class Super:
    def __init__(self, sub_cls, instance):
        # if sub_cls = B, instance = D()
        # Super(B, self).add(233)
        mro = instance.__class__.mro()
        # mro == [D, B, C, A, object]
        # sub_cls is B
        # find class behind sub_cls from mro
        # __mro_tail == [C, A, object]
        self.__mro_tail = mro[mro.index(sub_cls)+1:]
        self.__sub_cls = sub_cls
        self.__instance = instance

    def __getattr__(self, name):
        # find methods in every class from  mro_tail
        for cls in self.__mro_tail:
            if not hasattr(cls, name):
                continue

            print('call {}.{}'.format(cls, name))
            # get definding methods from class
            attr = getattr(cls, name)
            # if d = D(); d.add(233)  equals D.add(d, 233)
            # fill first self arg
            return partial(attr, self.__instance)

        raise AttributeError(name)


class NewA:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class NewB(NewA):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        Super(NewB, self).add(m)
        self.n += 3


class NewC(NewA):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        Super(NewC, self).add(m)
        self.n += 4


class NewD(NewB, NewC):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        Super(NewD, self).add(m)
        self.n += 5


class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add,origin n is {1}'.format(self, self.n))
        self.n += m
        print('A\'n is {}'.format(self.n))


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add,origin n is {1}'.format(self, self.n))
        super().add(m)
        self.n += 3
        print('B\'n is {}'.format(self.n))


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add,origin n is {1}'.format(self, self.n))
        super().add(m)
        self.n += 4
        print('C\'n is {}'.format(self.n))


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add,origin n is {1}'.format(self, self.n))
        # self's MRO is [D, B, C, A, object]
        # D's MRO is [B, C, A, object]
        super().add(m)
        self.n += 5
        print('D\'n is {}'.format(self.n))

if __name__ == '__main__':
    # b = B()
    # b.add(2)
    # print(b.n)
    # print('==========')
    # d = D()
    # d.add(2)
    # print(d.n)
    print('==========')

    nd = NewD()
    nd.add(2)
    print(nd.n)