### Index 0 ###
import numpy as np
from scipy.signal import find_peaks, welch

def inspection(input_data, sampling_rate=None):
    # Check if there are NaN values
    if np.isnan(input_data).any():
        print("Missing values detected in the input data.")
    else:
        print("No missing values detected.")
    
    # Analyze each foot data
    left_foot_data = input_data[0]
    right_foot_data = input_data[1]

    # Detecting peaks to analyze step patterns (assuming steps have peaks)
    left_peaks, _ = find_peaks(left_foot_data, distance=sampling_rate//2)
    right_peaks, _ = find_peaks(right_foot_data, distance=sampling_rate//2)
    
    if len(left_peaks) == 0 or len(right_peaks) == 0:
        print("No clear periodic step patterns detected.")
    else:
        print("Detected left foot peaks:", left_peaks)
        print("Detected right foot peaks:", right_peaks)
        print("Number of left steps:", len(left_peaks))
        print("Number of right steps:", len(right_peaks))

    # Frequency analysis (Spectral density to check dominant frequencies)
    f_left, Pxx_left = welch(left_foot_data, fs=sampling_rate)
    f_right, Pxx_right = welch(right_foot_data, fs=sampling_rate)
    
    main_freq_left = f_left[np.argmax(Pxx_left)]
    main_freq_right = f_right[np.argmax(Pxx_right)]
    print(f"Dominant frequency for left foot: {main_freq_left} Hz")
    print(f"Dominant frequency for right foot: {main_freq_right} Hz")

    # Trend analysis can be simple mean level check
    mean_left = np.mean(left_foot_data)
    mean_right = np.mean(right_foot_data)
    print(f"Mean pressure for left foot: {mean_left}")
    print(f"Mean pressure for right foot: {mean_right}")

inspection(input_data, sampling_rate=300)

### Index 1 ###
import numpy as np

def solver(input_data, sampling_rate=None):
    left_foot_data = input_data[0]
    right_foot_data = input_data[1]

    # Given peaks from the inspection
    left_peaks = np.array([137, 297, 452, 613, 763, 917, 1078, 1230, 1387, 1547])
    right_peaks = np.array([91, 244, 401, 551, 713, 875, 1027, 1177, 1339, 1544])

    # Calculate the time (in seconds) corresponding to each peak
    left_times = left_peaks / sampling_rate
    right_times = right_peaks / sampling_rate

    # Calculate delay between each left-right pair
    delays = left_times[:min(len(left_times), len(right_times))] - right_times[:min(len(left_times), len(right_times))]

    # Return the average delay as a scalar in np.ndarray
    average_delay = np.mean(delays)

    return np.array([average_delay])

# This would be used during actual function execution with input_data variable
# processed_output = solver(input_data, sampling_rate=300)

### Index 2 ###
### Index 3 ###
