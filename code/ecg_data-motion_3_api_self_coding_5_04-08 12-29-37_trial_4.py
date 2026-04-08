### Index 0 ###
def inspection(input_data, sampling_rate=500):
    import numpy as np
    from scipy.signal import find_peaks, periodogram
    import pandas as pd

    # Analyze Periodicity
    f, Pxx = periodogram(input_data, sampling_rate)
    peaks, _ = find_peaks(Pxx, height=0.01 * np.max(Pxx)) # Find peaks above 1% of max power
    dominant_frequencies = f[peaks]

    # Determine Signal Trend using Rolling Mean
    rolling_mean = pd.Series(input_data).rolling(window=int(sampling_rate/2)).mean()
    
    # Check for Unwanted Frequencies - especially low-frequency components < 0.5 Hz
    low_freq_power = np.sum(Pxx[f < 0.5])
    total_power = np.sum(Pxx)
    
    # Check for missing values
    missing_values = np.sum(np.isnan(input_data))

    print("Inspection Results:")
    print(f"Dominant Frequencies in the signal: {dominant_frequencies}")
    print(f"Low Frequency Power (< 0.5 Hz): {low_freq_power/total_power*100:.2f}% of total power")
    print("Signal Trend (Rolling Mean):", rolling_mean.tolist()[0:10])  # Print first 10 samples for brevity
    print(f"Missing values: {missing_values}")

### Index 1 ###
def solver(input_data, sampling_rate=500):
    import numpy as np
    from scipy.signal import butter, filtfilt

    # Design a high-pass Butterworth filter with a lower cutoff frequency of 0.1 Hz
    def butter_highpass(cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='high', analog=False)
        return b, a

    def highpass_filter(data, cutoff=0.1, fs=500, order=5):
        b, a = butter_highpass(cutoff, fs, order)
        y = filtfilt(b, a, data)
        return y
    
    # Apply highpass Butterworth filter to remove baseline drift
    filtered_data = highpass_filter(input_data, cutoff=0.1, fs=sampling_rate, order=5)
    
    return filtered_data

### Index 2 ###
### Index 3 ###
