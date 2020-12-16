#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:14:24 2020

@author: luca
"""

# =============================================================================
# import libraries
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.io import wavfile
import librosa

fs = 48000

for index in range(100):
    # =============================================================================
    # import audio
    # =============================================================================
    
    audio = librosa.load('./test.wav', sr=fs)
    audio = audio[0]
    
    signal = audio
    
    # =============================================================================
    # slice at zero-crossings
    # =============================================================================
    
    zero_crossings = np.where(np.diff(np.sign(signal)))[0] # find zero-crossings
    
    segments = [] # initialize segment array
    
    start_pos = 0 # set start position of first segment
    for z in zero_crossings:
        x = signal[start_pos:z] # cut segment
        segments.append(x) # append segment to segment array
        start_pos = z # set start position for next segment
    x = signal[start_pos:] # cut last segment
    segments.append(x) # append last segment to segment array
    
    # =============================================================================
    # alter segments
    # =============================================================================
    
    for s in segments:
        r = random.randrange(10)
        if (r > 8):
            s *= -1
            # s *= random.uniform(-1, 1)
        
    segments_flat = [item for sublist in segments for item in sublist] # flatten list of lists to 1d-list
    segments_flat /= np.amax(np.abs(segments_flat)) # normalize
    
    # plt.plot(segments_flat) # plot segments_flat
    # plt.xlim([0, 1000]) # limit x-axes to 10 periods
    # plt.show()
    
    # =============================================================================
    # write audio
    # =============================================================================
    
    wavfile.write('./test.wav', fs, signal) # write audio
    
    filepath = './test' + str(index) + '.wav'
    wavfile.write(filepath, fs, signal) # write audio
