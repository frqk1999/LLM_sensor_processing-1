### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=500):
    # Periodicity check and frequency domain analysis
    freqs, power_spectrum = signal.periodogram(input_data, fs=sampling_rate)
    
    # Find dominant frequency components within the ECG signal range
    peak_freqs = freqs[np.argsort(power_spectrum)[-5:]]  # Extract top 5 frequency components
    
    # Identify low-frequency range components (baseline drift candidates)
    baseline_indices = freqs < 0.5
    baseline_power = np.sum(power_spectrum[baseline_indices])
    
    # Check any high-power unwanted frequency (artifacts)
    unwanted_freq_indices = (freqs > 0.5) & (freqs < 10)  # Exclude ECG normal range
    unwanted_power = np.sum(power_spectrum[unwanted_freq_indices])
    
    # Check for missing values
    missing_values = np.isnan(input_data).sum()
    
    # Print results
    print(f"Top 5 dominant frequencies in the signal: {peak_freqs}")
    print(f"Total power in baseline wander (<0.5Hz): {baseline_power}")
    print(f"Total power in unwanted noise range (0.5Hz to 10Hz, excluding ECG): {unwanted_power}")
    print(f"Number of missing values in the data: {missing_values}")

### Index 1 ###
def solver(input_data, sampling_rate=500):
    # Design a high-pass filter with a cutoff frequency slightly below 0.5 Hz for removing baseline drift.
    # Here, we use a 6th-order Butterworth high-pass filter.
    cutoff_freq = 0.1  # Lower end, aligning with baseline drift frequency identified
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff_freq / nyquist
    
    # Design the filter
    b, a = signal.butter(N=6, Wn=normal_cutoff, btype='high', analog=False)
    
    # Apply the filter
    filtered_data = signal.filtfilt(b, a, input_data)
    
    return filtered_data

### Index 2 ###
### Index 3 ###
