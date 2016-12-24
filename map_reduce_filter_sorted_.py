# -*- coding: utf-8 -*-
'''
Created on 2016年12月24日

@author: dWX347607
'''




print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


print reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9])



print filter(lambda x : x % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15])

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
