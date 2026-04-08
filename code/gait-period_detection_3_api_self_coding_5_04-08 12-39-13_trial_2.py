### Index 0 ###
def inspection(input_data, sampling_rate):
    import numpy as np
    from scipy.signal import welch

    # 1. Check for periodicity using Welch\'s method
    frequencies, power_density = welch(input_data, fs=sampling_rate, nperseg=1024)
    dominant_frequency_index = np.argmax(power_density)
    dominant_frequency = frequencies[dominant_frequency_index]
    
    print(f"Dominant frequency (using Welch\'s method): {dominant_frequency} Hz")
    
    # 2. Harmonic inspection (example analysis using harmonics)
    harmonics = frequencies[power_density > 0.1 * np.max(power_density)]
    harmonics.sort()
    print(f"Harmonics frequencies (perhaps indicating fundamental and its multiples): {harmonics}")

    # 3. Trend Analysis - check if data drifts over time
    if np.ptp(input_data) > 10 * np.std(input_data):
        print("Significant trend detected, consider detrending.")
    else:
        print("No significant trend detected.")

    # 4. Corruption check for noise
    noise_threshold = 0.2 * np.max(power_density)
    noise_frequencies = frequencies[power_density > noise_threshold]
    print(f"Potential noise frequencies: {noise_frequencies}")

    # 5. Check for missing data
    missing_data_check = np.isnan(input_data)
    if np.any(missing_data_check):
        print("Missing data detected.")
    else:
        print("No missing data detected.")

    # Inform if setting looks reasonably clean
    if not np.any(missing_data_check) and len(noise_frequencies) <= 5:
        print("Signal is reasonably clean.")

inspection(input_data, sampling_rate)

### Index 1 ###
def solver(input_data, sampling_rate):
    import numpy as np
    from scipy.signal import welch

    # Determine the dominant frequency using Welch's method again to ensure consistency
    frequencies, power_density = welch(input_data, fs=sampling_rate, nperseg=1024)
    dominant_frequency_index = np.argmax(power_density)
    dominant_frequency = frequencies[dominant_frequency_index]

    # Calculate the average step period (inverse of frequency)
    average_step_period = 1 / dominant_frequency  # in seconds
    
    # Convert the step period from seconds to frames (sample) based on the sampling rate
    average_step_period_in_frames = average_step_period * sampling_rate  # in samples

    # Return as a single scalar
    return np.array([average_step_period_in_frames])

# Call the solver function
solver(input_data, sampling_rate)

### Index 2 ###
### Index 3 ###
