### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    import numpy as np
    import pandas as pd

    # Check if output_data has valid range, is empty, or contains missing values.
    if output_data is None or len(output_data) == 0:
        return False

    if np.any(pd.isnull(output_data)):
        return False
    
    # Check if output_data has any unrealistic values (such as negative indices)
    if np.any(output_data < 0) or np.any(output_data >= len(input_data)):
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import ttest_ind, f_oneway

    # Initialize flag for successful changes
    change_validation_passed = True
    
    # Iterate over detected change points
    for i in range(1, len(output_data)):
        prev_cp = output_data[i-1]
        current_cp = output_data[i]
        
        # Windows before and after change point
        window_before = input_data[prev_cp:current_cp]
        window_after = input_data[current_cp:current_cp+10]  # Plus window to ensure enough samples
        
        # Perform t-test for mean and F-test for variance
        t_stat, t_p = ttest_ind(window_before, window_after, equal_var=False)
        f_stat, f_p = f_oneway(window_before, window_after)
        
        # If tests are not significant, the change point detection might be invalid
        if t_p >= 0.05 and f_p >= 0.05:  # Using 5% significance level
            change_validation_passed = False
            break

    return change_validation_passed

### Index 2 ###
