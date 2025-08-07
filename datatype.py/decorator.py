#enables one to modify or extend the behaviour of
#functions or without changing their code
def my_deco(func):
    def wrapper():
        print("calling hello world function")
        func()
        print("finished calling")
        func()
        for i in range(1,100):
            print("i is",i)
        func()
    return wrapper
@my_deco
def hello():
    print("hello world")
hello()