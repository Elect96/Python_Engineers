#! /usr/bin/python
# src: https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

# frequency is the number of times a wave repeats a second
frequency = 1000
noisy_freq = 50
num_samples = 48000
# the sampling rate of the analog to digital converter
sampling_rate = 48000.0

# create the sine wave and noise
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]
sine_noise = [np.sin(2 * np.pi * noisy_freq * x/sampling_rate) for x in range(num_samples)]

# convert them to numpy arrays
sine_wave = np.array(sine_wave)
sine_noise = np.array(sine_noise)

# combined signal
combined_signal = sine_wave + sine_noise

# plotting
plt.subplot(3, 1, 1)
plt.title("Original sine wave")
# Need to add empty space
plt.subplots_adjust(hspace=.5)
plt.plot(sine_wave[:500])
plt.subplot(3, 1, 2)
plt.title("Noisy wave")
plt.plot(sine_noise[:4000])
plt.subplot(3, 1, 3)
plt.title("Original + Noise")
plt.plot(combined_signal[:3000])
plt.show()

# combined noise + signal wave
data_fft = np.fft.fft(combined_signal)
# absolute of the frequencies found in it
freq = (np.abs(data_fft[:len(data_fft)]))

plt.plot(freq)
plt.title("Before filtering: Will have main signal (1000Hz) + noise frequency (50Hz)")
plt.xlim(0, 1200)
plt.show()

filtered_freq = []
index = 0
for f in freq:
    # Filter between lower and upper limits
    # Choosing 950, as closest to 1000. In real world, won't get exact numbers like these
    if 950 < index < 1050:
        # Has a real value. I'm choosing >1, as many values are like 0.000000001 etc
        if f > 1:
            filtered_freq.append(f)
        else:
            filtered_freq.append(0)
    else:
        filtered_freq.append(0)
    index += 1

# plotting
plt.plot(filtered_freq)
plt.title("After filtering: Main signal only (1000Hz)")
plt.xlim(0, 1200)
plt.show()
plt.close()

# inverse fft, will take the signal and convert it back to time domain
recovered_signal = np.fft.ifft(filtered_freq)

# plotting
plt.subplot(3,1,1)
plt.title("Original sine wave")
# Need to add empty space, else everything looks scrunched up!
plt.subplots_adjust(hspace=.5)
plt.plot(sine_wave[:500])

plt.subplot(3,1,2)
plt.title("Noisy wave")
plt.plot(combined_signal[:4000])

plt.subplot(3,1,3)
plt.title("Sine wave after clean up")
plt.plot((recovered_signal[:500]))
plt.show()