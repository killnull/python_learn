# encoding:utf-8
from functools import wraps
# 总结无参装饰器模板
def outter(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        # 1、调用原函数
        # 2、为其增加新功能
        res=func(*args,**kwargs)
        return res
    return wrapper
 

# 有参装饰器模板
def 有参装饰器(x,y,z):
    def outter(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wrapper
    return outter

@有参装饰器(1,y=2,z=3) #@outter -> 被装饰对象=outter(被装饰对象) #wrapper #wrapper内调用xyz做逻辑
def 被装饰对象():
    pass
