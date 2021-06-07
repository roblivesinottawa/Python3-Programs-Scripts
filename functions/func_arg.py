def add():
    return 1 + 1

def beforeFunction(func):
    print("This is the function before add()")
    print(func())

beforeFunction(add)