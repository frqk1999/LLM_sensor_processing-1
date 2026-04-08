### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is empty or contains missing values
    if len(output_data) == 0 or np.isnan(output_data).any():
        return False
    return True

### Index 1 ###
