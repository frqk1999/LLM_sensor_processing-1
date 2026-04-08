### Index 0 ###
import numpy as np
from scipy.signal import find_peaks, periodogram, welch, firwin, lfilter

def inspection(input_data, sampling_rate):
    # 1) Check for periodicity in the signal.
    freqs, power_spectrum = periodogram(input_data, fs=sampling_rate)
    dominant_freqs = freqs[np.argsort(power_spectrum)[-5:]]  # Top 5 frequencies
    print("Dominant frequency components:", dominant_freqs)
    
    # 2) Check the trend of the signal by applying a simple moving average
    trend = np.convolve(input_data, np.ones(1000)/1000, mode=\'same\')
    
    # 3) Check for sources of corruption; e.g., via power spectral density and peak identification
    f, Pxx_den = welch(input_data, fs=sampling_rate)
    peaks, _ = find_peaks(Pxx_den, height=np.max(Pxx_den)*0.1)
    print("Identified noise peaks at frequencies:", f[peaks])
    
    # 4) Check for any missing values
    if np.any(np.isnan(input_data)):
        print("Missing values found in the signal.")
    else:
        print("No missing values found in the signal.")

### Index 1 ###
from scipy.signal import butter, sosfilt

def solver(input_data, sampling_rate):
    # Design a bandstop filter to remove noise at 375 Hz and 2000 Hz
    # Bandstop filter for around 375 Hz
    nyquist = 0.5 * sampling_rate
    low_cut1 = 370 / nyquist
    high_cut1 = 380 / nyquist
    sos1 = butter(2, [low_cut1, high_cut1], btype='bandstop', output='sos')

    # Bandstop filter for around 2000 Hz
    low_cut2 = 1995 / nyquist
    high_cut2 = 2005 / nyquist
    sos2 = butter(2, [low_cut2, high_cut2], btype='bandstop', output='sos')

    # Applying the bandstop filters sequentially
    filtered_signal = sosfilt(sos1, input_data)
    filtered_signal = sosfilt(sos2, filtered_signal)

    return filtered_signal

### Index 2 ###
### Index 3 ###
