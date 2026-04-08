### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values. 
    if output_data.size == 0 or np.isnan(output_data).any():
        return False
    if output_data.max() > 5 or output_data.min() < 0.5:  # Check plausible step period range
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    import scipy.signal as signal

    # Use autocorrelation to verify the periodicity of the input data.
    autocorr = np.correlate(input_data, input_data, mode='full')
    autocorr = autocorr[autocorr.size // 2:]
    peaks, _ = signal.find_peaks(autocorr, distance=sampling_rate/2)
    
    if len(peaks) < 1:
        return False  # No periodicity detected if no peaks found in autocorrelation

    # Derive estimated period from first peak for reference
    periods = np.diff(peaks) / sampling_rate
    average_period = np.mean(periods)
    
    # Compare derived period with output_data
    if np.abs(output_data[0] - average_period) > 0.2:  # within reasonable error margin
        return False

    return True

### Index 2 ###
