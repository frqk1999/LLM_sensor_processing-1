### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=None):
    # Check if the signal is periodic by looking at the Fast Fourier Transform (FFT)
    fft_result = np.fft.fft(input_data)
    fft_freq = np.fft.fftfreq(len(input_data), d=1/sampling_rate)
    
    # Dominant frequency analysis
    magnitude = np.abs(fft_result)
    dominant_freq = fft_freq[np.argmax(magnitude)]
    print(f"Dominant frequency: {dominant_freq} Hz")

    # Check trend by examining the mean of successive halves of the data
    first_half_mean = np.mean(input_data[:len(input_data)//2])
    second_half_mean = np.mean(input_data[len(input_data)//2:])
    trend = "increasing" if second_half_mean > first_half_mean else "decreasing" if second_half_mean < first_half_mean else "stable"
    print(f"Trend of the signal: {trend}")
    
    # Look for unwanted frequencies, check power at higher frequencies
    unwanted_freqs = fft_freq[(magnitude > np.max(magnitude) * 0.1) & (fft_freq > 25)]
    if len(unwanted_freqs) > 0:
        print(f"Unwanted frequencies above 25 Hz: {unwanted_freqs}")
    else:
        print("No significant unwanted frequencies above 25 Hz.")
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("Missing values detected in the signal.")
    else:
        print("No missing values detected in the signal.")

### Index 1 ###
import numpy as np
import scipy.signal as signal

def solver(input_data, sampling_rate=None):
    # Design a low-pass filter with a cutoff frequency at 25 Hz
    nyquist_rate = sampling_rate / 2
    cutoff_freq = 25
    normalized_cutoff_freq = cutoff_freq / nyquist_rate
    
    # Use a Butterworth filter
    b, a = signal.butter(N=4, Wn=normalized_cutoff_freq, btype='low', analog=False)
    
    # Apply the anti-aliasing filter
    filtered_data = signal.filtfilt(b, a, input_data)
    
    # Perform downsampling by taking every other sample
    downsampled_data = filtered_data[::int(sampling_rate/cutoff_freq)]
    
    return downsampled_data

### Index 2 ###
### Index 3 ###
