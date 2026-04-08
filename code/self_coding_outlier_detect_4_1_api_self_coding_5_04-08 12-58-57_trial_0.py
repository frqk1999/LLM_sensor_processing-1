### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.
    if output_data is None or len(output_data) == 0:
        return False

    # Check if output_data has values within the expected range
    # Validate that the values in output_data are non-negative integers
    if (output_data < 0).any():
        return False

    # Check for missing values
    if np.isnan(output_data).any():
        return False

    # Ensure that the indices are within the bounds of the input_data
    if np.any(output_data >= len(input_data)):
        return False

    return True

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

    # Compare expected outliers to the solver's output
    matched_outliers = np.in1d(output_data, expected_outlier_positions)

    # Check if detected outliers match expected outliers
    if len(output_data) == len(expected_outlier_positions) and matched_outliers.all():
        return True
    
    return False

### Index 2 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import zscore

    # Calculate z-scores of the input_data
    z_scores = zscore(input_data)

    # Define a threshold for considering a point as an outlier
    outlier_threshold = 3

    # Identify outlier positions based on the threshold
    expected_outlier_positions = np.where(np.abs(z_scores) > outlier_threshold)[0]

    # Compare expected outliers to the solver's output
    matched_outliers = np.isin(output_data, expected_outlier_positions)

    # Check if detected outliers match expected outliers
    if len(output_data) == len(expected_outlier_positions) and matched_outliers.all():
        return True
    
    return False

### Index 3 ###
