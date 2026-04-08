### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    from scipy.fft import fft, fftfreq
    
    # Check if input_data is a one-dimensional array
    if input_data.ndim != 1:
        print("Input data must be a one-dimensional array.")
        return
    
    # Frequency domain analysis
    n = len(input_data)
    fft_values = fft(input_data)
    fft_frequencies = fftfreq(n, 1/sampling_rate)
    
    # Only consider the positive frequencies
    fft_frequencies = fft_frequencies[:n // 2]
    fft_values = np.abs(fft_values[:n // 2])
    
    # Identify periodicity
    threshold = np.max(fft_values) * 0.1  # Threshold to detect dominant frequencies
    dominant_freqs = fft_frequencies[fft_values > threshold]
    
    # Check the trend and print properties
    if len(dominant_freqs) > 0:
        print("Signal is periodic. Dominant frequencies (Hz):", dominant_freqs)
    else:
        print("Signal is non-periodic")
    
    # Check for noise outside typical ECG frequencies (ECG: 0.5-150 Hz)
    noise_indices = np.where((fft_frequencies > 150) & (fft_values > threshold))[0]
    if len(noise_indices) > 0:
        print("Noise detected at frequencies above 150 Hz.")
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("Signal contains missing values.")
    else:
        print("No missing values detected.")

### Index 1 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import butter, filtfilt

    # Design a low-pass Butterworth filter
    def butter_lowpass(cutoff, fs, order=5):
        nyquist = 0.5 * fs  # Nyquist Frequency
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    # Apply the low-pass filter to the input data
    def lowpass_filter(data, cutoff_freq, fs, order=5):
        b, a = butter_lowpass(cutoff_freq, fs, order=order)
        y = filtfilt(b, a, data)  # Apply the filter
        return y

    # Define cutoff frequency for ECG low-pass filter, typically below 150 Hz
    cutoff_frequency = 150  # Cutoff frequency of the filter

    # Apply the filter
    filtered_data = lowpass_filter(input_data, cutoff_frequency, sampling_rate)

    return filtered_data

### Index 2 ###
### Index 3 ###
