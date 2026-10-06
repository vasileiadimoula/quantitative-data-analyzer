import matplotlib.pyplot as plt
def plot_data(numbers):
    plt.plot(numbers, marker="o")
    plt.title("Quantitative Data Analysis")
    plt.xlabel("Observation")
    plt.ylabel("Value")
    plt.grid()
    plt.savefig("line_plot.png")
    plt.show()
def plot_histogram(numbers):
    plt.hist(numbers, bins=10)
    plt.title("Data Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig("histogram.png")
    plt.show()
def plot_boxplot(numbers):
    plt.boxplot(numbers)
    plt.title("Box Plot - Outlier Detection")
    plt.ylabel("Value")
    plt.savefig("box_plot.png")
    plt.show()
