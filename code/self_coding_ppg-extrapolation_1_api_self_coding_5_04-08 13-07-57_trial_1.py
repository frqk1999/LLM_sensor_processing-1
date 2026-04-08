### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is non-empty and does not contain missing values
    if output_data.size == 0 or np.isnan(output_data).any():
        return False

    # Check if the output_data is within a reasonable range. Assuming PPG values cannot go beyond typical physiological limits.
    if np.min(output_data) < -5 or np.max(output_data) > 5:
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np

    # Ensure input_data is available and handle the last value correctly
    if input_data is None or input_data.size == 0:
        return False
    
    # Check if the predicted values are following the general trend of the input data
    last_value = input_data[-1]
    differences = np.diff(output_data)

    # Analyze the progression of the predicted values
    progression_check = np.all((output_data - last_value <= 2 * np.std(input_data)) & 
                               (output_data - last_value >= -2 * np.std(input_data)))

    # Optional: Should have a monotonous continuation given the decreasing trend detected
    trend_check = np.all(differences <= 0)

    return progression_check and trend_check

### Index 2 ###
