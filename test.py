#!/usr/bin/env python
# encoding: utf-8

from qps import QPS

def add(a, b):
    return a + b

with QPS(1000, add, 1, 2) as qps:
    pass
