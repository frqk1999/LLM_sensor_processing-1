### Index 0 ###
import numpy as np
from scipy.signal import find_peaks

def inspection(input_data, sampling_rate=None):
    # Check if the signal is periodic and identify dominant frequency components
    print("Inspecting ECG signal for periodicity and QRS complexes...")
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("Missing values detected in the signal.")

    # Check for periodic components
    freq_spectrum = np.fft.fft(input_data)
    freq_magnitudes = np.abs(freq_spectrum)
    dominant_freqs = np.argsort(-freq_magnitudes)[:5]
    print(f"Top 5 dominant frequencies: {dominant_freqs}")
    
    # Detect QRS complexes using peak detection; example threshold
    distance = sampling_rate * 0.6  # average human heart beat is every 0.6 seconds
    peaks, _ = find_peaks(input_data, distance=distance)
    print(f"Detected {len(peaks)} QRS complexes.")

inspection(input_data, sampling_rate=500)

### Index 1 ###
def solver(input_data, sampling_rate=None):
    # Fill missing values (for simplicity, using forward fill)
    input_data = np.where(np.isnan(input_data), np.nanmean(input_data), input_data)
    
    # Parameters for peak detection (based on typical ECG characteristics)
    distance = sampling_rate * 0.6  # in samples

    # Detect QRS complexes using peak detection
    peaks, _ = find_peaks(input_data, distance=distance)
    
    # Calculate bpm
    num_beats = len(peaks)
    total_time_in_minutes = len(input_data) / (sampling_rate * 60)  # Total time in minutes
    bpm = num_beats / total_time_in_minutes

    return bpm

# Call the solver function to obtain the bpm
result_bpm = solver(input_data, sampling_rate=500)
print(result_bpm)

### Index 2 ###
### Index 3 ###
