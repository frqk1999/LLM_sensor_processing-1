### Index 0 ###
def inspection(input_data, sampling_rate=500):
    import numpy as np
    from scipy.signal import find_peaks
    
    # Check if signal is non-periodic or periodic by finding the peaks
    peaks, _ = find_peaks(input_data, distance=sampling_rate*0.6)
    
    # Check the trend of the signal
    signal_mean = np.mean(input_data)
    signal_std = np.std(input_data)
    
    # Check for missing values
    missing_values = np.isnan(input_data).sum()
    
    if len(peaks) > 1:
        peak_distances = np.diff(peaks)
        print(f"Signal appears to have periodic components. Approx. peak-to-peak distances (in samples): {peak_distances}")
    else:
        print("Signal does not show periodic peaks.")
    
    print(f"Mean of the signal: {signal_mean}")
    print(f"Standard deviation of the signal: {signal_std}")
    print(f"Number of missing values: {missing_values}")

    # Here you might also want to check for noise or unwanted frequencies
    # e.g. by looking at frequency components with FFT if needed
    # This isn\'t implemented because we focus on the presence of cardiac peaks

inspection(input_data, sampling_rate=500)

### Index 1 ###
def solver(input_data, sampling_rate=500):
    import numpy as np
    from scipy.signal import find_peaks

    # Detect peaks in the ECG signal
    peaks, _ = find_peaks(input_data, distance=sampling_rate*0.6)
    
    # Calculate peak intervals
    peak_intervals = np.diff(peaks)
    
    # Convert intervals from samples to seconds
    intervals_in_seconds = peak_intervals / sampling_rate
    
    # Calculate Heart Rate in bpm
    if len(intervals_in_seconds) > 0:
        mean_rr_interval = np.mean(intervals_in_seconds)
        bpm = 60 / mean_rr_interval
    else:
        bpm = 0
    
    return bpm

# The function solver would be called with input_data and sampling_rate
# bpm = solver(input_data, sampling_rate=500)

### Index 2 ###
### Index 3 ###
