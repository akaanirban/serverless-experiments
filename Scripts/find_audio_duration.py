#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:36:33 2018

@author: anirban
"""

import subprocess
import os
import numpy as np
import pandas as pd


def get_duration(filename):
    # valid for any audio file accepted by ffprobe
    args = ("""ffprobe -i """ + filename + """ -show_entries format=duration -v quiet -of csv="p=0" """)
    time = subprocess.run(args, check=True, stdout=subprocess.PIPE, shell=True).stdout.strip().decode("utf-8")
    return float(time)

# Get all the file paths from the directory specified
def get_file_paths(dirname):
	file_paths = []  
	for root, directories, files in os.walk(dirname):
		for filename in files:
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)  
	return file_paths

if __name__ == "__main__":
    DIR = "/home/anirban/data/Music/rhys_mcg"
    audiofiles = get_file_paths(DIR)
    durations = np.zeros((len(audiofiles), 1))
    for idx, file in enumerate(audiofiles):
        dur = get_duration(file)
        durations[idx,0] = dur
        
    file_duration = pd.DataFrame({'filename': audiofiles, 'duration': durations})







