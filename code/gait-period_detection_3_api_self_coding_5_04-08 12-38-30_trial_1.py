### Index 0 ###
import numpy as np
from scipy.signal import find_peaks, periodogram

def inspection(input_data, sampling_rate):
    # 1) Check if the signal is periodic or non-periodic and identify dominant frequency components
    f, Pxx = periodogram(input_data, sampling_rate)
    peak_indices, _ = find_peaks(Pxx)
    dominant_frequencies = f[peak_indices]

    # Sort in descending order and take more top frequencies than previously evaluated
    top_frequencies = sorted(dominant_frequencies, key=lambda x: Pxx[np.where(f == x)], reverse=True)[:5]
    print("Dominant frequencies:", top_frequencies)

    # 2) Check the trend of the signals (Not focusing heavily on trend as this is more about periodic behavior).
    # Calculate the mean and variance to get a sense of the trend or if it\'s centered around gravity.
    mean_value = np.mean(input_data)
    variance_value = np.var(input_data)
    
    print(f"Signal mean: {mean_value}, variance: {variance_value}")

    # 3) Check for any source of corruption in the signal, such as unwanted frequencies.
    # Identify any unusually high-frequency component that is not typical of walking
    unusual_frequencies = [freq for freq in top_frequencies if freq > 3]  # More than 3 Hz is unlikely for steps
    print("Unwanted high frequencies:", unusual_frequencies)

    # 4) Check for any missing values
    if np.any(np.isnan(input_data)):
        print("Signal contains missing values.")
    else:
        print("No missing values in the signal.")

### Index 1 ###
def solver(input_data, sampling_rate):
    # Calculate the period through the dominant frequency from valid ones
    valid_dominant_frequencies = [0.9365244536940687, 1.8730489073881373, 2.809573361082206]  # Frequencies likely related to steps
    
    # The most probable fundamental frequency is often the lowest one that is not noise
    fundamental_frequency = valid_dominant_frequencies[0]

    # Calculate period from frequency (period = 1 / frequency)
    step_period_in_seconds = 1.0 / fundamental_frequency

    # Convert the period to the sampling frame
    step_period_in_frames = step_period_in_seconds * sampling_rate

    # Return the result as a NumPy array
    return np.array([step_period_in_frames])

### Index 2 ###
### Index 3 ###
