# -*- coding: utf-8 -*-
'''
Created on 2016年12月23日

@author: dWX347607
'''

class Student(object):
    '''
        @property装饰器就是负责把一个方法变成属性调用的
        @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    '''
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

if __name__ == "__main__":
    s = Student()
    s.score = 50
    print s.score
    
    s.score = 200
    print s.score
    
    
    