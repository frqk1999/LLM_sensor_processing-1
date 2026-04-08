### Index 0 ###
def inspection(input_data, sampling_rate=300):
    import numpy as np
    from scipy.signal import find_peaks, welch

    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("The signal contains missing values.")
    else:
        print("No missing values detected in the signal.")
    
    # Check if the signal is periodic and find its dominant frequencies
    freqs, psd = welch(input_data, fs=sampling_rate)
    dominant_freq_indices = np.argsort(psd)[-3:]  # Get top 3 frequency indices
    dominant_freqs = freqs[dominant_freq_indices]
    
    print(f"Dominant frequencies (Hz): {dominant_freqs}")

    # Determine if the signal is periodic
    peaks, _ = find_peaks(input_data)
    if len(peaks) > 1:
        periods = np.diff(peaks) / sampling_rate
        print(f"Detected step periods: {periods}")
    else:
        print("Could not determine periodic step pattern.")
    
    # Check for unwanted frequencies (e.g., powerline noise)
    unwanted_freqs = [50, 60]  # Common powerline frequencies
    interference = any(np.isclose(dominant_freqs, unwanted_freqs, atol=1))
    if interference:
        print("Powerline interference detected.")
    else:
        print("No significant powerline interference detected.")

inspection(input_data, sampling_rate=300)

### Index 1 ###
def inspection(input_data, sampling_rate=300):
    import numpy as np
    from scipy.signal import find_peaks, welch

    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("The signal contains missing values.")
    else:
        print("No missing values detected in the signal.")
    
    # Check if the signal is periodic and find its dominant frequencies
    freqs, psd = welch(input_data, fs=sampling_rate)
    dominant_freq_indices = np.argsort(psd)[-3:]  # Get top 3 frequency indices
    dominant_freqs = freqs[dominant_freq_indices]
    
    print(f"Dominant frequencies (Hz): {dominant_freqs}")

    # Determine if the signal is periodic by identifying peaks
    peaks, _ = find_peaks(input_data)
    if len(peaks) > 1:
        periods = np.diff(peaks) / sampling_rate
        print(f"Detected step periods: {periods}")
    else:
        print("Could not determine periodic step pattern.")
    
    # Check for unwanted frequencies (e.g., powerline noise at 50 Hz or 60 Hz)
    unwanted_freqs = [50, 60]  # Common powerline frequencies
    interference = any(np.isclose(dominant_freqs, u_freq, atol=1).any() for u_freq in unwanted_freqs)
    if interference:
        print("Powerline interference detected.")
    else:
        print("No significant powerline interference detected.")

inspection(input_data, sampling_rate=300)

### Index 2 ###
def solver(input_data, sampling_rate=300):
    import numpy as np
    from scipy.signal import find_peaks

    # Identify peaks in the data, corresponding to footfalls
    peaks, _ = find_peaks(input_data)
    
    # Calculate periods between peaks
    periods = np.diff(peaks) / sampling_rate
    
    # Calculate the average period
    average_period = np.mean(periods)
    
    # Return the average period as a numpy array
    return np.array([average_period])

# Example usage assuming input_data is provided correctly
# result = solver(input_data, sampling_rate=300)
# print(result)

### Index 3 ###
### Index 4 ###
