# -*- coding: utf-8 -*-
'''
Created on 2016年12月24日

@author: dWX347607
'''

'''
    #要创建一个class对象，type()函数依次传入3个参数：

    1. class的名称；
    2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) 

print Hello



# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
    
        '''
        __new__()方法接收到的参数依次是：

            #当前准备创建的类的对象；
            #类的名字；
            #类继承的父类集合；
            #类的方法集合。
        '''

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类
    
    
L = MyList()
L.add(1)
print L
    
    
    

