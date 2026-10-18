class StatisticalAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def validate_input(self):
        if not isinstance(self.numbers, list):
            raise TypeError("Input must be a list.")

        if len(self.numbers) == 0:
            raise ValueError("Input list cannot be empty.")

        for number in self.numbers:
            if isinstance(number, bool) or not isinstance(number, (int, float)):
                raise ValueError(
                    "Input must contain only numerical values."
                )

        return True

    def calculate_mean(self):
        self.validate_input()
        return sum(self.numbers) / len(self.numbers)

    def calculate_median(self):
        self.validate_input()

        sorted_numbers = sorted(self.numbers)
        size = len(sorted_numbers)
        middle = size // 2

        if size % 2 == 1:
            return sorted_numbers[middle]

        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    def calculate_mode(self):
        self.validate_input()

        frequencies = {}

        for number in self.numbers:
            frequencies[number] = frequencies.get(number, 0) + 1

        highest_frequency = max(frequencies.values())

        if highest_frequency == 1:
            return None

        modes = []

        for number, frequency in frequencies.items():
            if frequency == highest_frequency:
                modes.append(number)

        return modes

    def find_minimum(self):
        self.validate_input()
        return min(self.numbers)

    def find_maximum(self):
        self.validate_input()
        return max(self.numbers)

    def count_unique_values(self):
        self.validate_input()
        return len(set(self.numbers))

    def calculate_range(self):
        self.validate_input()
        return self.find_maximum() - self.find_minimum()

    def calculate_variance(self):
        self.validate_input()

        mean = self.calculate_mean()
        total = 0

        for number in self.numbers:
            total += (number - mean) ** 2

        return total / len(self.numbers)

    def display_result(self):
        self.validate_input()

        mean = self.calculate_mean()
        median = self.calculate_median()
        modes = self.calculate_mode()
        minimum = self.find_minimum()
        maximum = self.find_maximum()
        unique_values = self.count_unique_values()
        data_range = self.calculate_range()
        variance = self.calculate_variance()

        if modes is None:
            mode_result = "No unique mode"
        elif len(modes) == 1:
            mode_result = modes[0]
        else:
            mode_result = modes

        print("=" * 32)
        print("       STATISTICAL REPORT")
        print("=" * 32)
        print(f"Original Data : {self.numbers}")
        print()
        print(f"Mean          : {mean:.2f}")
        print(f"Median        : {median}")
        print(f"Mode          : {mode_result}")
        print(f"Minimum       : {minimum}")
        print(f"Maximum       : {maximum}")
        print(f"Unique Values : {unique_values}")
        print(f"Range         : {data_range}")
        print(f"Variance      : {variance:.2f}")
        print("=" * 32)


def main():
    numbers = [10, 20, 20, 30, 40, 50]

    try:
        analyzer = StatisticalAnalyzer(numbers)
        analyzer.validate_input()
        analyzer.display_result()

    except (TypeError, ValueError) as error:
        print(f"Input Error: {error}")

    except Exception as error:
        print(f"Unexpected Error: {error}")


if __name__ == "__main__":
    main()

