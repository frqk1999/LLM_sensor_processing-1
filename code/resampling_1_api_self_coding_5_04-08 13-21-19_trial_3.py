### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=None):
    # Analyze the periodicity of the signal
    freqs, power_spectrum = scipy.signal.periodogram(input_data, sampling_rate)

    # Check for dominant frequency components
    dominant_freqs = freqs[np.argsort(power_spectrum)[-5:]]
    print(f"Dominant Frequency Components (Top 5): {dominant_freqs}")

    # Analyze trends using mean and standard deviation
    trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    intercept, slope = trend
    print(f"Signal Trend: Slope = {slope}, Intercept = {intercept}")

    # Check for unwanted frequency components
    unwanted_freqs = freqs[power_spectrum > np.mean(power_spectrum) + 2 * np.std(power_spectrum)]
    print(f"Potential Unwanted Frequencies: {unwanted_freqs}")

    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("Missing values detected in the signal.")
    else:
        print("No missing values detected.")

### Index 1 ###
import numpy as np
from scipy.signal import periodogram

def inspection(input_data, sampling_rate=None):
    # Analyze the periodicity of the signal
    freqs, power_spectrum = periodogram(input_data, sampling_rate)

    # Check for dominant frequency components
    dominant_freqs = freqs[np.argsort(power_spectrum)[-5:]]
    print(f"Dominant Frequency Components (Top 5): {dominant_freqs}")

    # Analyze trends using mean and standard deviation
    trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    intercept, slope = trend
    print(f"Signal Trend: Slope = {slope}, Intercept = {intercept}")

    # Check for unwanted frequency components
    unwanted_freqs = freqs[power_spectrum > np.mean(power_spectrum) + 2 * np.std(power_spectrum)]
    print(f"Potential Unwanted Frequencies: {unwanted_freqs}")

    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("Missing values detected in the signal.")
    else:
        print("No missing values detected.")

### Index 2 ###
def solver(input_data, sampling_rate=None):
    # Design an anti-aliasing filter
    nyquist_rate = sampling_rate / 2
    cutoff_frequency = 25.0  # As we are downsampling to 50 Hz, the cutoff is 25 Hz
    sos = signal.butter(N=4, Wn=cutoff_frequency / nyquist_rate, btype='lowpass', output='sos')
    
    # Apply the anti-aliasing filter
    filtered_data = signal.sosfilt(sos, input_data)
    
    # Downsample the signal
    downsample_factor = 2
    downsampled_data = filtered_data[::downsample_factor]
    
    return downsampled_data

### Index 3 ###
### Index 4 ###
