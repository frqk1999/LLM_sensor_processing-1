### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data is valid
    if output_data is None or len(output_data) == 0:
        return False  # Check if the output_data is not empty.
        
    # Check for missing or invalid values
    if np.any(np.isnan(output_data)) or np.any(np.isinf(output_data)):
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np

    # Calculate the mean and standard deviation of the input and output data
    input_mean = np.mean(input_data)
    input_std = np.std(input_data)
    
    output_mean = np.mean(output_data)
    output_std = np.std(output_data)
    
    # Define a tolerance level for prediction magnitude ('reasonable range' could be within 2 standard deviations)
    tolerance = 2
    
    # Check if the predicted values are within the tolerance range of the original data
    mean_check = abs(output_mean - input_mean) <= tolerance * input_std
    std_check = abs(output_std - input_std) <= tolerance * input_std
    
    return mean_check and std_check

### Index 2 ###
