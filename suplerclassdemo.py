
class A:
    def __init__(self):
        self.x = 0
class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startwith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

class Base:
    def __init__(self):
        print('Base.__init__')
class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')
class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')
class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')

class AA(Base):
    def __init__(self):
        super().__init__()
        print('AA.__init__')
class BB(Base):
    def __init__(self):
        super().__init__()
        print('BB.__init__')
class CC(AA, BB):
    def __init__(self):
        super().__init__()
        print('CC.__init__')


class AAA:
    def spam(self):
        print('AAA.spam')
        super().spam()
class BBB:
    def spam(self):
        print('BBB.spam')
class CCC(AAA, BBB):
    pass

if __name__ == "__main__":
    print("============ use base============")
    c= C()
    print(C.__mro__)
    print("============ use super============")
    cc= CC()
    print(CC.__mro__)

    print("============ use super============")
    c = CCC()
    c.spam()
    print(CCC.__mro__)