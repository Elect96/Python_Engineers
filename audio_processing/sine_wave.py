#! /usr/bin/python
# src: https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

# frequency is the number of times a wave repeats a second
frequency = 1000
# num_sumples is the number of times a second the converter takes a sample of the analog signal
# 48000 is used in professional audio equipment
num_samples = 48000
# the sampling rate of the analog to digital converter
sampling_rate = 48000.0
# if we want full scale audio, we would take 32767 (2^15-1, the maximum value of signed 16 bit number)
# but we will take audio signal half as loud, 16000
amplitude = 16000
file = "test.wav"

sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]
# Optional: Uncomment the code below to draw a graph.
# x = range(num_samples)
# plt.plot(x[:300], sine_wave[:300])
# plt.show()

wav_file = wave.open(file, "w")
wav_file.setparams((1, 2, int(sampling_rate), num_samples, "NONE", "not compressed"))
# write the sin_wave sample by sample
for s in sine_wave:
    # pack the data to make it readable in binary format
    wav_file.writeframes((struct.pack("h", int(s * amplitude))))
wav_file.close()