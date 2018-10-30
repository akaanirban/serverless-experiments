#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:13:53 2018

@author: anirban
"""
from timeit import default_timer as timer

def recurive_fibonacci(n):
    if n <= 1:
        return 1
    else:
        return recurive_fibonacci(n-1)+ recurive_fibonacci(n-2)


for i in range(20):
    t = timer()
    print("Gor the {}th Fibonacci number {} in {} seconds ".format(i, recurive_fibonacci(i), timer()-t))