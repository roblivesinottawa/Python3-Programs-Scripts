from functools import wraps 

def logit(function):
    @wraps(function)
    def with_logging(*args, **kwargs):
        print(f"{function.__name__} was called." )
        return function(*args, **kwargs)
    return with_logging

@logit
def addition_function(x):
    return x + x


result = addition_function(10)