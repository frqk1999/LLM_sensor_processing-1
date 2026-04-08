### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=None):
    # Inspect the input data to understand its characteristics before downsampling.

    # Check if the average and median are equal (indicating periodic signal)
    avg = np.mean(input_data)
    median = np.median(input_data)
    
    # Check for missing values
    missing_values = np.isnan(input_data).any()

    if avg == median:
        periodic = True
    else:
        periodic = False

    # Compute the Fourier Transform to find dominant frequencies
    freqs = np.fft.fftfreq(len(input_data), d=1/sampling_rate)
    fft_values = np.abs(np.fft.fft(input_data))
    
    # Find the most dominant frequency
    dominant_freq = freqs[np.argmax(fft_values)]
    
    print(f"Periodic Signal: {periodic}")
    print(f"Dominant Frequency: {dominant_freq}")
    print(f"Missing Values: {missing_values}")
    print(f"Signal has {32}s samples (2s of 100Hz)")

def solver(input_data, sampling_rate=100):
    # Enhanced filter design
    
    # Nyquist rate for target sampling rate of 50Hz
    target_sampling_rate = 50
    nyquist_rate = target_sampling_rate / 2.0

    # Design an anti-aliasing filter
    sos = signal.butter(8, nyquist_rate, btype=\'low\', fs=sampling_rate, output=\'sos\')

    # Apply the filter to the input data
    filtered_data = signal.sosfilt(sos, input_data)

    # Downsample the filtered data
    downsampled_data = signal.resample(filtered_data, int(len(input_data) * target_sampling_rate / sampling_rate))

    return downsampled_data

### Index 1 ###
### Index 2 ###
