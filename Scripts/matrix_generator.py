#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:10:06 2018

@author: anirban
"""

#Matrix Generators
import numpy as np
import pandas as pd


def sparse_matrix(N1, N2, f, conversion=np.asarray, rseed=0):
    """create NxN matrix with an approximate fraction f of nonzero entries"""
    rng = np.random.RandomState(rseed)
    M = rng.randint(1, 100, (N1, N2))
    #M = rng.randn(N1, N2)
    M[M > f] = 0
    return conversion(M)

for i in range(1, 13):
    data = pd.DataFrame(sparse_matrix(2**i, 2**i, 60, np.asarray, 0))
    data.to_csv("/home/anirban/Desktop/Matrices/test_{}.csv".format(i))

