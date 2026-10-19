import numpy as np


class NumpyDatasetAnalyzer:
    """Analyze a 2D dataset using NumPy."""

    def __init__(self, data):
        self.validate_input(data)
        self.array = np.array(data, dtype=float)

    def validate_input(self, data):
        if data is None:
            raise ValueError("Dataset cannot be empty.")

        array = np.asarray(data)

        if array.size == 0:
            raise ValueError("Dataset cannot be empty.")

        if array.ndim != 2:
            raise ValueError("Dataset must be a 2D array.")

        if not np.issubdtype(array.dtype, np.number):
            raise ValueError("Dataset must contain only numbers.")

        if not np.all(np.isfinite(array)):
            raise ValueError("Dataset contains invalid values.")

        return True

    def convert_to_array(self, data):
        self.validate_input(data)
        return np.array(data, dtype=float)

    def get_dataset_info(self):
        return {
            "rows": self.array.shape[0],
            "columns": self.array.shape[1],
            "shape": self.array.shape,
            "data_type": str(self.array.dtype)
        }

    def get_column(self, column_index):
        if column_index < 0 or column_index >= self.array.shape[1]:
            raise IndexError("Invalid column index.")

        return self.array[:, column_index]

    def get_row(self, row_index):
        if row_index < 0 or row_index >= self.array.shape[0]:
            raise IndexError("Invalid row index.")

        return self.array[row_index, :]

    def calculate_column_mean(self):
        return np.mean(self.array, axis=0)

    def calculate_column_minimum(self):
        return np.min(self.array, axis=0)

    def calculate_column_maximum(self):
        return np.max(self.array, axis=0)

    def calculate_column_std(self):
        return np.std(self.array, axis=0)

    def scale_features(self):
        minimum = np.min(self.array, axis=0)
        maximum = np.max(self.array, axis=0)

        difference = maximum - minimum
        difference[difference == 0] = 1

        return (self.array - minimum) / difference

    def feature_summary(self):
        return {
            "mean": self.calculate_column_mean(),
            "minimum": self.calculate_column_minimum(),
            "maximum": self.calculate_column_maximum(),
            "standard_deviation": self.calculate_column_std()
        }

    def split_features_target(self, target_index=-1):
        if target_index < 0:
            target_index += self.array.shape[1]

        if target_index < 0 or target_index >= self.array.shape[1]:
            raise IndexError("Invalid target column index.")

        X = np.delete(self.array, target_index, axis=1)
        y = self.array[:, target_index]

        return X, y

    def display_report(self):
        print("\n" + "=" * 55)
        print("       NUMPY 2D DATASET ANALYZER REPORT")
        print("=" * 55)

        print("\n1. Original Dataset:")
        print(self.array)

        print("\n2. Dataset Information:")
        print(self.get_dataset_info())

        print("\n3. Column Means:")
        print(self.calculate_column_mean())

        print("\n4. Column Minimums:")
        print(self.calculate_column_minimum())

        print("\n5. Column Maximums:")
        print(self.calculate_column_maximum())

        print("\n6. Column Standard Deviations:")
        print(self.calculate_column_std())

        print("\n7. Scaled Features:")
        print(self.scale_features())

        print("\n8. Feature Summary:")
        print(self.feature_summary())

        X, y = self.split_features_target()

        print("\n9. Features (X):")
        print(X)

        print("\n10. Target (y):")
        print(y)

        print("\n" + "=" * 55)


def main():
    data = [
        [25, 30000, 2],
        [30, 45000, 5],
        [35, 60000, 8],
        [40, 80000, 12],
        [45, 100000, 15]
    ]

    analyzer = NumpyDatasetAnalyzer(data)
    analyzer.display_report()


if __name__ == "__main__":
    main()