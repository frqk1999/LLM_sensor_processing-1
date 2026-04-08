### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import ruptures as rpt

    # 1. Check for missing values
    if np.isnan(input_data).any():
        print("There are missing values in the input data.")
    else:
        print("No missing values found.")

    # 2. Detect change points using the \'ruptures\' package
    try:
        algo = rpt.Pelt(model="rbf").fit(input_data)
        change_points = algo.predict(pen=10)
        print(f"Detected change points at positions: {change_points}")
    except Exception as e:
        print(f"An error occurred during change point detection: {e}")

# There\'s no need for a sampling rate as the data is not specified to be time-dependent with a specific rate.

### Index 1 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import norm

    # 1. Check for missing values
    if np.isnan(input_data).any():
        print("There are missing values in the input data.")
    else:
        print("No missing values found.")

    # 2. Basic change point detection using statistics
    try:
        # Calculate means and deviations in segments
        segment_length = 100  # length of a segment for detecting changes
        num_segments = len(input_data) // segment_length
        change_points = []

        for i in range(1, num_segments):
            start_prev = (i - 1) * segment_length
            end_prev = i * segment_length
            start_next = i * segment_length
            end_next = (i + 1) * segment_length

            segment_prev = input_data[start_prev:end_prev]
            segment_next = input_data[start_next:end_next]

            mean_prev = np.mean(segment_prev)
            std_prev = np.std(segment_prev)
            mean_next = np.mean(segment_next)

            # Check for significant change in mean
            if np.abs(mean_next - mean_prev) > 1.5 * std_prev:
                change_points.append(start_next)

        print(f"Detected change points at positions: {change_points}")
    except Exception as e:
        print(f"An error occurred during change point detection: {e}")

### Index 2 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import zscore
    from scipy.interpolate import interp1d

    # Step 1: Handle Missing Values
    try:
        if np.isnan(input_data).any():
            # Interpolate to fill missing values
            nan_indices = np.isnan(input_data)
            not_nan_indices = ~nan_indices
            interp_func = interp1d(np.flatnonzero(not_nan_indices), input_data[not_nan_indices], kind=\'linear\', fill_value="extrapolate")
            input_data[nan_indices] = interp_func(np.flatnonzero(nan_indices))
            print("Handled missing values using linear interpolation.")

    except Exception as e:
        print(f"An error occurred when handling missing values: {e}")
        return input_data  # Early return in case of error

    # Step 2: Adjust Detection Parameters and Re-detect Change Points
    try:
        segment_length = 50  # shorter segment length for finer detection
        num_segments = len(input_data) // segment_length
        change_points = []

        for i in range(1, num_segments):
            start_prev = (i - 1) * segment_length
            end_prev = i * segment_length
            start_next = i * segment_length
            end_next = (i + 1) * segment_length if (i + 1) * segment_length < len(input_data) else len(input_data)

            segment_prev = input_data[start_prev:end_prev]
            segment_next = input_data[start_next:end_next]

            mean_prev = np.mean(segment_prev)
            mean_next = np.mean(segment_next)
            std_prev = np.std(segment_prev)

            # Check for significant change in mean
            if np.abs(mean_next - mean_prev) > 1.5 * std_prev:
                change_points.append(start_next)

        print(f"Re-detected change points at positions: {change_points}")
        return np.array(change_points)

    except Exception as e:
        print(f"An error occurred during change point detection: {e}")
        return input_data  # Early return in case of error

### Index 3 ###
### Index 4 ###
