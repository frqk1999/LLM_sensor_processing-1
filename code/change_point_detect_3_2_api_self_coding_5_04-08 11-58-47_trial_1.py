### Index 0 ###
### Index 1 ###
import numpy as np

def inspection(input_data, sampling_rate=None):
    # Check basic properties and prepare for analysis
    if not isinstance(input_data, np.ndarray):
        print("Input data must be a numpy array.")
        return
    
    # Check for NaN values
    nan_count = np.isnan(input_data).sum()
    print(f"Number of NaN values in the data: {nan_count}")
    
    # Check if large fluctuations suggest periodicity or noise
    fft_result = np.fft.fft(input_data)
    power = np.abs(fft_result) ** 2
    dominant_freqs = np.argsort(power)[-3:]  # Top 3 frequency components
    print(f"Dominant frequencies (by index): {dominant_freqs}")
    
    # Trend analysis via central difference
    trend = np.mean(input_data[1:] - input_data[:-1])
    print(f"Average trend: {trend}")

def solver(input_data, sampling_rate=None):
    if not isinstance(input_data, np.ndarray):
        raise ValueError("Input data must be a numpy array.")
        
    # Parameters for CUSUM
    window_size = 50  # Window size for dynamic threshold
    threshold = np.std(input_data) * 2  # Initial threshold
    
    change_points = []
    mean_shift = 0
    start_mean = np.mean(input_data[:window_size])
    
    for i in range(window_size, len(input_data)):
        current_mean = np.mean(input_data[i-window_size:i])
        mean_shift += current_mean - start_mean
        
        # Cumulative sum for change detection
        if abs(mean_shift) > threshold:
            change_points.append(i)
            # Reset mean shift after detecting a change
            start_mean = current_mean
            mean_shift = 0
            
    return np.array(change_points)

### Index 2 ###
### Index 3 ###
