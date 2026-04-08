### Index 0 ###
import numpy as np
from scipy.signal import find_peaks, welch
from scipy.fft import fft, fftfreq

def inspection(input_data, sampling_rate=None):
    if sampling_rate is None:
        raise ValueError("Sampling rate is required.")
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("Signal contains missing values.")
    else:
        print("No missing values detected.")

    # Check if the signal is periodic by analyzing dominant frequency components
    freqs, power = welch(input_data, fs=sampling_rate)
    dominant_freqs = freqs[np.argsort(power)[-3:]]  # Three highest power frequencies
    print(f"Dominant Frequencies: {dominant_freqs}")

    # Assess the trend, though simple here (could use detrending for real cases)
    trend = np.polyfit(range(len(input_data)), input_data, 1)
    print(f"Trend Line: Slope={trend[0]}, Intercept={trend[1]}")

    # Print basic stats 
    print(f"Mean: {np.mean(input_data)}, Std: {np.std(input_data)}")

    # Check for unwanted frequencies
    fft_vals = np.abs(fft(input_data))
    fft_freqs = fftfreq(len(fft_vals), 1/sampling_rate)
    significant_indices = np.where(fft_vals > np.partition(fft_vals, -3)[-3])[0]
    significant_freqs = np.abs(fft_freqs[significant_indices])
    print(f"Significant Frequencies: {significant_freqs}")

    # Check for any unexpected frequency components
    unwanted_freqs = significant_freqs[significant_freqs > 25]  # Anything above desired passband
    if unwanted_freqs.size > 0:
        print(f"Potential Unwanted Frequencies Detected: {unwanted_freqs}")

### Index 1 ###
from scipy.signal import butter, filtfilt

def solver(input_data, sampling_rate=None):
    if sampling_rate is None:
        raise ValueError("Sampling rate is required.")
    
    # Setting the new sampling rate
    target_sampling_rate = 50
    nyquist_rate = target_sampling_rate / 2
    
    # Anti-aliasing Butterworth Low-pass filter
    cutoff_freq = nyquist_rate - 5  # Set to slightly below Nyquist frequency of the target
    b, a = butter(N=4, Wn=cutoff_freq, btype=\'low\', fs=sampling_rate)
    
    # Filter the input data
    filtered_data = filtfilt(b, a, input_data)

    # Downsample the signal
    downsample_factor = int(sampling_rate / target_sampling_rate)
    downsampled_data = filtered_data[::downsample_factor]

    return downsampled_data

### Index 2 ###
### Index 3 ###
