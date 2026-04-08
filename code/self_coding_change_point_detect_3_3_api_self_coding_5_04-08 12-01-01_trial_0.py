### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    if output_data.size == 0:
        return False
    if np.isnan(output_data).any():
        return False
    if np.any(output_data < 0) or np.any(output_data >= input_data.shape[0]):
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import ttest_ind

    # Edge case where no change points are detected
    if output_data.size == 0:
        return False

    # Convert change points to list and prepend 0 and append length of input_data to handle edge sections
    change_points = [0] + list(output_data) + [len(input_data)]
    
    # Validate changes in subsets among change points
    significant_changes = 0
    for i in range(len(change_points) - 1):
        segment1 = input_data[change_points[i]:change_points[i+1]]
        for j in range(i+1, len(change_points) - 1):
            segment2 = input_data[change_points[j]:change_points[j+1]]
            t_stat, p_value = ttest_ind(segment1, segment2, equal_var=False)
            
            # Check if the statistical test indicates significant change (taking alpha = 0.05)
            if p_value < 0.05:
                significant_changes += 1
                break

    # Ensure a number of segments detected show significant differences
    if significant_changes >= len(output_data) / 2:  # At least half should be significantly different
        return True
    return False

### Index 2 ###
