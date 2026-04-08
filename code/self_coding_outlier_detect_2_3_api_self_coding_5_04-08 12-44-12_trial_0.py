### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data:
    # 1) Contains valid values (e.g., non-negative indices within the bounds of input_data).
    # 2) Is empty or with any invalid range.
    
    if output_data is None or len(output_data) == 0:
        return False
    
    # Check if all indices are within range of input_data
    if np.any(output_data < 0) or np.any(output_data >= len(input_data)):
        return False
    
    return True

### Index 1 ###
from scipy.stats import zscore

def challenger(input_data, output_data, sampling_rate=None):
    # Calculate z-scores for the entire dataset
    z_scores = zscore(input_data)
    
    # Set a z-score threshold (e.g., |z| > 3) for statistical significance
    threshold = 3
    
    # Find positions where |z-score| exceeds the threshold
    significant_anomalies = np.where(np.abs(z_scores) > threshold)[0]
    
    # Compare detected output positions with significant anomalies
    detected_anomalies = set(output_data)
    actual_significant_anomalies = set(significant_anomalies)
    
    # Check if detected anomalies are consistent with statistical tests
    # Ensuring all detected anomalies are indeed significant
    if not detected_anomalies.issubset(actual_significant_anomalies):
        return False
    
    # Check for excessive false negatives - ensure some anomalies are detected
    if len(detected_anomalies) < 1:
        return False
    
    return True

### Index 2 ###
