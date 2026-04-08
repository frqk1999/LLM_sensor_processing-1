### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=300):
    # Check if the signal is periodic or non-periodic
    freqs, power_spectrum = signal.welch(input_data, fs=sampling_rate)

    # Find the dominant frequency component
    dominant_freq = freqs[np.argmax(power_spectrum)]
    
    # Check trend (by examining if a significant low-frequency component exists)
    trend_component = power_spectrum[0] if 0 in freqs else None
    
    # Check for unwanted frequency components
    unwanted_frequencies = freqs[(power_spectrum > np.mean(power_spectrum) + 3*np.std(power_spectrum)) & (freqs < 0.5)]

    # Check for missing values
    missing_values = np.isnan(input_data).any()
    
    # Print the findings
    print("Dominant Frequency:", dominant_freq)
    print("Trend Component:", trend_component)
    print("Unwanted Frequencies:", unwanted_frequencies)
    print("Missing Values Present:", missing_values)

### Index 1 ###
import numpy as np
import scipy.signal as signal
from scipy.signal import find_peaks

def solver(input_data, sampling_rate=300):
    # Calculate the frequency domain representation using STFT
    f, t, Zxx = signal.stft(input_data, fs=sampling_rate, nperseg=256)
    
    # Consider only the walking range (1-2 Hz) for analysis
    walking_range_mask = (f >= 1) & (f <= 2)
    Zxx_walking = Zxx[walking_range_mask, :]
    f_walking = f[walking_range_mask]
    
    # Sum the power in the walking frequency range over time
    power_over_time = np.abs(Zxx_walking).mean(axis=0)
    
    # Peak detection to estimate period related to steps
    peaks, _ = find_peaks(power_over_time, height=np.mean(power_over_time))
    
    # Average time difference between peaks as a first estimator of period
    step_period_times = np.diff(t[peaks]) if len(peaks) > 1 else [0]
    
    # Calculate median of time differences
    median_period = np.median(step_period_times)
    
    # Return the median period in an ndarray
    return np.array([median_period])

### Index 2 ###
### Index 3 ###
