### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import ruptures as rpt
    
    # Normalize the input data for more consistent results in change detection
    data = (input_data - np.mean(input_data)) / np.std(input_data)
    
    # Using Ruptures to detect change points with change in distribution
    algo = rpt.Pelt(model="rbf").fit(data)
    change_points = algo.predict(pen=10)  # The penalty can be adjusted based on sampling rate and specific needs
    
    print("Detected change points at indices:", change_points[:-1])

### Index 1 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import pandas as pd
    from scipy.stats import kstest
    
    # Normalize the data for consistent results
    data = (input_data - np.mean(input_data)) / np.std(input_data)

    # Window size for sliding statistics (e.g., mean, variance)
    window_size = 30  # Example window size; this might need to be adjusted based on data characteristics
    step = 5  # Step size for each segment

    mean_changes = []
    var_changes = []
    p_value_threshold = 0.05  # Threshold for detecting a significant change

    # Sliding window analysis
    for i in range(0, len(data) - window_size, step):
        segment = data[i:i+window_size]
        mean_segment = np.mean(segment)
        var_segment = np.var(segment)

        if i > 0:
            # Check changes in mean and variance
            if abs(mean_segment - mean_changes[-1]) > 0.5 or abs(var_segment - var_changes[-1]) > 0.5:
                print(f"Potential change in trend detected between indices {i} and {i+window_size}")

        # Kolmogorov-Smirnov Test for distribution changes
        if i >= window_size * 2:  # Ensure enough data for meaningful statistics
            prev_segment = data[i-window_size:i]
            _, p_value = kstest(segment, prev_segment)
            if p_value < p_value_threshold:
                print(f"Potential distribution change detected between indices {i} and {i+window_size}")

        mean_changes.append(mean_segment)
        var_changes.append(var_segment)

### Index 2 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import kstest

    # Normalize the input data for consistency
    data = (input_data - np.mean(input_data)) / np.std(input_data)
    
    window_size = 30
    step = 5
    p_value_threshold = 0.05

    change_positions = []

    for i in range(0, len(data) - window_size, step):
        segment = data[i:i+window_size]

        if i >= window_size * 2:
            prev_segment = data[i-window_size:i]
            _, p_value = kstest(segment, prev_segment)
            if p_value < p_value_threshold and (not change_positions or i - change_positions[-1] >= window_size):
                change_positions.append(i)

    return change_positions

### Index 3 ###
### Index 4 ###
