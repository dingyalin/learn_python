# -*- coding: utf-8 -*-
'''
Created on 2016年12月24日

@author: dWX347607
'''

from types import MethodType

class Student(object):
    __slots__ = ('name', 'age', 'set_age', 'set_score') # 用tuple定义允许绑定的属性名称
    pass


def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
    
def set_score(self, score):
    self.score = score


s = Student()
s.name = 'Michael'
s.set_age = MethodType(set_age, s, Student)


Student.set_score = MethodType(set_score, None, Student)



s.page = 11
