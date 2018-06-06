import time, functools

def performance(unit):
    def pre_decorator(f):
        @functools.wraps(f)
        def wrapper(*args,**kw):
            t1 = time.time()
            r = f(*args,**kw)
            t2 = time.time()
            t = (t2 - ti)*1000 if unit=='ms' else (t2-t1)
            print 'Call %s() in %f %s' %(f.__name__,t,unit)
            return r
        return wrapper
    return pre_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial.__name__