### Index 0 ###
import numpy as np
from scipy.signal import butter, filtfilt, stft
import matplotlib.pyplot as plt

def inspection(input_data, sampling_rate=None):
    # Frequency analysis using Short-Time Fourier Transform (STFT)
    f, t, Zxx = stft(input_data, fs=sampling_rate, nperseg=256)
    # Calculate the average spectrum
    mean_spectrum = np.mean(np.abs(Zxx), axis=1)
    
    # Find the predominant low-frequency component for baseline drift
    drift_frequency_limit = 0.5  # Frequencies below this are considered as drift potentially
    
    # Check signal periodicity, trends, and contamination
    print("Mean Spectrum (first 5 values):", mean_spectrum[:5])
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("Warning: Missing values detected in the input data.")
    else:
        print("No missing values detected in the input data.")

def solver(input_data, sampling_rate=None):
    # Design a high-pass filter to remove baseline drift
    cutoff_freq = 0.5  # cutoff frequency for high-pass filtering (determined from inspection)
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(N=4, Wn=normal_cutoff, btype=\'high\', analog=False)
    
    # Filter the signal
    filtered_signal = filtfilt(b, a, input_data)
    
    # Verify QRS preservation by checking signal range 
    # and slight cross-correlation with a template if needed
    
    return filtered_signal

### Index 1 ###
### Index 2 ###
