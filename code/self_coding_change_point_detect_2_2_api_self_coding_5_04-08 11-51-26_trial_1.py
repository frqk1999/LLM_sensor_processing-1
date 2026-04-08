### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data
    # 1) Check if the output_data has the valid range, is empty, or contains missing values.
    if output_data.size == 0:
        return False
    if np.any(np.isnan(output_data)):
        return False
    return True

### Index 1 ###
