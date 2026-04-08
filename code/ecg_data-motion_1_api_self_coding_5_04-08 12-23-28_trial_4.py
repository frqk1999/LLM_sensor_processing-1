### Index 0 ###
import numpy as np
from scipy.signal import welch, butter, sosfilt
from statsmodels.tsa.seasonal import STL
from numpy import isnan

def inspection(input_data, sampling_rate):
    # Check if the signal is periodic or non-periodic
    f, Pxx = welch(input_data, fs=sampling_rate)
    
    print("Frequency components: ", f)
    dominant_freqs = f[np.argsort(Pxx)[-3:]]  # Example to print top 3 frequencies
    print("Dominant frequency components: ", dominant_freqs)
    
    # Check trend of the signals using STL
    result = STL(input_data, period=500, seasonal=13).fit()
    print("Trend observed with STL: ", np.sum(result.trend))
    
    # Corruption (Check for powerline noise frequency around 60Hz)
    if np.any((f >= 59) & (f <= 61)):
        print("Evidence of powerline noise")
    
    # Check for missing values
    if np.any(isnan(input_data)):
        print("Missing values present in the data")
    else:
        print("No missing values in data")

### Index 1 ###
import numpy as np
from scipy.signal import butter, sosfilt, sosfreqz

def solver(input_data, sampling_rate=500):
    def bandstop_filter(data, f1, f2, fs, order=2):
        # Bandstop filter to remove powerline noise (e.g., 59Hz - 61Hz to capture variations)
        sos = butter(order, [f1, f2], btype='bandstop', fs=fs, output='sos')
        return sosfilt(sos, data)

    def highpass_filter(data, cutoff_freq, fs, order=5):
        # High-pass filter for removing baseline drift
        # We determined the drift frequencies (<1Hz), hence higher cutoff
        sos = butter(order, cutoff_freq, btype='highpass', fs=fs, output='sos')
        return sosfilt(sos, data)

    # Remove powerline noise
    filtered_data = bandstop_filter(input_data, 59, 61, sampling_rate)

    # Remove baseline drift using a high-pass filter
    # Choosing cutoff frequency of 0.8 Hz based on inspection
    filtered_data = highpass_filter(filtered_data, 0.8, sampling_rate)

    return filtered_data

### Index 2 ###
### Index 3 ###
