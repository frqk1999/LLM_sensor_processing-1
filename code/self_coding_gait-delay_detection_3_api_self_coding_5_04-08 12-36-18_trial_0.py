### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check for empty output
    if output_data.size == 0:
        return False
    
    # Check for NaN or missing values
    if np.isnan(output_data).any():
        return False
    
    # Check for valid range (assuming valid delay range is small and realistic for walking steps)
    if output_data[0] < 0 or output_data[0] > 1:  # 1 second is a considerable upper limit for human walking delay
        return False
    
    return True

# Execute inspection
inspection_passed = inspection(input_data, output_data, sampling_rate=300)
inspection_passed

### Index 1 ###
import numpy as np

def challenger(input_data, output_data, sampling_rate=None):
    left_foot_data = input_data[0]
    right_foot_data = input_data[1]
    
    # Given peaks from the inspection
    left_peaks = np.array([137, 297, 452, 613, 763, 917, 1078, 1230, 1387, 1547])
    right_peaks = np.array([91, 244, 401, 551, 713, 875, 1027, 1177, 1339, 1544])
    
    # Calculate the time (in seconds) corresponding to each peak
    left_times = left_peaks / sampling_rate
    right_times = right_peaks / sampling_rate
    
    # Calculate actual delays between each pair and check against the computed average
    actual_delays = left_times - right_times
    computed_average_delay = output_data[0]
    
    # Mean of actual delays
    mean_actual_delay = np.mean(actual_delays)
    
    # Checking if the computed delay is close to the actual mean delay
    return np.isclose(mean_actual_delay, computed_average_delay, atol=0.01)

# Execute challenger
challenger_passed = challenger(input_data, output_data, sampling_rate=300)
challenger_passed

### Index 2 ###
