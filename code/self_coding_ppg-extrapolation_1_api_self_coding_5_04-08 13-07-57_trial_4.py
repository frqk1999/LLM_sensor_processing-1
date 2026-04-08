### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values.
    
    # Check if the output_data is empty
    if output_data.size == 0:
        return False
    
    # Check if the output_data contains any NaN or Inf values
    if np.isnan(output_data).any() or np.isinf(output_data).any():
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np

    # Ensure input_data is available and handle it correctly
    if input_data is None or input_data.size == 0:
        return False
    
    # Calculate statistics of the input data
    input_mean = np.mean(input_data)
    input_std = np.std(input_data)
    
    # Check if the predicted values are within a reasonable range of the last known input values
    last_value = input_data[-1]
    max_reasonable_value = last_value + 3 * input_std
    min_reasonable_value = last_value - 3 * input_std

    # Check the range and smooth progression of predictions
    in_range_check = np.all(output_data >= min_reasonable_value) and np.all(output_data <= max_reasonable_value)
    progression_check = np.all(np.diff(output_data) <= input_std)

    return in_range_check and progression_check

### Index 2 ###
