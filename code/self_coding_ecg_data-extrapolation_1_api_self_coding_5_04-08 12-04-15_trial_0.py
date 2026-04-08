### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is valid
    if output_data is None or len(output_data) == 0:
        return False
    # Check for missing values
    if np.any(np.isnan(output_data)):
        return False
    # Check for range (assuming ECG values might have limitations, but range depends on input specifics, here check for arbitrary large/small numbers)
    if np.any(output_data > 1e6) or np.any(output_data < -1e6):
        return False
    return True

inspection(input_data=None, output_data=np.array([-0.06254498, -0.06258045, -0.06102735, -0.06459711, -0.06482576, -0.06357855,
                                                 -0.06359452, -0.06338228, -0.06338383, -0.06368548, -0.06370111, -0.0636313,
                                                 -0.06361011, -0.06357914, -0.06358597, -0.06361094, -0.06361447, -0.06361091,
                                                 -0.0636072, -0.06360368, -0.06360442, -0.06360652, -0.06360714, -0.06360702,
                                                 -0.06360656, -0.06360618, -0.06360623, -0.06360641, -0.0636065, -0.0636065,
                                                 -0.06360645, -0.06360641, -0.06360641, -0.06360643, -0.06360644, -0.06360644,
                                                 -0.06360644, -0.06360643, -0.06360643, -0.06360643, -0.06360643, -0.06360644,
                                                 -0.06360643, -0.06360643, -0.06360643, -0.06360643, -0.06360643, -0.06360643,
                                                 -0.06360643, -0.06360643]), sampling_rate=50)

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    
    # Calculate the standard deviation of both input and output to compare the variability
    input_std = np.std(input_data)
    output_std = np.std(output_data)
    
    # Check if the predicted values show a realistic pattern with similar variability to the input
    # If the output values have significantly lower or higher dispersion, that could be a potential issue.
    if output_std < 0.5 * input_std or output_std > 1.5 * input_std:
        return False
    
    # Additionally, check if the output continues the trend observed in the input
    input_trend = np.mean(np.diff(input_data))
    output_trend = np.mean(np.diff(output_data))
    
    # Compare the trend of input and output signals
    if np.sign(input_trend) != np.sign(output_trend):
        return False
        
    return True

### Index 2 ###
