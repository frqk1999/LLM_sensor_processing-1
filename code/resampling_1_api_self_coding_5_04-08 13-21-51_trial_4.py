### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import welch
    
    # Check periodicity by dominant frequency
    freqs, psd = welch(input_data, fs=sampling_rate)
    dominant_freq = freqs[np.argmax(psd)]
    
    # Check overall trend (using linear regression as a simple trend indicator)
    time = np.arange(len(input_data)) / sampling_rate
    coef = np.polyfit(time, input_data, 1)
    trend = coef[0]
    
    # Detect unwanted frequencies; check any fluctuation in power spectrum
    high_freqs = freqs[freqs > sampling_rate / 4]
    high_freq_power = np.sum(psd[freqs > sampling_rate / 4])
    
    # Check for missing values
    missing_values = np.isnan(input_data).sum()
    
    print(f"Dominant Frequency: {dominant_freq} Hz")
    print(f"Trend: {\'Increasing\' if trend > 0 else \'Decreasing\' if trend < 0 else \'Stable\'}")
    print(f"High Frequency Power: {high_freq_power:.2f}")
    print(f"Number of Missing Values: {missing_values}")
    return

### Index 1 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import butter, lfilter, decimate

    # Design a Butterworth lowpass filter
    cutoff_frequency = 25  # Half of the target sampling rate (50 Hz)
    nyquist_rate = sampling_rate / 2
    normal_cutoff = cutoff_frequency / nyquist_rate
    
    # Use a relatively higher order for sharper cutoff
    order = 6
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    
    # Apply the filter to the data
    filtered_data = lfilter(b, a, input_data)
    
    # Downsample the filtered signal
    downsample_factor = sampling_rate // 50
    downsampled_data = filtered_data[::downsample_factor]
    
    return downsampled_data

### Index 2 ###
### Index 3 ###
