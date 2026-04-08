### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is a scalar value within a plausible range for heart rate
    if output_data is None or np.isnan(output_data):
        return False
    
    # Heart rate should be within a reasonable range for humans
    if not (30 <= output_data <= 220):
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import find_peaks
    
    # Detect peaks representing QRS complexes
    distance = sampling_rate * 0.6  # Here, we assume at least 0.6 seconds between heartbeats, typical at rest.
    peaks, properties = find_peaks(input_data, distance=distance)
    
    # Check 1: Are the detected peaks plausible in number compared to output bpm?
    num_beats_calculated = len(peaks)
    
    # Calculate the time in minutes
    total_time_in_minutes = len(input_data) / (sampling_rate * 60)
    
    # Use the calculated number of peaks to determine bpm
    calculated_bpm = num_beats_calculated / total_time_in_minutes
    
    # A tolerance check for the calculated bpm to be close to the output bpm
    if not (calculated_bpm - 5 <= output_data <= calculated_bpm + 5):
        return False
    
    # Check 2: Are these peaks prominent enough?
    height_threshold = np.mean(input_data) + 0.5 * np.std(input_data)
    peak_heights = input_data[peaks]
    
    # Ensure each detected peak is above a certain minimum threshold to consider it as a QRS complex
    if not np.all(peak_heights > height_threshold):
        return False
    
    return True

### Index 2 ###
