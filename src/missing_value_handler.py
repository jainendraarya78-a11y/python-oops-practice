class MissingValueHandler:

    def __init__(self, data):
        self.original_data = data.copy() if isinstance(data, list) else data
        self.data = data.copy() if isinstance(data, list) else data

    def validate_input(self):
        if not isinstance(self.data, list):
            raise TypeError("Input must be a list.")

        if len(self.data) == 0:
            raise ValueError("Input list cannot be empty.")

        for value in self.data:
            if value is not None and not isinstance(value, (int, float)):
                raise TypeError("Dataset contains invalid values.")

    def find_missing_indexes(self):
        missing_indexes = []

        for index in range(len(self.data)):
            if self.data[index] is None:
                missing_indexes.append(index)

        return missing_indexes

    def count_missing_values(self):
        return len(self.find_missing_indexes())

    def get_available_values(self):
        available_values = []

        for value in self.data:
            if value is not None:
                available_values.append(value)

        return available_values

    def calculate_mean(self):
        available_values = self.get_available_values()

        if len(available_values) == 0:
            raise ValueError("No valid values exist to calculate the mean.")

        total = 0

        for value in available_values:
            total += value

        return total / len(available_values)

    def fill_with_mean(self):
        mean = self.calculate_mean()
        cleaned_data = self.data.copy()

        for index in range(len(cleaned_data)):
            if cleaned_data[index] is None:
                cleaned_data[index] = mean

        return cleaned_data

    def fill_with_median(self):
        available_values = self.get_available_values()

        if len(available_values) == 0:
            raise ValueError("No valid values exist to calculate the median.")

        sorted_values = sorted(available_values)
        n = len(sorted_values)
        middle = n // 2

        if n % 2 == 1:
            median = sorted_values[middle]
        else:
            median = (sorted_values[middle - 1] + sorted_values[middle]) / 2

        cleaned_data = self.data.copy()

        for index in range(len(cleaned_data)):
            if cleaned_data[index] is None:
                cleaned_data[index] = median

        return cleaned_data

    def fill_with_zero(self):
        cleaned_data = self.data.copy()

        for index in range(len(cleaned_data)):
            if cleaned_data[index] is None:
                cleaned_data[index] = 0

        return cleaned_data

    def fill_missing_values(self, strategy):
        if strategy == "mean":
            return self.fill_with_mean()

        elif strategy == "median":
            return self.fill_with_median()

        elif strategy == "zero":
            return self.fill_with_zero()

        else:
            raise ValueError(
                "Invalid strategy. Use 'mean', 'median', or 'zero'."
            )

    def display_report(self):
        self.validate_input()

        missing_indexes = self.find_missing_indexes()
        missing_count = len(missing_indexes)
        available_values = self.get_available_values()

        print()
        print("========================================")
        print("       MISSING VALUE REPORT")
        print("========================================")
        print()
        print("Original Data:")
        print(self.original_data)
        print()
        print(f"Total Values       : {len(self.data)}")
        print(f"Missing Values     : {missing_count}")
        print(f"Missing Indexes    : {missing_indexes}")
        print(f"Available Values   : {len(available_values)}")

        if missing_count > 0:
            mean = self.calculate_mean()
            print(f"Mean               : {mean}")

            cleaned_data = self.fill_with_mean()

            print()
            print("Cleaned Data:")
            print(cleaned_data)

        else:
            print()
            print("Cleaned Data:")
            print(self.data.copy())

        print()
        print("========================================")


def main():

    print("\nTEST CASE 1 - Normal Missing Values")

    data1 = [25, 30, None, 40, None, 35, 28]

    handler1 = MissingValueHandler(data1)
    handler1.display_report()


    print("\nTEST CASE 2 - No Missing Values")

    data2 = [10, 20, 30, 40]

    handler2 = MissingValueHandler(data2)
    handler2.display_report()


    print("\nTEST CASE 3 - All Values Missing")

    data3 = [None, None, None]

    try:
        handler3 = MissingValueHandler(data3)
        handler3.display_report()

    except ValueError as error:
        print("Error:", error)


    print("\nTEST CASE 4 - Empty Dataset")

    data4 = []

    try:
        handler4 = MissingValueHandler(data4)
        handler4.display_report()

    except ValueError as error:
        print("Error:", error)


    print("\nTEST CASE 5 - Invalid Value")

    data5 = [10, 20, "30", None]

    try:
        handler5 = MissingValueHandler(data5)
        handler5.display_report()

    except TypeError as error:
        print("Error:", error)


    print("\nTEST CASE 6 - Negative Values")

    data6 = [-10, -20, None, -30]

    handler6 = MissingValueHandler(data6)
    handler6.display_report()


    print("\nBONUS - Different Imputation Strategies")

    bonus_data = [10, 20, None, 40, None]

    bonus_handler = MissingValueHandler(bonus_data)

    print("Original Data:", bonus_data)
    print("Mean:", bonus_handler.fill_missing_values("mean"))
    print("Median:", bonus_handler.fill_missing_values("median"))
    print("Zero:", bonus_handler.fill_missing_values("zero"))


if __name__ == "__main__":
    main()