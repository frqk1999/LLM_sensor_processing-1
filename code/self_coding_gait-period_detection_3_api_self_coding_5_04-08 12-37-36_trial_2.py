### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
        # Check for the validity of output_data by inspecting its range, emptiness, and missing values.
        return output_data.size > 0 and np.isfinite(output_data).all()

### Index 1 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check for the validity of output_data by inspecting its range, emptiness, and missing values.
    return output_data.size > 0 and np.isfinite(output_data).all()

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
    
    # Convert dominant frequencies to periods (in frames based on sampling rate)
    dominant_periods_in_frames = sampling_rate / dominant_freqs
    
    # Check if estimated period matches a dominant period within a certain tolerance
    estimated_period = output_data[0]
    tolerance = 5  # Allow a small tolerance for variability in frames
    
    # Determine if any dominant period is close to the calculated estimated period
    period_match = any(np.isclose(dominant_period, estimated_period, atol=tolerance) for dominant_period in dominant_periods_in_frames)
    
    return period_match

### Index 3 ###
