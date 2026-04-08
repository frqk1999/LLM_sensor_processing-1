### Index 0 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    import ruptures as rpt

    # Apply the Binary Segmentation method for change point detection
    # We assume the task mainly involves changes in the distribution\'s mean or variance.
    model = "l2"  # "l2" is often used for detecting changes in mean or variance
    algo = rpt.Binseg(model=model)

    # Fit the algorithm to the data
    algo.fit(input_data)

    # Detection of change points
    change_points = algo.predict(n_bkps=10) # Limit to 10 breakpoints for the sake of computational feasibility

    # Return the list of change points
    return change_points

### Index 1 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from statsmodels.tsa.stattools import adfuller

    def detect_change_points(data, window_size, significance):
        change_points = []

        for start in range(0, len(data) - window_size):
            window_data = data[start:start + window_size]
            
            # Perform Augmented Dickey-Fuller test to check stationarity
            result = adfuller(window_data)
            p_value = result[1]

            # If p-value is smaller than significance, we suspect a change point at the end of this window
            if p_value < significance:
                change_points.append(start + window_size)

        # Remove redundant entries by checking if change points are very close
        filtered_points = []
        for i in range(len(change_points)):
            if i == 0 or change_points[i] > change_points[i-1] + window_size:
                filtered_points.append(change_points[i])

        return filtered_points

    # Example configuration
    window_size = 50
    significance_level = 0.05
    
    # Detect change points
    change_point_positions = detect_change_points(input_data, window_size, significance_level)

    return change_point_positions

### Index 2 ###
### Index 3 ###
