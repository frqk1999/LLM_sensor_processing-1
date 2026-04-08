### Index 0 ###
import numpy as np
from scipy.fft import fft
from scipy.signal import find_peaks, detrend
import pandas as pd

def inspection(input_data, sampling_rate=None):
    # Check for missing values
    missing_values = np.isnan(input_data).sum()
    print(f"Missing values in the dataset: {missing_values}")

    # Apply FFT to find dominant frequency components
    n = len(input_data)
    yf = fft(input_data)
    xf = np.fft.fftfreq(n, 1 / sampling_rate)

    # Consider amplitude of FFT and get the main frequencies
    amplitudes = np.abs(yf)
    peaks, _ = find_peaks(amplitudes[:n // 2])
    dominant_frequencies = xf[peaks]

    # Display dominant frequency components
    print("Dominant frequency components found in signal:")
    for freq in dominant_frequencies:
        if amplitudes[freq] > np.mean(amplitudes):
            print(f"Frequency: {freq} Hz")

    # Check for trends in signal
    trend = detrend(input_data)
    trend_strength = np.max(trend) - np.min(trend)
    if trend_strength < 1e-3:
        print("No strong trend observed in the signal.")
    else:
        print("Trend detected in the signal.")

    # Check for unwanted frequencies, e.g., powerline noise frequency (50 or 60 Hz)
    power_line_noise = [50, 60]
    close_to_powerline_noise = any((np.isclose(dominant_frequencies, noise, atol=5).any()) for noise in power_line_noise)
    if close_to_powerline_noise:
        print("Possible powerline noise detected in signal.")

    # Summarize inspection results
    print("Inspection completed.")

# Assuming input_data and sampling_rate are provided during runtime for execution

### Index 1 ###
import numpy as np
from scipy.fft import fft
from scipy.signal import find_peaks, detrend


def inspection(input_data, sampling_rate=None):
    # Check if sampling_rate is provided
    if sampling_rate is None:
        print("Error: Sampling rate must be provided for analysis.")
        return None

    # Check for missing values
    missing_values = np.isnan(input_data).sum()
    print(f"Missing values in the dataset: {missing_values}")

    # Apply FFT to find dominant frequency components
    n = len(input_data)
    yf = fft(input_data)
    xf = np.fft.fftfreq(n, 1 / sampling_rate)

    # Consider amplitude of FFT and get the main frequencies
    amplitudes = np.abs(yf)
    peaks, _ = find_peaks(amplitudes[:n // 2])
    dominant_frequencies = xf[peaks]

    # Display dominant frequency components
    print("Dominant frequency components found in signal:")
    for freq in dominant_frequencies:
        if freq > 0 and amplitudes[peaks][dominant_frequencies == freq].max() > np.mean(amplitudes):
            print(f"Frequency: {freq} Hz")

    # Check for trends in signal
    trend = detrend(input_data)
    trend_strength = np.max(trend) - np.min(trend)
    if trend_strength < 1e-3:
        print("No strong trend observed in the signal.")
    else:
        print("Trend detected in the signal.")

    # Check for unwanted frequencies, e.g., powerline noise frequency (50 or 60 Hz)
    power_line_noise = [50, 60]
    close_to_powerline_noise = any((np.isclose(dominant_frequencies, noise, atol=5).any()) for noise in power_line_noise)
    if close_to_powerline_noise:
        print("Possible powerline noise detected in signal.")

    # Summarize inspection results
    print("Inspection completed.")

# Assuming input_data and sampling_rate are provided during runtime for execution

### Index 2 ###
def inspection(input_data, sampling_rate=None):
    # Ensure that the sampling rate is provided
    if sampling_rate is None:
        print("Error: Sampling rate must be provided for analysis.")
        return None

    # Check for missing values
    missing_values = np.isnan(input_data).sum()
    print(f"Missing values in the dataset: {missing_values}")

    # Apply FFT to find dominant frequency components
    n = len(input_data)
    yf = fft(input_data)
    xf = np.fft.fftfreq(n, 1 / sampling_rate)

    # Consider amplitude of FFT and get the main frequencies
    amplitudes = np.abs(yf)
    peaks, _ = find_peaks(amplitudes[:n // 2])
    dominant_frequencies = xf[peaks > 0]

    # Display dominant frequency components
    print("Dominant frequency components found in signal:")
    for freq in dominant_frequencies:
        if amplitudes[peaks][dominant_frequencies == freq].max() > np.mean(amplitudes):
            print(f"Frequency: {freq} Hz")

    # Check for trends in signal
    trend = detrend(input_data)
    trend_strength = np.max(trend) - np.min(trend)
    if trend_strength < 1e-3:
        print("No strong trend observed in the signal.")
    else:
        print("Trend detected in the signal.")

    # Check for unwanted frequencies, e.g., powerline noise frequency (50 or 60 Hz)
    power_line_noise = [50, 60]
    close_to_powerline_noise = any((np.isclose(dominant_frequencies, noise, atol=5).any()) for noise in power_line_noise)
    if close_to_powerline_noise:
        print("Possible powerline noise detected in signal.")

    # Summarize inspection results
    print("Inspection completed.")

### Index 3 ###
### Index 4 ###
# Assuming you have your data loaded into a variable named `current_data`
# and your sampling rate is defined, you would call the function like this:

current_data = np.array([your_actual_data_here])  # Replace with your actual data array
sampling_rate = 500  # Given sampling rate for your application

inspection(input_data=current_data, sampling_rate=sampling_rate)

### Index 5 ###
# Prior to the function call, ensure you have the data correctly stored in a NumPy array.
# In your workflow, you should load or collect your data into a variable.
# Example:
import numpy as np

# This is your actual collected data array
# Replace the line below with your actual data array
# Example format: data = np.array([0.5, 1.2, 0.3, ... ]) for numerical data collected
data = np.array([...])  # ¡û Replace with your own data array

# Sampling rate provided in the query
sampling_rate = 500

# Call the function for inspection
inspection(input_data=data, sampling_rate=sampling_rate)

### Index 6 ###
import numpy as np
from scipy.fft import fft
from scipy.signal import find_peaks, detrend

def inspection(input_data, sampling_rate=None):
    # Ensure that the sampling rate is provided
    if sampling_rate is None:
        print("Error: Sampling rate must be provided for analysis.")
        return None

    # Convert input_data to a float array to support NaN checking
    input_data_float = input_data.astype(float)
    
    # Check for missing values
    missing_values = np.isnan(input_data_float).sum()
    print(f"Missing values in the dataset: {missing_values}")

    # Apply FFT to find dominant frequency components
    n = len(input_data_float)
    yf = fft(input_data_float)
    xf = np.fft.fftfreq(n, 1 / sampling_rate)

    # Consider amplitude of FFT and get the main frequencies
    amplitudes = np.abs(yf)
    peaks, _ = find_peaks(amplitudes[:n // 2])
    dominant_frequencies = xf[peaks > 0]

    # Display dominant frequency components
    print("Dominant frequency components found in signal:")
    for freq in dominant_frequencies:
        if amplitudes[peaks][dominant_frequencies == freq].max() > np.mean(amplitudes):
            print(f"Frequency: {freq} Hz")

    # Check for trends in signal
    trend = detrend(input_data_float)
    trend_strength = np.max(trend) - np.min(trend)
    if trend_strength < 1e-3:
        print("No strong trend observed in the signal.")
    else:
        print("Trend detected in the signal.")

    # Check for unwanted frequencies, e.g., powerline noise frequency (50 or 60 Hz)
    power_line_noise = [50, 60]
    close_to_powerline_noise = any((np.isclose(dominant_frequencies, noise, atol=5).any()) for noise in power_line_noise)
    if close_to_powerline_noise:
        print("Possible powerline noise detected in signal.")

    # Summarize inspection results
    print("Inspection completed.")

# Assuming input_data (a numeric numpy array) and sampling_rate are provided during runtime

### Index 7 ###
import numpy as np

# Load or define your data in a NumPy array
# For demonstration, replace the dummy array below with your actual data array
data = np.array([...])  # Replace with your actual collected data

# Define the sampling rate as provided or as necessary
sampling_rate = 500  # Ensure that this is passed correctly

# Call the function for inspection with the proper arguments
inspection(input_data=data, sampling_rate=sampling_rate)

### Index 8 ###
import numpy as np

# This is an example. Replace with your actual collected data.
# Ensure that this array contains real numerical values like "data = np.array([1.0, 2.5, 3.7, ...])"
data = np.array([1.0, 2.5, 3.7])  # Replace these example numbers with your actual data

# Define the sampling rate.
sampling_rate = 500  # Be sure the sampling rate is correct for your data context

# Call the function for inspection with the proper arguments.
inspection(input_data=data, sampling_rate=sampling_rate)

### Index 9 ###
import numpy as np
from scipy.stats import zscore

def solver(input_data, sampling_rate=None):
    # Convert input data to a float array for safety
    input_data_float = input_data.astype(float)
    
    # Calculate the z-score for each data point to detect outliers
    z_scores = zscore(input_data_float)
    
    # Consider data points as outliers if the absolute z-score is greater than a threshold (e.g., 3)
    threshold = 3
    outlier_indices = np.where(np.abs(z_scores) > threshold)[0]
    
    # Print the positions of outliers
    print("Positions of outliers in the time series:")
    print(outlier_indices)
    
    # Return the indices for further use if needed
    return outlier_indices

# Assuming input_data and sampling_rate are provided during runtime for execution

### Index 10 ###
