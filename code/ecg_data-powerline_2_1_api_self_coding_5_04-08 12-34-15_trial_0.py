### Index 0 ###
import numpy as np
from scipy.signal import periodogram, find_peaks

def inspection(input_data, sampling_rate=500):
    # 1. Periodicity Check
    freqs, power_spectrum = periodogram(input_data, sampling_rate)
    
    # Find dominant frequencies
    peaks, _ = find_peaks(power_spectrum, height=0.1)
    dominant_freqs = freqs[peaks]

    print(f"Dominant Frequencies in the Signal: {dominant_freqs}")

    if len(dominant_freqs) > 0:
        print("The signal shows periodic components.")

    # 2. Trend Analysis
    trend = np.mean(input_data)
    print(f"Mean of the signal (Checking for DC offset): {trend}")

    # 3. Noise Identification (focusing on 50 Hz and 60 Hz)
    noise_freqs = [50, 60]
    detected_noise = [freq for freq in noise_freqs if freq in np.round(dominant_freqs)]
    print(f"Detected Powerline Noise at: {detected_noise} Hz")

    # 4. Check for Missing Values
    missing_values = np.isnan(input_data).sum()
    print(f"Number of Missing Values in the Signal: {missing_values}")

### Index 1 ###
from scipy.signal import iirnotch, filtfilt

def solver(input_data, sampling_rate=500):
    # Notch filter design for both 50 Hz and 60 Hz
    freq_notch_50 = 50.0  # Frequency to be removed from signal (50Hz)
    freq_notch_60 = 60.0  # Frequency to be removed from signal (60Hz)
    
    # Quality factor
    quality_factor = 30.0  # Quality factor controls the width of the notch, the higher the narrower
    
    # Design notch filter for 50 Hz
    b_50, a_50 = iirnotch(freq_notch_50, quality_factor, sampling_rate)
    
    # Design notch filter for 60 Hz
    b_60, a_60 = iirnotch(freq_notch_60, quality_factor, sampling_rate)

    # Apply notch filter zero-phase filtering (filtfilt)
    filtered_data_50 = filtfilt(b_50, a_50, input_data)
    filtered_data_50_60 = filtfilt(b_60, a_60, filtered_data_50)

    return filtered_data_50_60

### Index 2 ###
### Index 3 ###
