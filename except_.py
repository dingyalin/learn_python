# -*- coding: utf-8 -*-
'''
Created on 2016年12月24日

@author: dWX347607
'''


import logging


try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
    logging.exception(e)
finally:
    print 'finally...'
print 'END'