"""def my_dec(fun):
    def wrapper():
        print("hello from wrapper")
        fun()
    return wrapper

@my_dec
def greet():
    print("hello from greet")"""


'''def my_dec(fun):
    def wrapper(a,b):
        if b>0:
            fun(a,b)
        else:
            print("b have to be greater than zero")
    return wrapper

@my_dec
def division(a,b):
    print(a/b)


division(17,2)'''

'''
def gift_pack(func):
    def wrapper():
        print("wrapping the gift")
        func()
        print("the gift")
    return wrapper

@gift_pack
def git():
    print("this is gift")

git()

'''
def my_dec(fun):
    def wrapper(a,b):
        if b>0:
            fun(a,b)
        else:
            print("b have to be greater than zero")
    return wrapper

@my_dec
def division(a,b):
    print(a/b)


division(17,2)






