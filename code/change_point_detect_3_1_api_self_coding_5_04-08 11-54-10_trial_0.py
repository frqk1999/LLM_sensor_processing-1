### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import pandas as pd
    import ruptures as rpt
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the data.")
    else:
        print("No missing values detected.")
    
    # Detect change points
    algo = rpt.Pelt(model="rbf").fit(input_data)
    result = algo.predict(pen=10)
    
    # Print the detected change points
    print("Detected change points at positions:", result[:-1])

### Index 1 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import pandas as pd
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the data.")
    else:
        print("No missing values detected.")
    
    # Use statistical methods to find potential change points
    # Convert to rolling windows to inspect for changes
    window_size = 50
    means = pd.Series(input_data).rolling(window=window_size).mean()
    stds = pd.Series(input_data).rolling(window=window_size).std()
    
    # Define thresholds for changes (e.g., significant deviation in mean or std)
    mean_threshold = means.std()
    std_threshold = stds.std()
    
    # Identify points where changes exceed thresholds
    change_points = np.where((np.abs(means.diff().fillna(0)) > mean_threshold) & 
                             (np.abs(stds.diff().fillna(0)) > std_threshold))[0]
    
    # Display change points
    print("Detected change points at positions:", change_points)

### Index 2 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import pandas as pd
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the data.")
    else:
        print("No missing values detected.")

    # Use rolling windows to inspect changes
    window_size = max(20, len(input_data) // 10)  # Use a fraction of the data size for more sensitivity
    means = pd.Series(input_data).rolling(window=window_size).mean().dropna()
    stds = pd.Series(input_data).rolling(window=window_size).std().dropna()

    # Dynamically calculating threshold based on overall signal metrics
    mean_threshold = means.max() - means.min()
    std_threshold = 2 * stds.mean()  # Use a more lenient measure
    
    # Identify points where changes in mean or std exceed thresholds;
    # Consider any significant deviations as potential change points
    change_points = np.where((np.abs(means.diff().fillna(0)) > mean_threshold) | 
                             (np.abs(stds.diff().fillna(0)) > std_threshold))[0]
    
    # Display change points
    print("Detected change points at positions:", change_points)

### Index 3 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import pandas as pd

    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the data.")
        return
    else:
        print("No missing values detected.")

    # Detect change points using cumulative sum (CUSUM)
    def detect_cusum(data, threshold, drift=0):
        import numpy as np

        # Initialize variables
        s_pos, s_neg = 0, 0
        change_indices = []

        # Loop over the data
        for i in range(1, len(data)):
            value = data[i] - data[i - 1]
            s_pos = max(0, s_pos + value - drift)
            s_neg = min(0, s_neg + value + drift)

            if s_pos > threshold:
                change_indices.append(i)
                s_pos = 0
            elif s_neg < -threshold:
                change_indices.append(i)
                s_neg = 0

        return change_indices

    # Parameters for CUSUM
    threshold = np.std(input_data) * 0.5  # Sensitivity level
    drift = 0.01 * np.std(input_data)

    change_points = detect_cusum(input_data, threshold, drift)
    print("Detected change points at positions:", change_points)

### Index 4 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the data.")
        return
    else:
        print("No missing values detected.")

    # Detect change points using cumulative sum (CUSUM)
    def detect_cusum(data, threshold, drift=0):
        import numpy as np

        # Initialize variables
        s_pos, s_neg = 0, 0
        change_indices = []

        # Loop over the data
        for i in range(1, len(data)):
            value = data[i] - data[i - 1]
            s_pos = max(0, s_pos + value - drift)
            s_neg = min(0, s_neg + value + drift)

            if s_pos > threshold:
                change_indices.append(i)
                s_pos = 0
            elif s_neg < -threshold:
                change_indices.append(i)
                s_neg = 0

        # Filter out closely spaced change points
        filtered_changes = []
        if change_indices:
            filtered_changes.append(change_indices[0])
            for i in range(1, len(change_indices)):
                if change_indices[i] - filtered_changes[-1] > 10:  # Keep only more distant changes
                    filtered_changes.append(change_indices[i])

        return filtered_changes

    # Parameters for CUSUM
    threshold = np.std(input_data)  # Sensitivity level
    drift = 0.05 * np.std(input_data)

    change_points = detect_cusum(input_data, threshold, drift)
    print("Detected change points at positions:", change_points)

### Index 5 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    
    # Detect change points using cumulative sum (CUSUM)
    def detect_cusum(data, threshold, drift=0):
        import numpy as np

        # Initialize variables
        s_pos, s_neg = 0, 0
        change_indices = []

        # Loop over the data
        for i in range(1, len(data)):
            value = data[i] - data[i - 1]
            s_pos = max(0, s_pos + value - drift)
            s_neg = min(0, s_neg + value + drift)

            if s_pos > threshold:
                change_indices.append(i)
                s_pos = 0
            elif s_neg < -threshold:
                change_indices.append(i)
                s_neg = 0

        # Filter out closely spaced change points
        filtered_changes = []
        if change_indices:
            filtered_changes.append(change_indices[0])
            for i in range(1, len(change_indices)):
                if change_indices[i] - filtered_changes[-1] > 10:  # Keep only more distant changes
                    filtered_changes.append(change_indices[i])

        return filtered_changes

    # Parameters for CUSUM
    threshold = np.std(input_data)  # Sensitivity level
    drift = 0.05 * np.std(input_data)

    change_points = detect_cusum(input_data, threshold, drift)
    return change_points

### Index 6 ###
### Index 7 ###
