### Index 0 ###
import numpy as np
from scipy.signal import periodogram
from scipy.fft import fft

def inspection(input_data, sampling_rate):    
    # Checking periodicity and dominant frequencies
    frequencies, power_spectrum = periodogram(input_data, fs=sampling_rate)
    dominant_frequencies = frequencies[np.argsort(power_spectrum)[-5:]]
    print(f"Dominant frequencies are approximately: {dominant_frequencies} Hz")

    # Checking for obvious trends 
    trend = np.polyfit(range(len(input_data)), input_data, 1)
    print(f"Linear trend identified with slope: {trend[0]}")

    # Detecting unwanted frequencies potentially causing baseline drift
    fft_values = np.abs(fft(input_data))
    power_threshold = np.mean(fft_values) + 2 * np.std(fft_values)
    dominant_freqs_above_threshold = frequencies[fft_values > power_threshold]
    
    print(f"Potential unwanted frequencies above threshold: {dominant_freqs_above_threshold}")

    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("Warning: Signal contains missing values.")
    else:
        print("No missing values detected.")

    print("Inspection complete.")

### Index 1 ###
import numpy as np
from scipy.signal import periodogram
from scipy.fft import fft, fftfreq

def inspection(input_data, sampling_rate):
    # Number of samples in the input data
    num_samples = len(input_data)
    
    # Checking periodicity and dominant frequencies using periodogram
    frequencies, power_spectrum = periodogram(input_data, fs=sampling_rate)
    dominant_indices = np.argsort(power_spectrum)[-5:]
    dominant_frequencies = frequencies[dominant_indices]
    print(f"Dominant frequencies are approximately: {dominant_frequencies} Hz")

    # Checking for an overall linear trend
    trend = np.polyfit(range(num_samples), input_data, 1)
    print(f"Linear trend identified with slope: {trend[0]}")

    # Detecting unwanted frequencies potentially causing baseline drift
    fft_values = np.abs(fft(input_data))
    fft_frequencies = fftfreq(num_samples, 1 / sampling_rate)
    
    # Use only the positive frequencies, avoiding repetition
    pos_mask = fft_frequencies > 0
    power_threshold = np.mean(fft_values[pos_mask]) + 2 * np.std(fft_values[pos_mask])
    
    # Identify unwanted frequencies that exceed the threshold
    unwanted_freqs = fft_frequencies[pos_mask][fft_values[pos_mask] > power_threshold]
    
    print(f"Potential unwanted frequencies above threshold: {unwanted_freqs}")

    # Check for missing values in the signal
    if np.any(np.isnan(input_data)):
        print("Warning: Signal contains missing values.")
    else:
        print("No missing values detected.")

    print("Inspection complete.")

### Index 2 ###
from scipy.signal import savgol_filter

def solver(input_data, sampling_rate):
    # Apply Savitzky-Golay filter to smooth the data and remove baseline drift
    # Window length and polyorder can be adjusted for better performance based on the inspection
    filtered_signal = savgol_filter(input_data, window_length=501, polyorder=3, mode='interp')
    
    return filtered_signal

### Index 3 ###
### Index 4 ###
