### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.
    # Check if the output_data has the valid range, is empty, or contains missing values.

    # Check if output_data is non-empty
    if len(output_data) == 0:
        return False

    # Check for missing values in output_data
    if np.isnan(output_data).any():
        return False

    # Check if output_data has valid range - Since it represents indices, it must be non-negative and less than the length of input_data
    if np.any(output_data < 0) or np.any(output_data >= len(input_data)):
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    import pandas as pd
    from scipy.stats import zscore

    # Create a time series from the input data
    input_series = pd.Series(input_data)

    # Calculate the z-score for each data point
    z_scores = np.abs(zscore(input_series))

    # We can manually check the output_data representing indices for anomalies
    threshold = 3  # the same threshold was used in the solver

    # Check if the output_data corresponds to z-scores that are above the threshold
    for position in output_data:
        if z_scores[position] <= threshold:
            return False  

    return True

### Index 2 ###
