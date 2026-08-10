class StatisticalAnalyzer:

    def __init__(self, data):
        self.data = data
        self.validate_input()

    def validate_input(self):
        if not isinstance(self.data, list):
            raise TypeError("Input must be a list.")

        if not all(isinstance(value, (int, float)) and not isinstance(value, bool)
                   for value in self.data):
            raise TypeError("Input must contain only numerical values.")

        if len(self.data) == 0:
            raise ValueError("Input list cannot be empty.")

    def calculate_mean(self):
        return sum(self.data) / len(self.data)

    def calculate_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        middle = n // 2

        if n % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            return sorted_data[middle]

    def calculate_mode(self):
        frequencies = {}

        for value in self.data:
            frequencies[value] = frequencies.get(value, 0) + 1

        maximum_frequency = max(frequencies.values())

        if maximum_frequency == 1:
            return "No mode"

        modes = []

        for value, frequency in frequencies.items():
            if frequency == maximum_frequency:
                modes.append(value)

        if len(modes) == 1:
            return modes[0]

        return modes

    def calculate_min(self):
        return min(self.data)

    def calculate_max(self):
        return max(self.data)

    def calculate_unique(self):
        return len(set(self.data))

    def calculate_range(self):
        return self.calculate_max() - self.calculate_min()

    def calculate_variance(self):
        mean = self.calculate_mean()
        squared_differences = []

        for value in self.data:
            difference = value - mean
            squared_differences.append(difference ** 2)

        return sum(squared_differences) / len(self.data)

    def display_report(self):
        print("\n================================")
        print("       STATISTICAL REPORT")
        print("================================")

        print(f"Original Data : {self.data}")
        print(f"Mean          : {self.calculate_mean():.2f}")
        print(f"Median        : {self.calculate_median()}")
        print(f"Mode          : {self.calculate_mode()}")
        print(f"Minimum       : {self.calculate_min()}")
        print(f"Maximum       : {self.calculate_max()}")
        print(f"Unique Values : {self.calculate_unique()}")
        print(f"Range         : {self.calculate_range()}")
        print(f"Variance      : {self.calculate_variance():.2f}")

        print("================================")


def run_tests():

    print("\n===== TEST CASE 1 =====")
    data1 = [10, 20, 20, 30, 40, 50]
    analyzer1 = StatisticalAnalyzer(data1)
    analyzer1.display_report()

    print("\n===== TEST CASE 2 =====")
    data2 = [10, 20, 30, 40, 50]
    analyzer2 = StatisticalAnalyzer(data2)
    print("Data:", data2)
    print("Median:", analyzer2.calculate_median())

    print("\n===== TEST CASE 3 =====")
    data3 = [10, 20, 30, 40]
    analyzer3 = StatisticalAnalyzer(data3)
    print("Data:", data3)
    print("Median:", analyzer3.calculate_median())

    print("\n===== TEST CASE 4 =====")
    data4 = [10, 10, 20, 20, 30]
    analyzer4 = StatisticalAnalyzer(data4)
    print("Data:", data4)
    print("Modes:", analyzer4.calculate_mode())

    print("\n===== TEST CASE 5 =====")
    data5 = [10, 20, "30", 40]

    try:
        analyzer5 = StatisticalAnalyzer(data5)
        analyzer5.display_report()
    except (TypeError, ValueError) as error:
        print("Error:", error)


if __name__ == "__main__":
    run_tests()