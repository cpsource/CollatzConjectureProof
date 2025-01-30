import numpy as np
from collections import Counter
import math

def analyze_binary_string(binary_str):
    N = len(binary_str)
    count_ones = binary_str.count("1")
    count_zeros = binary_str.count("0")
    
    # Shannon Entropy
    p1 = count_ones / N
    p0 = count_zeros / N
    entropy = - (p1 * math.log2(p1) if p1 > 0 else 0) - (p0 * math.log2(p0) if p0 > 0 else 0)

    # Runs
    runs = [len(r) for r in binary_str.replace("01", "0 1").replace("10", "1 0").split()]
    avg_run_length = np.mean(runs)
    max_run_length = np.max(runs)

    # Transition probability
    transitions_0_to_1 = sum(1 for i in range(N-1) if binary_str[i] == '0' and binary_str[i+1] == '1')
    transitions_1_to_0 = sum(1 for i in range(N-1) if binary_str[i] == '1' and binary_str[i+1] == '0')

    prob_0_to_1 = transitions_0_to_1 / count_zeros if count_zeros > 0 else 0
    prob_1_to_0 = transitions_1_to_0 / count_ones if count_ones > 0 else 0

    # Print results
    print(f"Length: {N}")
    print(f"1's Frequency: {p1:.3f}, 0's Frequency: {p0:.3f}")
    print(f"Shannon Entropy: {entropy:.3f}")
    print(f"Average Run Length: {avg_run_length:.2f}, Max Run Length: {max_run_length}")
    print(f"P(0 → 1): {prob_0_to_1:.3f}, P(1 → 0): {prob_1_to_0:.3f}")

# Example usage:
binary_string = "10101100011010001011010"
analyze_binary_string(binary_string)

