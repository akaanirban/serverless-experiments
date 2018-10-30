#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:54:56 2018

@author: "Anirban Das"
"""

import numpy as np
from timeit import default_timer as timer


t1 = timer()
A = np.random.random((10000, 10000))
for i in range(100):
    t2 = timer()
    A = np.multiply(A, A)
    t3 = timer()
    print("T3-T2", t3-t2)


B = np.random.rand(10000, 10000)
t4 = timer()
B[B> 0.1] = 0
t5 = timer()
B = np.multiply(B, B)
t6 = timer()

print("T2-T1", t2-t1)
print("T3-T2", t3-t2)
print("T4-T3", t4-t3)
print("T5-T4", t5-t4)
print("T6-T5", t6-t5)







































