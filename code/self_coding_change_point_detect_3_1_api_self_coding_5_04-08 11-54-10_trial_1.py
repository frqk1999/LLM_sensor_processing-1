### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data is a valid list of indices
    if not isinstance(output_data, (list, np.ndarray)) or len(output_data) == 0:
        return False
    
    # Check if indices in output_data are within the bounds of input_data
    if np.any((output_data < 0) | (output_data >= len(input_data))):
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import ttest_ind, levene

    change_points = output_data
    epsilon = 5  # Number of points around change point to consider for comparison

    # Check if any true change in mean or variance around detected change points
    for cp in change_points:
        if cp - epsilon < 0 or cp + epsilon >= len(input_data):
            continue  # Skipping edge cases where comparison is not possible
        
        before_segment = input_data[max(0, cp - 2*epsilon):cp - epsilon]
        after_segment = input_data[cp + epsilon : min(len(input_data), cp + 2*epsilon)]

        # Check for a change in mean using t-test
        t_stat, p_value = ttest_ind(before_segment, after_segment, equal_var=False)
        if p_value >= 0.05:
            return False  # No significant change in mean detected

        # Check for a change in variance using Levene's test
        l_stat, p_value = levene(before_segment, after_segment)
        if p_value >= 0.05:
            return False  # No significant change in variance detected

    return True

### Index 2 ###
