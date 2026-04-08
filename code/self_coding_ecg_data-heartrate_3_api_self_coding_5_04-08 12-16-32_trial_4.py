### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values. 
    # Args:
    #   input_data: The data type is numpy.ndarray. The input ECG time series data.
    #   output_data: The data type is numpy.ndarray or scalar, representing the calculated bpm.
    #   sampling_rate: The sampling rate of the data.
    if output_data is None or np.isnan(output_data):
        return False  # Output is not valid (None or NaN found)
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=500):
    import numpy as np
    from scipy.signal import find_peaks

    # Detect peaks representing QRS complexes
    distance = sampling_rate * 0.6  # in samples (assuming at least 0.6 seconds between heartbeats)
    peaks, properties = find_peaks(input_data, distance=distance)

    # Calculate BPM based on detected peaks
    num_beats_calculated = len(peaks)
    total_time_in_minutes = len(input_data) / (sampling_rate * 60)
    calculated_bpm = num_beats_calculated / total_time_in_minutes

    # A tolerance check for the calculated bpm to be close to the output bpm
    tolerance = 5
    if not (calculated_bpm - tolerance <= output_data <= calculated_bpm + tolerance):
        return False

    # Check if detected peaks are prominent enough
    height_threshold = np.mean(input_data) + 0.5 * np.std(input_data)
    peak_heights = input_data[peaks]
    
    # Ensure each detected peak is above a certain minimum threshold to consider it a QRS complex
    if not np.all(peak_heights > height_threshold):
        return False

    return True

### Index 2 ###
