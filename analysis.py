import numpy as np
def validate_numbers(numbers):
    if not numbers:
        raise ValueError("The data cannot be empty.")
def calculate_mean(numbers):
    validate_numbers(numbers)
    mean = sum(numbers) / len(numbers)
    return(mean)
def calculate_median(numbers):
    validate_numbers(numbers)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    return median
def calculate_variance(numbers):
    validate_numbers(numbers)
    mean = calculate_mean(numbers)
    squared_differences = []
    for number in numbers:
        difference = number - mean
        squared_difference = difference ** 2
        squared_differences.append(squared_difference)
    variance = sum(squared_differences) / len(numbers)
    return variance
def calculate_standard_deviation(numbers):
    validate_numbers(numbers)
    variance = calculate_variance(numbers)
    standard_deviation = variance ** 0.5
    return standard_deviation
def calculate_range(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    data_range = maximum - minimum
    return minimum, maximum, data_range
def detect_outliers(numbers):
    validate_numbers(numbers)
    q1 = np.percentile(numbers, 25)
    q3 = np.percentile(numbers, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = []
    for number in numbers:
        if number < lower_bound or number > upper_bound:
            outliers.append(number)
    return outliers