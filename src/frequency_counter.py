class FrequencyCounter:
    def __init__(self, numbers):
        """Initialize the object with the given numbers."""
        self.numbers = numbers

    def validate_input(self):
        if not isinstance(self.numbers, list):
            raise TypeError('Input must be a list.')

        if len(self.numbers) == 0:
            raise ValueError('Input list cannot be empty.')

    def count_frequency(self):
        frequency = {}

        for value in self.numbers:
            if value in frequency:
                frequency[value] += 1
            else:
                frequency[value] = 1

        return frequency

    def display_result(self):
        frequency = self.count_frequency()
        print("Original list:", self.numbers)
        print("Frequency:", frequency)

        print("Original List :", self.numbers)
        print("Frequency      :", frequency)


def main():
    numbers = [1, 2, 2, 3, 1, 5, 4, 2, 5, 5]

    try:
        obj = FrequencyCounter(numbers)
        obj.validate_input()
        obj.display_result()

    except (TypeError, ValueError) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()