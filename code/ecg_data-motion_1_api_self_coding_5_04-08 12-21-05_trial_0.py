### Index 0 ###
def inspection(input_data, sampling_rate=500):
    import numpy as np
    from scipy.signal import find_peaks, welch
    import pandas as pd

    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the signal.")
    else:
        print("No missing values detected in the signal.")

    # Check if the signal is periodic or non-periodic (It\'s expected to be periodic since it\'s ECG)
    f, Pxx = welch(input_data, fs=sampling_rate)
    dominant_frequencies = f[np.argsort(Pxx)[-3:]]  # find top 3 dominant frequencies

    if any(dominant_frequencies < 1):  # detect very low frequency components as potential artifacts
        print("The signal contains very low frequency components which could be due to baseline drift.")

    peaks, _ = find_peaks(input_data, distance=sampling_rate//2)  # Rough QRS complex estimation
    beat_intervals = np.diff(peaks) / sampling_rate
    avg_heart_rate = 60 / np.mean(beat_intervals) if len(beat_intervals) > 0 else None

    print(f"Average Heart Rate: {avg_heart_rate} BPM - Based on detected peak intervals.")

    # Check for trends in the signal using a rolling window
    rolling_mean = pd.Series(input_data).rolling(window=150).mean()  # window size can be refined
    if np.std(rolling_mean - input_data) < 0.01:  # a small threshold to detect noticeable trends
        print("There appears to be a noticeable trend or baseline drift in the signal.")

    print("Dominant frequencies detected (indicative of periodicity):", dominant_frequencies)

# This output should guide us on how to proceed for baseline drift removal.

### Index 1 ###
def solver(input_data, sampling_rate=500):
    from scipy.signal import butter, filtfilt

    # Design a high-pass filter
    def high_pass_filter(data, cutoff=0.5, fs=500, order=4):
        nyq = 0.5 * fs  # Nyquist Frequency
        normal_cutoff = cutoff / nyq  # Normalized Frequency
        b, a = butter(order, normal_cutoff, btype='high', analog=False)
        y = filtfilt(b, a, data)
        return y

    # Filter the input ECG signal
    filtered_data = high_pass_filter(input_data, cutoff=0.5, fs=sampling_rate, order=4)

    return filtered_data

### Index 2 ###
### Index 3 ###
