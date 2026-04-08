### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the provided output_data is within the valid range of input indices.
    if output_data is None or len(output_data) == 0:
        return False
    if np.isnan(output_data).any():
        return False
    if (output_data < 0).any() or (output_data >= len(input_data)).any():
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import iqr

    # Define dynamic thresholds using median and IQR (Interquartile Range)
    data_median = np.median(input_data)
    data_iqr = iqr(input_data)

    # Outliers can be outside of 1.5 * IQR from the 1st and 3rd quartiles
    lower_bound = data_median - 1.5 * data_iqr
    upper_bound = data_median + 1.5 * data_iqr

    # Detect positions where data falls outside the bounds
    dynamic_outlier_positions = np.where((input_data < lower_bound) | (input_data > upper_bound))[0]

    # Compare detected outliers with output_data positions
    detected_positions_set = set(output_data)
    dynamic_positions_set = set(dynamic_outlier_positions)

    # Check for overlap and align with the revised plan
    if detected_positions_set.issubset(dynamic_positions_set):
        return True

    return False

### Index 2 ###
