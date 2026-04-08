### Index 0 ###
import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu, skew, kurtosis

def inspection(input_data, sampling_rate=None):
    # Identify potential change points using a sliding window approach
    window_size = max(20, len(input_data) // 50)  # Adaptive window size
    change_points = []
    
    for i in range(window_size, len(input_data) - window_size):
        # Define two segments of the data
        segment_1 = input_data[i-window_size:i]
        segment_2 = input_data[i:i+window_size]
        
        # Calculate statistical properties
        mean_1, mean_2 = np.mean(segment_1), np.mean(segment_2)
        variance_1, variance_2 = np.var(segment_1), np.var(segment_2)
        skewness_1, skewness_2 = skew(segment_1), skew(segment_2)
        kurt_1, kurt_2 = kurtosis(segment_1), kurtosis(segment_2)
        
        # Perform statistical tests
        _, p_value_ttest = ttest_ind(segment_1, segment_2, equal_var=False)
        _, p_value_mannwhitney = mannwhitneyu(segment_1, segment_2)
        
        # Check if there is a significant change
        if (p_value_ttest < 0.05 or p_value_mannwhitney < 0.05) and (
            abs(mean_1 - mean_2) > 0.5 or abs(variance_1 - variance_2) > 0.5 or
            abs(skewness_1 - skewness_2) > 0.5 or abs(kurt_1 - kurt_2) > 0.5):
            change_points.append(i)
    
    # Deduplicate close change points
    change_points = np.unique(change_points)
    print("Detected change points indices:", change_points)

def solver(input_data, sampling_rate=None):
    # Reuse and refine the change point detection logic from inspection
    window_size = max(20, len(input_data) // 50)  # Adaptive window size
    change_points = []
    
    for i in range(window_size, len(input_data) - window_size):
        # Define two segments of the data
        segment_1 = input_data[i-window_size:i]
        segment_2 = input_data[i:i+window_size]
        
        # Calculate statistical properties
        mean_1, mean_2 = np.mean(segment_1), np.mean(segment_2)
        variance_1, variance_2 = np.var(segment_1), np.var(segment_2)
        skewness_1, skewness_2 = skew(segment_1), skew(segment_2)
        kurt_1, kurt_2 = kurtosis(segment_1), kurtosis(segment_2)
        
        # Perform statistical tests
        _, p_value_ttest = ttest_ind(segment_1, segment_2, equal_var=False)
        _, p_value_mannwhitney = mannwhitneyu(segment_1, segment_2)
        
        # Check if there is a significant change
        if (p_value_ttest < 0.05 or p_value_mannwhitney < 0.05) and (
            abs(mean_1 - mean_2) > 0.5 or abs(variance_1 - variance_2) > 0.5 or
            abs(skewness_1 - skewness_2) > 0.5 or abs(kurt_1 - kurt_2) > 0.5):
            change_points.append(i)
    
    # Deduplicate close change points
    change_points = np.unique(change_points)
    return change_points

### Index 1 ###
### Index 2 ###
