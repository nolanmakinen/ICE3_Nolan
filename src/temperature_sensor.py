import statistics

def validate_temperature(value):
    try:
        temp = float(value)  # Convert to float
        if temp < -50 or temp > 150:
            raise ValueError("Out-of-bound value detected.")  # Error for out-of-range values
        return temp  # Return valid temperature
    except ValueError:  # This will catch non-numeric and out-of-range errors
        try:
            float(value)  # Try to convert again to check if it's numeric
        except ValueError:
            raise ValueError("Invalid input detected.")  # Non-numeric input is invalid
        raise ValueError("Out-of-bound value detected.")  # Out-of-range values

def process_temperatures(temp_list):
    if not temp_list:
        return "No input provided."

    valid_temps = []

    try:
        for temp in temp_list:
            valid_temps.append(validate_temperature(temp))  # Validate each input
    except ValueError as e:
        return str(e)

    # Implement custom logic for min() and max()
    min_temp = valid_temps[0]
    max_temp = valid_temps[0]

    # Find max_temp first
    for temp in valid_temps[1:]:
        if temp > max_temp:
            max_temp = temp

    # Find min_temp
    min_temp = max_temp = valid_temps[0]  # Start with the first element

    for temp in valid_temps[1:]:
        if temp < min_temp:
            min_temp = temp
        if temp > max_temp:
            max_temp = temp

    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"
