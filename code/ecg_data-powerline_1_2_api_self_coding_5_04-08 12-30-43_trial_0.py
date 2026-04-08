### Index 0 ###
def inspection(input_data, sampling_rate=500):
    import numpy as np
    from scipy.fft import fft, fftfreq
    
    # Check for missing values
    if np.isnan(input_data).any():
        print("Missing values found in the input signal.")
    else:
        print("No missing values in the input signal.")
        
    # Perform Fourier transform to find frequency components
    n = len(input_data)
    T = 1.0 / sampling_rate
    yf = fft(input_data)
    xf = fftfreq(n, T)[:n//2]
    
    # Identify dominant frequencies in the signal
    dominant_freqs = np.abs(yf[:n//2])  # Only consider positive frequencies
    max_freq_amp = np.max(dominant_freqs)
    threshold = 0.1 * max_freq_amp  # Define a threshold to consider as dominant frequency
    
    significant_freqs = xf[dominant_freqs > threshold]
    print(f"Significant frequency components in the signal: {significant_freqs}")
    
    # Check for powerline interference (around 50Hz or 60Hz)
    for noise_freq in [50, 60]:
        if noise_freq in significant_freqs:
            print(f"Powerline noise detected at {noise_freq} Hz.")

    # Check trend - for simplicity, we can just observe if there\'s any DC offset
    mean_value = np.mean(input_data)
    if np.abs(mean_value) > 1e-3:
        print(f"Non-zero DC offset detected in the signal: {mean_value}.")
    else:
        print("No significant DC offset detected in the signal.")

### Index 1 ###
def solver(input_data, sampling_rate=500):
    from scipy.signal import iirnotch, filtfilt
    
    # Define the notch filter parameters
    freq = 50.0  # Frequency to be removed from the signal (Hz)
    Q = 30.0     # Quality factor, higher means narrower notch
    
    # Design notch filter
    b, a = iirnotch(w0=freq, Q=Q, fs=sampling_rate)
    
    # Apply the notch filter
    filtered_data = filtfilt(b, a, input_data)
    
    return filtered_data

### Index 2 ###
### Index 3 ###
