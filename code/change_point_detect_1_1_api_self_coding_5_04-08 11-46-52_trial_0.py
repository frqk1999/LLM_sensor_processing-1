### Index 0 ###
import numpy as np
import ruptures as rpt

def inspection(input_data, sampling_rate=None):
    # 1) Check for periodicity: using autocorrelation or Fourier transform
    print("Checking for periodicity in the signal...")
    fft_result = np.fft.fft(input_data)
    frequencies = np.fft.fftfreq(len(input_data))
    dominant_freq = np.argmax(np.abs(fft_result))
    if fft_result[dominant_freq] > 1:  # if any frequency component is significantly present
        print(f"The signal is periodic with a dominant frequency: {frequencies[dominant_freq]}")
    else:
        print("The signal is non-periodic.")
    
    # 2) Check the trend by differencing
    print("Checking for trend in the signal...")
    diff_data = np.diff(input_data)
    if np.mean(diff_data) > 0:
        print("The signal has an increasing trend.")
    elif np.mean(diff_data) < 0:
        print("The signal has a decreasing trend.")
    else:
        print("The signal does not have any noticeable trend.")
    
    # 3) Check for unwanted frequencies (noise)
    print("Checking for unwanted frequency components...")
    if np.std(diff_data) / np.std(input_data) > 0.5:
        print("The signal might have unwanted frequency components indicating noise.")
    else:
        print("No significant noise detected in frequency components.")
    
    # 4) Check for missing values
    print("Checking for missing values...")
    if np.isnan(input_data).any():
        print("The signal has missing values.")
    else:
        print("No missing values in the signal.")

### Index 1 ###
import numpy as np

def inspection(input_data, sampling_rate=None):
    # 1) Checking for periodicity
    print("Checking for periodicity in the signal...")
    fft_result = np.fft.fft(input_data)
    magnitudes = np.abs(fft_result)
    frequencies = np.fft.fftfreq(len(input_data))
    dominant_freq_idx = np.argmax(magnitudes)
    if magnitudes[dominant_freq_idx] > np.mean(magnitudes):
        print(f"The signal seems periodic with a dominant frequency: {frequencies[dominant_freq_idx]}")
    else:
        print("The signal is non-periodic.")
    
    # 2) Checking the trend
    print("Checking for trend in the signal...")
    diff_data = np.diff(input_data)
    if np.mean(diff_data) > 0:
        print("The signal has an increasing trend.")
    elif np.mean(diff_data) < 0:
        print("The signal has a decreasing trend.")
    else:
        print("The signal does not have any noticeable trend.")
    
    # 3) Checking for unwanted frequencies (noise)
    print("Checking for unwanted frequency components...")
    noise_threshold = 0.5
    if np.std(diff_data) / np.std(input_data) > noise_threshold:
        print("The signal might have unwanted frequency components indicating noise.")
    else:
        print("No significant noise detected in the frequency components.")
    
    # 4) Checking for missing values
    print("Checking for missing values...")
    if np.isnan(input_data).any():
        print("The signal has missing values.")
    else:
        print("No missing values in the signal.")

### Index 2 ###
def solver(input_data, sampling_rate=None):
    # Using a simple window-based method to detect abrupt changes in the mean
    window_size = 50  # This can be adjusted depending on signal characteristics
    change_points = []
    
    previous_mean = np.mean(input_data[:window_size])
    
    for i in range(window_size, len(input_data)):
        current_window = input_data[i-window_size:i]
        current_mean = np.mean(current_window)
        
        # Define a threshold for significant change
        if np.abs(current_mean - previous_mean) > np.std(input_data) * 0.5:
            change_points.append(i)
            previous_mean = current_mean  # Update the previous mean
    
    print("Detected change points at positions:", change_points)
    return np.array(change_points)

### Index 3 ###
### Index 4 ###
