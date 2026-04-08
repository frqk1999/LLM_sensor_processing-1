### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values. 
    if output_data is None or len(output_data) == 0:
        return False
    if np.any(np.isnan(output_data)):
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import zscore

    # Calculate z-scores of the input_data
    z_scores = zscore(input_data)

    # Define a threshold for considering a point as an outlier, typically a z-score beyond ¡À3 is considered an outlier
    outlier_threshold = 3

    # Identify outlier positions based on z-scores
    expected_outlier_positions = np.where(np.abs(z_scores) > outlier_threshold)[0]

    # Determine if the calculated outlier positions match the detected ones
    detected_positions_set = set(output_data)
    expected_positions_set = set(expected_outlier_positions)

    # Check if all detected outliers are in the expected positions
    if detected_positions_set.issubset(expected_positions_set):
        return True

    return False

### Index 2 ###
