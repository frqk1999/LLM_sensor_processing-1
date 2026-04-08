### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is a single numeric (scalar) value and is not empty or containing missing values.
    if output_data.size != 1:
        return False
    if np.isnan(output_data).any():
        return False
    return True

# Invoke the inspection function to check for initial validity
inspection_result = inspection(None, output_data=[0.85333333])

### Index 1 ###
def inspection(input_data, output_data, sampling_rate=None):
    import numpy as np
    
    # Convert the output_data to a NumPy array first
    output_data = np.array(output_data)
    
    # Check if the output_data is a single numeric (scalar) value and is not empty or containing missing values.
    if output_data.size != 1:
        return False
    if np.isnan(output_data).any():
        return False
    return True

# Perform the inspection
inspection_result = inspection(None, output_data=[0.85333333])

### Index 2 ###
def challenger(input_data, output_data, sampling_rate=300):
    import numpy as np
    from scipy.signal import welch
    
    # Calculate power spectral density to find dominant frequencies
    freqs, psd = welch(input_data, fs=sampling_rate)
    
    # Identify indices of the top 3 dominant frequencies
    dominant_freq_indices = np.argsort(psd)[-3:]
    
    # Retrieve corresponding dominant frequencies
    dominant_freqs = freqs[dominant_freq_indices]
    
    # Convert dominant frequencies to periods in seconds
    dominant_periods = 1 / dominant_freqs
    
    # Check if the estimated period matches any dominant period within a certain tolerance
    estimated_period = output_data[0]
    tolerance = 0.05  # Allow small tolerance for variability in seconds
    
    # Verify if any dominant period is close to the estimated period
    period_match = any(np.isclose(dominant_period, estimated_period, atol=tolerance) for dominant_period in dominant_periods)
    
    return period_match

# Example usage for verification
challenger_result = challenger(input_data, output_data=[0.85333333], sampling_rate=300)

### Index 3 ###
