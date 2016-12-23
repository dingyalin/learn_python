# -*- coding: utf-8 -*-
'''
Created on 2016年12月23日

@author: dWX347607
'''


l = [x * x for x in range(10)]
g = (x * x for x in range(10))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


print l
print g