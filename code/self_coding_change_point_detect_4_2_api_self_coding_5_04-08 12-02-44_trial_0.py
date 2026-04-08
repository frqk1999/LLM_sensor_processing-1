### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is empty
    if output_data is None or len(output_data) == 0:
        return False

    # Check for missing values
    if np.any(np.isnan(output_data)):
        return False

    # Check for reasonable range (if there's a specific range expected)
    # For typical numerical data, check if the range is too extreme
    if not np.all(np.isfinite(output_data)):
        return False

    # Additional domain-specific checks can be added if needed
    return True

### Index 1 ###
import numpy as np
from scipy.stats import ttest_ind, f_oneway

def challenger(input_data, output_data, sampling_rate=None):
    # Assuming change points were detected at these indices:
    detected_change_points = [61, 62, 64, 65, 68, 69, 70, 203, 207, 209, 211, 212, 293]

    # Minimum segments to compare ¨C before and after change point
    min_segment_length = 10
    alpha = 0.05  # significance level for statistical test

    significant_changes = []

    for cp in detected_change_points:
        if cp - min_segment_length < 0 or cp + min_segment_length >= len(output_data):
            continue  # Skip points too close to the signal boundaries

        # Segments before and after the change point
        segment_before = output_data[cp-min_segment_length:cp]
        segment_after = output_data[cp:cp+min_segment_length]

        # Perform t-test on means
        t_stat, p_value = ttest_ind(segment_before, segment_after, equal_var=False)

        # Perform F-test on variances
        f_stat, fp_value = f_oneway(segment_before, segment_after)

        if p_value < alpha or fp_value < alpha:
            significant_changes.append(cp)

    # Check if there are significant changes
    return len(significant_changes) > 0

### Index 2 ###
