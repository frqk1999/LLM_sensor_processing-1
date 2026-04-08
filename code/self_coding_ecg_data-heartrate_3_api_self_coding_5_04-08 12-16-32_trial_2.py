### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check for valid range: For bpm, a normal range is approximately 40 to 180 in healthy adults.
    if not (40 <= output_data <= 180):
        return False

    # Check for missing values and emptiness
    if np.isnan(output_data) or output_data.size == 0:
        return False

    return True

# Since the valid bpm range is between 40 and 180 bpm and no additional information indicates missing values, if the checks above pass, the output data is considered valid.

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import find_peaks

    # Detect peaks representing QRS complexes
    distance = sampling_rate * 0.6  # Here, we assume at least 0.6 seconds between heartbeats
    
    # Bandpass filter the signal for enhanced QRS detection if not already done in the solver. 
    peaks, properties = find_peaks(input_data, distance=distance)

    # Check 1: Evaluate the possibility of the bpm based on detected peaks
    num_beats_calculated = len(peaks)
    total_time_in_minutes = len(input_data) / (sampling_rate * 60)
    calculated_bpm = num_beats_calculated / total_time_in_minutes

    # Allow a tolerance of +/-5 bpm for the calculated bpm to be close to the output bpm
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
