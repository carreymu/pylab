from functools import partial
from socket import socket,AF_INET,SOCK_STREAM
import math

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
        # return 'Pair(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

_formats ={
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if(code == ''):
            code ='ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []
    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        print('start connect')
        return sock
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()
        print('close connect')

class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def diameter(self):
        return self.radius * 2
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("can't delete attribute")

class SubPerson(Person):
    # overwrite super getter
    @property
    def first_name(self):
        print('Getting first_name in subPerson')
        return super().first_name
    # overwrite super getter again
    @Person.first_name.getter
    def first_name(self):
        print('Person.first_name.getter in subPerson')
        return super().first_name
    @first_name.setter
    def first_name(self, value):
        print('Setting first_name to', value)
        super(SubPerson, SubPerson).first_name.__set__(self, value)
    @first_name.deleter
    def first_name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).first_name.__delattr__(self)

class SubPerson1(Person):
    # @property
    @Person.first_name.getter
    def first_name(self):
        print('Getting first_name from subperson1')
        return super().first_name


class Integer:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]
class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y



#######inheritance#########
class Animal:
    def __init__(self, can_fly=False):
        self.can_fly = can_fly

    def fly(self):
        print(('I CAN FLY!' if self.can_fly else 'I can not fly'))

class Dog(Animal):
    def bark(self):
        print('Woooooooooooof')

class Fly:
    def fly(self):
        print('I am a fly and I am happy to fly.')
    def flying(self):
        print('I am flying')

if __name__ =="__main__":
    print("============ __repr__ replace __str__============")
    p = Pair(3, 4)
    print('p is {0!r}'.format(p))
    print('p is {0}'.format(p))
    print(p)

    print("============ Customized [with] ============")
    # conn = LazyConnection(('www.python.org',80))
    # with conn as s:
    #     pass
    #     with conn as s2:
    #         pass

    print("============add check to class attribute ============")
    a = Person('guido')
    print(a.first_name)

    print("============union functions in a class============")
    c = Circle(4.0)
    print("c.radius is ", c.radius)
    print('c.area is ', c.area)
    print('c.perimeter is ', c.perimeter)

    print("============sub_class============")
    s = SubPerson('Guido')
    print('s.first_name', s.first_name)
    print(SubPerson.__mro__)
    print('---')
    s.first_name = "Larry"
    print('s.first_name', s.first_name)
    print('---overwrite only one method')
    s1= SubPerson1('JinGuo')
    print('s1.first_name', s1.first_name)
    s1.first_name = 'Leeeee'
    print('s1.first_name', s1.first_name)

    print("============create new class or attribute============")
    p = Point(2, 3)
    print('p.x is {},p.y is {}'.format(p.x, p.y))
    p.x = 5
    # error
    # p.y = 2.3
    print('p.x is {},p.y is {}'.format(p.x, p.y))
    print(Point.x)

    print("============inheritance============")
    d = Dog()
    # d.can_fly = True
    d.fly()
    d.bark()

    print("============override============")
    f = Fly()
    f.fly()
    f.flying()
