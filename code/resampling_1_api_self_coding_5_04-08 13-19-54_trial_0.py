### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=None):
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("The signal contains missing values.")
    else:
        print("No missing values found in the signal.")
    
    # Check periodicity and find the dominant frequency components
    freqs, psd = signal.welch(input_data, fs=sampling_rate)
    dominant_frequency = freqs[np.argmax(psd)]
    print(f"Dominant frequency in the signal: {dominant_frequency} Hz")
    
    # Check trend (visual inspection in an interactive setting would differ)
    from scipy.signal import detrend
    detrended_data = detrend(input_data)
    trend_magnitude = np.mean(np.abs(input_data - detrended_data))
    print(f"Trend magnitude in the signal: {trend_magnitude}")
    
    # Check for unwanted frequencies (for example, high peaks in PSD not related to dominant frequency)
    unwanted_frequencies = freqs[(psd > np.percentile(psd, 95)) & (freqs != dominant_frequency)]
    print(f"Potential unwanted frequencies: {unwanted_frequencies}")

### Index 1 ###
def solver(input_data, sampling_rate=None):
    # First, apply an anti-aliasing filter to the input signal
    nyquist_rate = 0.5 * sampling_rate
    cutoff = 0.5 * 50  # Since we're downsampling to 50 Hz
    sos = signal.butter(N=5, Wn=cutoff/nyquist_rate, btype='low', output='sos')
    filtered_data = signal.sosfilt(sos, input_data)
    
    # Downsample the filtered signal
    downsample_factor = int(sampling_rate / 50)
    downsampled_data = filtered_data[::downsample_factor]

    return downsampled_data

### Index 2 ###
### Index 3 ###
