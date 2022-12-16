import sys

class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "singleton"):
            print("hello")
            cls.singleton = super(Singleton, cls).__new__(cls)
        return cls.singleton

class A(Singleton):
    def __init__(self,a):
        print(a)
        self.a = a

a = A(3)
b = A(4)