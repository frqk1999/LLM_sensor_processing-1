### Index 0 ###
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, welch

def inspection(input_data, sampling_rate=None):
    # Checking for periodicity using Fourier Transform
    N = len(input_data)
    freqs = fftfreq(N, 1/sampling_rate)
    fft_vals = fft(input_data)

    # Dominant frequencies
    freqs_power = np.abs(fft_vals)
    peaks, _ = find_peaks(freqs_power, height=np.mean(freqs_power))
    dominant_frequencies = freqs[peaks]

    print("Dominant frequency components:", dominant_frequencies)

    # Trend and lower frequency detection using Welch\'s method
    f, Pxx = welch(input_data, fs=sampling_rate)
    low_freqs = f[np.where(f < 0.5)]
    low_freq_power = Pxx[np.where(f < 0.5)]

    print("Low frequency components (possibly responsible for drift):", low_freqs)

    # Checking for missing values
    if np.isnan(input_data).any():
        print("There are missing values in the input data.")
    else:
        print("No missing values in the input data.")

### Index 1 ###
from scipy.signal import butter, filtfilt

def solver(input_data, sampling_rate=None):
    # Design a high-pass filter to remove baseline drift
    cutoff = 0.5  # Cutoff frequency in Hz
    order = 4  # Order of the filter
    
    # Normalize the frequency
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff / nyquist

    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='high', analog=False)

    # Apply the high-pass filter
    filtered_signal = filtfilt(b, a, input_data)

    return filtered_signal

### Index 2 ###
### Index 3 ###
