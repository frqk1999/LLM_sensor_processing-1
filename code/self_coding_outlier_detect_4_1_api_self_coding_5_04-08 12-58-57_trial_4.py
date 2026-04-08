### Index 0 ###
import numpy as np

def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is empty or contains missing values
    if output_data is None or len(output_data) == 0:
        return False
    if np.any(np.isnan(output_data)):
        return False
    
    # Check that output_data values are within the range of input_data indices
    if np.min(output_data) < 0 or np.max(output_data) >= len(input_data):
        return False
    
    return True

# Assume the inspection function was executed

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import zscore

    # Calculate z-scores of the input_data
    z_scores = zscore(input_data)

    # Define a threshold for considering a point as an outlier
    outlier_threshold = 3

    # Identify outlier positions based on the threshold
    expected_outlier_positions = np.where(np.abs(z_scores) > outlier_threshold)[0]

    # Compare detected positions with expected outlier positions
    detected_positions_set = set(output_data)
    expected_positions_set = set(expected_outlier_positions)

    # Check if all detected outliers are in the expected positions
    if detected_positions_set.issubset(expected_positions_set):
        return True

    return False

# Assume the challenger function was executed

### Index 2 ###
