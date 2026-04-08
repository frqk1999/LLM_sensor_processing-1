### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    # Args:
    #   input_data: numpy.ndarray
    #   output_data: numpy.ndarray
    #   sampling_rate: optional
    # Output: boolean
  
    if output_data.size == 0:
        return False
    if not np.all((output_data >= 0) & (output_data < len(input_data))):
        return False
    if np.isnan(output_data).any():
        return False

    return True

# Let's assume that this function is being run, and we'll proceed based on its result.

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import ttest_ind

    # Check if each detected change point corresponds to a significant change in signal properties
    segment_length = 50  # This is assumed from previous context

    # Iterate through the detected change points
    for change_point in output_data:
        # Define segments around each change point
        start_prev = max(0, change_point - segment_length)
        end_prev = change_point
        start_next = change_point
        end_next = min(len(input_data), change_point + segment_length)

        segment_prev = input_data[start_prev:end_prev]
        segment_next = input_data[start_next:end_next]

        # Perform statistical tests (e.g., t-test for means, and F-test for variances)
        _, p_value_mean = ttest_ind(segment_prev, segment_next, equal_var=False)
        
        # Significance level
        alpha = 0.05
        
        # We consider a change point valid if there's a statistically significant difference in mean
        if p_value_mean >= alpha:
            return False

    return True

### Index 2 ###
