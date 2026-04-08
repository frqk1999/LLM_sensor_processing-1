### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # 1) Check if the output_data has the valid range, is empty or contains missing values. 
    # 2) Do NOT check the data type - using the isinstance or np.isscalar function is not reliable.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data. sampling_rate is mandatory for speech, ecg, ppg, and gait data. It could be optional for others.
    # Output: boolean variable - True or False. If the result does not pass your test, output False. Else, output True.
    
    if output_data is None or np.isnan(output_data):
        return False
    if output_data < 0 or output_data > 300:
        # Assuming a human feasible heart rate should be between 0 and 300 bpm
        return False
    return True

inspection(input_data, 78.0, sampling_rate=500)

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import find_peaks
    
    # Detect peaks representing QRS complexes
    distance = sampling_rate * 0.6  # in samples
    peaks, properties = find_peaks(input_data, distance=distance)
    
    # Check 1: Are the detected peaks plausible in number compared to output bpm?
    num_beats_calculated = len(peaks)
    total_time_in_minutes = len(input_data) / (sampling_rate * 60)
    calculated_bpm = num_beats_calculated / total_time_in_minutes
    
    # A tolerance check for the calculated bpm to be close to the output bpm
    if not (calculated_bpm - 5 <= output_data <= calculated_bpm + 5):
        return False
    
    # Check 2: Are these peaks prominent enough?
    # Assuming a heuristic thresholding for prominence compared to average peak height
    height_threshold = np.mean(input_data) + 0.5 * np.std(input_data)
    peak_heights = input_data[peaks]
    
    if not np.all(peak_heights > height_threshold):
        return False
    
    return True

### Index 2 ###
