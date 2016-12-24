# -*- coding: utf-8 -*-
'''
Created on 2016年12月23日

@author: dWX347607
'''

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

#在执行到IO操作时，gevent自动切换 gevent.sleep()

def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
])





