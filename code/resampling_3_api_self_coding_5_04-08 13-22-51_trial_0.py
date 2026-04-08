### Index 0 ###
import numpy as np
from scipy.fft import fft

def inspection(input_data, sampling_rate=None):
    # 1) Check if the signal is periodic or non-periodic
    amplitude_spectrum = np.abs(fft(input_data))
    dominant_frequencies = np.argsort(amplitude_spectrum)[-5:]  # Top 5 frequencies
    print("Dominant frequency components (indices):", dominant_frequencies)
    
    # 2) Check the trend of the signals
    trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    print("Trend (slope, intercept):", trend)
    
    # 3) Check for unwanted frequency components (such as power-line interference)
    # Assuming 50 Hz or 60 Hz power-line frequency
    power_line_freqs = [50, 60]
    power_line_detected = False
    for freq in power_line_freqs:
        peak_idx = int(len(input_data) * freq / sampling_rate)
        if amplitude_spectrum[peak_idx] > 0.1 * np.max(amplitude_spectrum):  # Arbitrary threshold
            power_line_detected = True
    
    print("Power-line interference detected:", power_line_detected)
    
    # 4) Check for missing data
    is_finite = np.all(np.isfinite(input_data))
    print("Any missing/NaN values in data:", not is_finite)

# Assuming input_data and sampling_rate will be provided when the function is called.

### Index 1 ###
import numpy as np

def solver(input_data, sampling_rate=None):
    # Downsample by taking every other sample
    downsampled_data = input_data[::2]
    return downsampled_data

### Index 2 ###
### Index 3 ###
