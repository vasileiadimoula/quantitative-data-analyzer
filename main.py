from data_loader import load_data
from analysis import (
    calculate_mean,
    calculate_median,
    calculate_variance,
    calculate_standard_deviation,
    calculate_range,
    detect_outliers
)
from visualization import plot_data, plot_histogram, plot_boxplot
def analyze_data(numbers):
    print("\n--- DATA ANALYSIS REPORT ---")
    print("Count:", len(numbers))
    print("Mean:", calculate_mean(numbers))
    print("Median:", calculate_median(numbers))
    print("Variance:", calculate_variance(numbers))
    print("Standard Deviation:", calculate_standard_deviation(numbers))
    minimum, maximum, data_range = calculate_range(numbers)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Range:", data_range)
    print("Outliers:", detect_outliers(numbers))
def main():
    try:
        numbers = load_data("data.csv")
        analyze_data(numbers)
        plot_data(numbers)
        plot_histogram(numbers)
        plot_boxplot(numbers)
    except FileNotFoundError:
        print("Error: The file 'data.csv' was not found.")
    except ValueError as error:
        print(f"Error: {error}")
if __name__ == "__main__":
    main()