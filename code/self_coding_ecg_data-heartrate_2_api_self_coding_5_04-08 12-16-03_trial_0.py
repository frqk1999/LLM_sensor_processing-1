### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    import numpy as np
    
    # 1) Check if the output_data is within a valid range for bpm. Typically, a valid human heart rate is between 40 bpm to 180 bpm at rest.
    if not (40 <= output_data <= 180):
        return False
    
    # 2) Check if output_data is empty or contains missing values
    if np.isnan(output_data):
        return False

    # If all checks are passed
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import find_peaks, iirnotch, filtfilt

    # Apply a notch filter to remove 50 Hz interference for accurate peak detection
    notch_freq = 50.0  # Frequency to be removed from the signal (Hz)
    quality_factor = 30.0  # Quality factor for the notch filter
    b_notch, a_notch = iirnotch(notch_freq, quality_factor, sampling_rate)
    filtered_data = filtfilt(b_notch, a_notch, input_data)

    # Detect R-peaks with a minimum distance to ensure independent heart beats
    distance = int(sampling_rate * 0.6)  # Calculate minimum distance between R-peaks: minimum human heart rate is ~40 bpm
    peaks, _ = find_peaks(filtered_data, distance=distance)
    
    # Validate if we have enough peaks to calculate a reliable rr_intervals and bpm
    if len(peaks) < 2:
        return False

    # Compute RR intervals and BPM
    rr_intervals = np.diff(peaks) / sampling_rate  # Convert intervals from samples to seconds
    computed_bpm = 60.0 / np.mean(rr_intervals)

    # Check if calculated BPM based on challenge is within 5% tolerance of output_data
    if not (0.95 * output_data <= computed_bpm <= 1.05 * output_data):
        return False

    return True

### Index 2 ###
