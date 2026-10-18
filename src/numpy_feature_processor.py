import numpy as np


class NumpyFeatureProcessor:
    """Process numerical data using NumPy."""

    def __init__(self, data):
        self.data = data
        self.array = None
        self.min_max_data = None
        self.standardized_data = None

    def validate_input(self):
        """Validate that input is a non-empty list of numbers."""
        if not isinstance(self.data, list):
            raise TypeError("Input must be a Python list.")

        if len(self.data) == 0:
            raise ValueError("Input list cannot be empty.")

        for value in self.data:
            if isinstance(value, (bool, np.bool_)):
                raise ValueError("Dataset contains non-numeric values.")

            if not isinstance(value, (int, float, np.integer, np.floating)):
                raise ValueError("Dataset contains non-numeric values.")

            if not np.isfinite(value):
                raise ValueError("Dataset must contain only finite numbers.")

        return True

    def convert_to_array(self):
        """Convert the original list into a NumPy array."""
        self.validate_input()
        self.array = np.array(self.data, dtype=float)
        return self.array

    def _ensure_array(self):
        """Validate and create the array if it does not exist."""
        if self.array is None:
            self.convert_to_array()

    def get_array_info(self):
        """Return and display NumPy array properties."""
        self._ensure_array()

        info = {
            "array": self.array,
            "dtype": self.array.dtype,
            "ndim": self.array.ndim,
            "shape": self.array.shape,
            "size": self.array.size,
        }

        print("\nNumPy Array:")
        print(self.array)
        print(f"Data Type: {self.array.dtype}")
        print(f"Dimensions: {self.array.ndim}")
        print(f"Shape: {self.array.shape}")
        print(f"Size: {self.array.size}")

        return info

    def calculate_minimum(self):
        self._ensure_array()
        return np.min(self.array)

    def calculate_maximum(self):
        self._ensure_array()
        return np.max(self.array)

    def calculate_mean(self):
        self._ensure_array()
        return np.mean(self.array)

    def calculate_standard_deviation(self):
        self._ensure_array()
        return np.std(self.array)

    def min_max_scale(self):
        """Scale values into the range 0 to 1."""
        self._ensure_array()

        minimum = np.min(self.array)
        maximum = np.max(self.array)

        if maximum == minimum:
            raise ValueError(
                "Min-Max scaling is not possible because all values are equal."
            )

        self.min_max_data = (
            (self.array - minimum) / (maximum - minimum)
        )

        return self.min_max_data

    def standardize(self):
        """Apply Z-score standardization."""
        self._ensure_array()

        mean = np.mean(self.array)
        standard_deviation = np.std(self.array)

        if standard_deviation == 0:
            raise ValueError(
                "Z-Score standardization is not possible because "
                "standard deviation is zero."
            )

        self.standardized_data = (
            (self.array - mean) / standard_deviation
        )

        return self.standardized_data

    def display_report(self):
        """Display the complete feature-processing report."""
        self.validate_input()
        self._ensure_array()

        print("\n" + "=" * 58)
        print("          NUMPY FEATURE PROCESSING REPORT")
        print("=" * 58)

        print("\nOriginal Data:")
        print(self.data)

        self.get_array_info()

        print(f"\nMinimum: {self.calculate_minimum():g}")
        print(f"Maximum: {self.calculate_maximum():g}")
        print(f"Mean: {self.calculate_mean():g}")
        print(
            "Standard Deviation: "
            f"{self.calculate_standard_deviation():.4f}"
        )

        try:
            scaled = self.min_max_scale()
            print("\nMin-Max Scaled:")
            print(np.round(scaled, 2))
        except ValueError as error:
            print(f"\nMin-Max Scaling Error: {error}")

        try:
            standardized = self.standardize()
            print("\nZ-Score Standardized:")
            print(np.round(standardized, 4))
        except ValueError as error:
            print(f"\nZ-Score Standardization Error: {error}")

        print("\n" + "=" * 58)

    def compare_scaling_methods(self):
        """Display original values and both scaling results."""
        self._ensure_array()

        scaled = self.min_max_scale()
        standardized = self.standardize()

        print("\nSCALING METHODS COMPARISON")
        print("-" * 65)
        print(
            f"{'Original Value':>15} | "
            f"{'Min-Max Value':>15} | "
            f"{'Z-Score Value':>15}"
        )
        print("-" * 65)

        for original, min_max, z_score in zip(
            self.array, scaled, standardized
        ):
            print(
                f"{original:15.4f} | "
                f"{min_max:15.4f} | "
                f"{z_score:15.4f}"
            )

        print("-" * 65)
        print("\nBonus Challenge Explanations:")
        print("1. Min-Max scaling transforms values into the range 0 to 1.")
        print("2. Z-Score standardization centers values around zero.")
        print("3. The standardized data has mean approximately zero.")
        print(
            "4. Scaling can help algorithms compare features "
            "on different numerical scales."
        )


def run_test_case(title, data):
    """Run one dataset test and report success or failure."""
    print(f"\n\nTEST CASE: {title}")
    print("-" * 58)

    try:
        processor = NumpyFeatureProcessor(data)
        processor.validate_input()
        processor.convert_to_array()
        processor.display_report()
        print("Test completed.")
    except (TypeError, ValueError) as error:
        print(f"Expected/Handled Error: {error}")


def main():
    """Run the main report and all six test cases."""
    data = [10, 20, 30, 40, 50]

    try:
        obj = NumpyFeatureProcessor(data)
        obj.validate_input()
        obj.convert_to_array()
        obj.display_report()
        obj.compare_scaling_methods()
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")

    run_test_case("1 - Normal Dataset", [10, 20, 30, 40, 50])
    run_test_case("2 - Negative Values", [-10, -5, 0, 5, 10])
    run_test_case("3 - Decimal Values", [1.5, 2.5, 3.5, 4.5])
    run_test_case("4 - Constant Dataset", [100, 100, 100])
    run_test_case("5 - Invalid Dataset", [10, 20, "30", 40])
    run_test_case("6 - Empty Dataset", [])


if __name__ == "__main__":
    main()