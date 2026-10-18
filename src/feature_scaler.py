class FeatureScaler:
    def __init__(self, data, new_min=0, new_max=1):
        self.data = data
        self.new_min = new_min
        self.new_max = new_max
        self.minimum = None
        self.maximum = None
        self.scaled_data = None

    def validate_input(self):
        if not isinstance(self.data, list):
            raise TypeError("Input must be a list.")        
        if len(self.data) == 0:
            raise ValueError("Input list cannot be empty.")

        for value in self.data:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("Dataset contains invalid values.")

        if not isinstance(self.new_min, (int, float)) or isinstance(self.new_min, bool):
            raise ValueError("Target minimum must be a number.")

        if not isinstance(self.new_max, (int, float)) or isinstance(self.new_max, bool):
            raise ValueError("Target maximum must be a number.")

        if self.new_min >= self.new_max:
            raise ValueError("Target minimum must be less than target maximum.")

        return True
    def find_minimum(self):
        self.validate_input()
        self.minimum = min(self.data)
        return self.minimum

    def find_maximum(self):
        self.validate_input()
        self.maximum = max(self.data)
        return self.maximum

    def scale_data(self):
        self.validate_input()
        minimum = self.find_minimum()
        maximum = self.find_maximum()

        if minimum == maximum:
            raise ValueError(
                "Cannot scale data because all values are identical."
            )

        self.scaled_data = [
            self.new_min
            + ((value - minimum) / (maximum - minimum))
            * (self.new_max - self.new_min)
            for value in self.data
        ]

        return self.scaled_data
    def display_report(self):
        self.scale_data()
        print("=" * 40)
        print("          FEATURE SCALING REPORT")
        print("=" * 40)
        print()
        print(f"Original Data : {self.data}")
        print()
        print(f"Minimum       : {self.minimum}")
        print(f"Maximum       : {self.maximum}")
        print()
        print(f"Target Range  : {self.new_min} to {self.new_max}")
        print(f"Scaled Data   : {self.scaled_data}")
        print()
        print("=" * 40)


def main():
    data = [10, 20, 30, 40, 50]

    try:
        obj = FeatureScaler(data)
        obj.validate_input()
        obj.display_report()

    except (TypeError, ValueError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()