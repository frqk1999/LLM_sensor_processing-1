### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values.
    if output_data.size == 0:
        return False  # Output is empty

    if np.any(np.isnan(output_data)):
        return False  # Contains missing values

    # In the context of this problem, output_data should only contain a single delay value.
    if output_data.shape != (1,):
        return False  # The output must be a scalar inside a numpy array

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import correlate
  
    # Decompose the stacked array
    left_foot_signal = input_data[0]
    right_foot_signal = input_data[1]
  
    # Cross-correlate signals to validate the delay
    correlation = correlate(left_foot_signal, right_foot_signal, mode='full')
    lags = np.arange(-len(left_foot_signal) + 1, len(right_foot_signal))
    peak_lag = lags[np.argmax(correlation)]
  
    # Convert lag to time (seconds)
    computed_delay_seconds = peak_lag / sampling_rate
    
    # Compare the challenge result to output_data
    return np.allclose(computed_delay_seconds, output_data[0], atol=1e-2)

### Index 2 ###
