# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_audio = pd.read_csv('data_lambda_perf/AWS_audio_local_stats_2018-10-02.csv')
audio_durations = pd.read_csv('data_lambda_perf/audio_durations.csv')
audio_durations = audio_durations.loc[:, ~audio_durations.columns.str.contains('^Unnamed')]
data_audio = data_audio.set_index('audiofilename').join(audio_durations.set_index('filename'))
data_image = pd.read_csv('data_lambda_perf/AWS_image_local_stats_2018-10-02.csv')
data_matrix = pd.read_csv('data_lambda_perf/AWS_matrix_local_stats_2018-10-03-1.csv')
data_matrix = data_matrix.loc[0::2, :]



########################### AUDIO #############################################
plt.figure()
compute_time = np.array(data_audio.t6.astype('float') - data_audio.t4.astype('float'))
size = np.array(data_audio.audiofilesize.astype('float'))
compiled = np.vstack((size, compute_time)).T
d = compiled[compiled[:,0].argsort()]
#plt.plot(d[:, 0], d[:,1])
plt.scatter(size, compute_time)
plt.title("plot of audio to speech calculations")
plt.xlabel("Size of audio files")
plt.ylabel("Time for calculation")


########################### Duration vs Size #############################################
plt.figure()
size = np.array(data_audio.audiofilesize.astype('float'))
duration = np.array(data_audio.duration.astype('float'))
compiled = np.vstack((size, duration)).T
d = compiled[compiled[:,0].argsort()]
#plt.plot(d[:, 0], d[:,1])
plt.scatter(size, duration)
plt.title("plot of audio file duration vs size")
plt.xlabel("Size of audio files")
plt.ylabel("Duration of Audio files")


########################### IMAGE #############################################
plt.figure()
compute_time = np.array(data_image.t6 - data_image.t2.astype('float'))
size = np.array(data_image.imagefilesize.astype('float'))
compiled = np.vstack((size, compute_time)).T
d = compiled[compiled[:,0].argsort()]
#plt.plot(d[:, 0], d[:,1])
plt.scatter(size, compute_time)
plt.title("plot of image recognition calculations")
plt.xlabel("Size of image files")
plt.ylabel("Time for calculation")

########################### MATRIX#############################################
plt.figure()
io_time = np.array(data_matrix.t2.astype('float') - data_matrix.t1.astype('float'))
compute_time = np.array(data_matrix.t4.astype('float') - data_matrix.t1.astype('float'))
svd_time = np.array(data_matrix.t3.astype('float') - data_matrix.t2.astype('float'))

size = np.array(data_matrix.matrixsize.astype('float'))
compiled = np.vstack((size, compute_time, io_time, svd_time)).T
d = compiled[compiled[:,0].argsort()]
plt.plot(d[:, 0], d[:,1], label="computetime")
plt.plot(d[:,0],  d[:, 2], label="iotime")
plt.plot(d[:, 0], d[:,3], label="svd")

plt.legend()
plt.title("plot of matrix SVD calculations")
plt.xlabel("Size of matrix text files")
plt.ylabel("Time for calculation")



