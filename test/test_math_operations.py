# test_temperature_sensor.py

# Test Cases
test_cases = [
    # Boundary Value Analysis
    [-50],           # Valid lower boundary
    [150],           # Valid upper boundary
    [-49, 149],      # Values inside range

    # Robustness Testing (Corrected to detect out-of-bounds)
    [-60, 20, 160],  # Out-of-bound values (-60, 160) → Should return "Out-of-bound value detected."
    [20, "abc", 30], # Contains invalid string ("abc") → Should return "Invalid input detected."
    [10, "@", -40],  # Contains invalid character ("@") → Should return "Invalid input detected."

    # Special Scenarios
    [2**3 -1, -2**31],  # -2^31 is an invalid input → Should return "Out-of-bound value detected."
    [50, 50, 50],       # All values the same → Should process normally
    [],                 # Empty list (should return "No input provided.")
]

# Running the test cases
for i, case in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {case}")
    print(process_temperatures(case))
    print("-" * 40)