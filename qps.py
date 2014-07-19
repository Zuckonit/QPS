#!/usr/bin/env python
# encoding: utf-8
import time

'''
Example::
    def add(a, b):
        return a+b

    with QPS(1000, add, 1, 2) as qps:
        # Put whatever logic you want here.
        # ``for`` loops are great here for timing things that are very fast.
        print qps.qps


'''

class QPS(object):
    """
    A context manager that qps the code it wraps.

    """
    def __init__(self, times, func, *args, **kwargs):
        self.start = None
        self.end = None
        self.qps = None
        self.elapsed = None
        self.times = times
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __enter__(self):
        self.start = time.time()
        for i in xrange(self.times):
            self.func(*self.args, **self.kwargs)
            
        return self

    def __exit__(self, type, value, tb):
        if tb:
            return False
        self.end = time.time()
        self.qps = (self.end - self.start)/self.times
        print self.qps
