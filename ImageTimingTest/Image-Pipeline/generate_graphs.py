#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:33:20 2018

@author: "Anirban Das"
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure()
data = pd.read_csv('all_timings_35_vgg16.txt', header=None, names=["filename", "filesize", "imagewidth", "imageheight", "t1", "t2", "t3"])
data = data.reset_index(drop=True)
ax = fig.gca(projection='3d')
ax.scatter(data.imageheight, data.imagewidth, data.t3-data.t2, label='Resize + forwardprop')
ax.set_ylabel('Imagewidth')
ax.set_xlabel('Imageheight')
ax.set_zlabel('compute time')

plt.figure()
time_forward = data.t3 - data.t2
time_resize = data.t2 - data.t1
time_total = data.t3 - data.t1
plt.plot(np.arange(data.shape[0]), time_forward, label="Forward prop time")
plt.plot(np.arange(data.shape[0]), time_resize, label="Image resize time")
plt.plot(np.arange(data.shape[0]), time_total, label="total time")
plt.legend()
plt.xlabel("indices of copy of ILSVRC2012_test_00000035.JPEG ")
plt.ylabel("time in seconds")
# =============================================================================
# ax2 = fig.gca(projection='3d')
# ax2.scatter(data.imageheight, data.imagewidth, data.t2-data.t1, label='Resize')
# ax2.set_ylabel('Imagewidth')
# ax2.set_xlabel('Imageheight')
# ax2.set_zlabel('Resize time')
# 
# ax3 = fig.gca(projection='3d')
# ax3.scatter(data.imageheight, data.imagewidth, data.filesize, label='Filesize')
# ax3.set_ylabel('Imagewidth')
# ax3.set_xlabel('Imageheight')
# ax3.set_zlabel('Filesize')
# =============================================================================

