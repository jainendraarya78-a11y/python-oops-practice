class MissingValueHandler:
    """Analyze and handle missing values in a dataset."""

    def __init__(self, data):
        self.data = data
        self.cleaned_data = None

    def validate_input(self):
        """Validate the dataset."""
        if not isinstance(self.data, list):
            raise TypeError("Input must be a list.")

        if len(self.data) == 0:
            raise ValueError("Input list cannot be empty.")

        for value in self.data:
            if value is not None:
                if isinstance(value, bool) or not isinstance(value, (int, float)):
                    raise ValueError("Dataset contains invalid values.")

        return True

    def find_missing_indexes(self):
        """Return indexes of missing values."""
        self.validate_input()

        indexes = []

        for index, value in enumerate(self.data):
            if value is None:
                indexes.append(index)

        return indexes

    def count_missing_values(self):
        """Count missing values."""
        return len(self.find_missing_indexes())

    def get_available_values(self):
        """Return values excluding None."""
        self.validate_input()

        available_values = []

        for value in self.data:
            if value is not None:
                available_values.append(value)

        return available_values

    def calculate_mean(self):
        """Calculate mean manually."""
        available_values = self.get_available_values()

        if len(available_values) == 0:
            raise ValueError(
                "Cannot calculate mean because all values are missing."
            )

        total = 0

        for value in available_values:
            total += value

        return total / len(available_values)

    def fill_with_mean(self):
        """Replace missing values with the mean."""
        mean_value = self.calculate_mean()

        self.cleaned_data = []

        for value in self.data:
            if value is None:
                self.cleaned_data.append(mean_value)
            else:
                self.cleaned_data.append(value)

        return self.cleaned_data

    def calculate_median(self):
        """Calculate median manually."""
        available_values = self.get_available_values()

        if len(available_values) == 0:
            raise ValueError(
                "Cannot calculate median because all values are missing."
            )

        sorted_values = sorted(available_values)
        count = len(sorted_values)
        middle = count // 2

        if count % 2 == 1:
            return sorted_values[middle]

        return (
            sorted_values[middle - 1] + sorted_values[middle]
        ) / 2

    def fill_with_median(self):
        """Replace missing values with the median."""
        median_value = self.calculate_median()

        self.cleaned_data = []

        for value in self.data:
            if value is None:
                self.cleaned_data.append(median_value)
            else:
                self.cleaned_data.append(value)

        return self.cleaned_data

    def fill_with_zero(self):
        """Replace missing values with zero."""
        self.cleaned_data = []

        for value in self.data:
            if value is None:
                self.cleaned_data.append(0)
            else:
                self.cleaned_data.append(value)

        return self.cleaned_data

    def fill_missing_values(self, strategy="mean"):
        """Fill missing values using the selected strategy."""
        if strategy == "mean":
            return self.fill_with_mean()

        elif strategy == "median":
            return self.fill_with_median()

        elif strategy == "zero":
            return self.fill_with_zero()

        else:
            raise ValueError(
                "Invalid strategy. Choose 'mean', 'median', or 'zero'."
            )

    def display_report(self):
        """Display the missing value report."""
        self.validate_input()

        missing_indexes = self.find_missing_indexes()
        available_values = self.get_available_values()

        print("=" * 40)
        print("       MISSING VALUE REPORT")
        print("=" * 40)

        print("\nOriginal Data:")
        print(self.data)

        print(f"\n{'Total Values':<20}: {len(self.data)}")
        print(f"{'Missing Values':<20}: {len(missing_indexes)}")
        print(f"{'Missing Indexes':<20}: {missing_indexes}")
        print(f"{'Available Values':<20}: {len(available_values)}")

        if not available_values:
            raise ValueError(
                "Cannot clean dataset because all values are missing."
            )

        mean_value = self.calculate_mean()
        print(f"{'Mean':<20}: {mean_value}")

        self.fill_missing_values("mean")

        print("\nCleaned Data:")
        print(self.cleaned_data)

        print("\n" + "=" * 40)


def main():
    """Run the program and test all six cases."""

    print("TEST CASE 1: Normal Missing Values")

    try:
        data = [25, 30, None, 40, None, 35, 28]
        obj = MissingValueHandler(data)

        obj.validate_input()
        obj.display_report()

        print("\nOriginal data preserved:", obj.data)

    except (TypeError, ValueError) as error:
        print("Error:", error)

    print("\nTEST CASE 2: No Missing Values")

    try:
        obj = MissingValueHandler([10, 20, 30, 40])
        obj.validate_input()
        obj.display_report()

    except (TypeError, ValueError) as error:
        print("Error:", error)

    print("\nTEST CASE 3: All Values Missing")

    try:
        obj = MissingValueHandler([None, None, None])
        obj.validate_input()
        obj.display_report()

    except (TypeError, ValueError) as error:
        print("Error:", error)

    print("\nTEST CASE 4: Empty Dataset")

    try:
        obj = MissingValueHandler([])
        obj.validate_input()
        obj.display_report()

    except (TypeError, ValueError) as error:
        print("Error:", error)

    print("\nTEST CASE 5: Invalid Value")

    try:
        obj = MissingValueHandler([10, 20, "30", None])
        obj.validate_input()
        obj.display_report()

    except (TypeError, ValueError) as error:
        print("Error:", error)

    print("\nTEST CASE 6: Negative Values")

    try:
        obj = MissingValueHandler([-10, -20, None, -30])
        obj.validate_input()
        obj.display_report()

    except (TypeError, ValueError) as error:
        print("Error:", error)

    print("\nBONUS CHALLENGE")

    try:
        bonus_data = [10, 20, None, 40, None]
        bonus_obj = MissingValueHandler(bonus_data)

        print("Original Data:", bonus_obj.data)
        print("Mean Imputation:",
              bonus_obj.fill_missing_values("mean"))
        print("Median Imputation:",
              bonus_obj.fill_missing_values("median"))
        print("Zero Imputation:",
              bonus_obj.fill_missing_values("zero"))

        print("Original Data After Imputation:", bonus_obj.data)

    except (TypeError, ValueError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
