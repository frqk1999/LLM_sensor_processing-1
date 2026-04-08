### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values. 
    if output_data < 0 or np.isnan(output_data) or len(output_data) == 0:
        return False
    return True

# Note: In this case, output_data is a single float bpm value, not an array.

### Index 1 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is valid (non-negative and not NaN)
    if output_data < 0 or np.isnan(output_data):
        return False
    return True

### Index 2 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Check if the computed bpm is within a realistic human heart rate range
    # Typically, resting heart rates for adults range from 60 to 100 bpm
    # During intense exercise, rates may go as high as 180-200 bpm for healthy individuals
    # Values significantly outside this range may indicate error.
    
    # Typical human heart rate range during rest and various activities
    min_bpm = 30   # Erroneously low or during sleep
    max_bpm = 200  # Upper limits during intense exercise
    
    if min_bpm <= output_data <= max_bpm:
        return True
    else:
        return False

### Index 3 ###
