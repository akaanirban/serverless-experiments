#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:08:30 2018

@author: anirban
"""

from timeit import default_timer as timer
import numpy as np

size = 10

t0 = timer()
q, r = np.linalg.qr(np.random.rand(size, size))
t1 = timer()
print(t1-t0)

q, r = np.linalg.qr(np.random.rand(size**2, size**2))
t2 = timer()
print(t2-t1)

q, r = np.linalg.qr(np.random.rand(size**3, size**3))
t3 = timer()
print(t3-t2)

q, r = np.linalg.qr(np.random.rand(size**4, size**4))
t4 = timer()
print(t4-t3)













