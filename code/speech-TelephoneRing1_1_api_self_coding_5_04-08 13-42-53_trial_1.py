### Index 0 ###
import numpy as np
from scipy.signal import find_peaks, welch

def inspection(input_data, sampling_rate=None):
    # Check if input data is periodic or not using Fourier Transform
    frequencies = np.fft.rfftfreq(len(input_data), 1/sampling_rate)
    fft_magnitudes = np.abs(np.fft.rfft(input_data))
    
    # Find dominant frequencies
    peaks, _ = find_peaks(fft_magnitudes, height=np.max(fft_magnitudes) * 0.1)
    peak_freqs = frequencies[peaks]
    peak_mags = fft_magnitudes[peaks]

    print("Identified dominant frequencies (Hz):", peak_freqs)
    print("Corresponding magnitudes:", peak_mags)

    # Use Welch\'s method for power spectral density estimation
    freq_welch, psd = welch(input_data, fs=sampling_rate, nperseg=1024)
    
    # Inspect unwanted frequency component potentially belonging to ringing
    max_noise_freqs = peak_freqs[peak_freqs > 1000]  # Example threshold
    print("Potential unwanted noise frequencies (Hz):", max_noise_freqs)

    # Inspect signal trend (i.e., drift over time)
    trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    print("Overall trend in signal:", trend)

    # Check for missing values (NaNs or Infs)
    if np.any(np.isnan(input_data)) or np.any(np.isinf(input_data)):
        print("Warning: The signal contains missing or infinite values.")
    else:
        print("The signal does not contain missing or infinite values.")

### Index 1 ###
from scipy.signal import iirnotch, filtfilt

def solver(input_data, sampling_rate=None):
    # Define notch frequencies for ringing noise
    noise_freqs = [
        1006.67, 1015, 1030, 1038.33, 1045, 1071.67, 1103.33, 1121.67, 
        1130, 1138.33, 1150, 1216.67, 1230, 1976.67, 1980, 1988.33, 
        1991.67, 1995, 1998.33, 2001.67, 2005, 2010, 2013.33, 2026.67, 2030, 2043.33, 2076.67, 2080
    ]

    filtered_data = input_data.copy()
    for f in noise_freqs:
        # Design notch filter to remove specific ringing frequency
        b, a = iirnotch(w0=f / (sampling_rate / 2), Q=30)  # Higher Q factor for narrower notch
        filtered_data = filtfilt(b, a, filtered_data)

    return filtered_data

### Index 2 ###
### Index 3 ###
