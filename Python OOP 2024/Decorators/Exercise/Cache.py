def cache(func):
    def wrapper(args):
        if not wrapper.log.get(args):
            wrapper.log[args] = func(args)
        
        return wrapper.log[args]
    
    wrapper.log = {}

    return wrapper


    

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
