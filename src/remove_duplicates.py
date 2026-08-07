class RemoveDuplicates:
    def __init__(self, numbers):
        """Initialize the object with the given numbers."""
        self.numbers = numbers

    def validate_input(self):
        if not isinstance(self.numbers, list):
            raise TypeError('Input must be a list.')

    def remove_duplicates(self):
        unique_numbers = []

        for value in self.numbers:
            if value not in unique_numbers:
                unique_numbers.append(value)

        return unique_numbers

    def display_result(self):
        unique_numbers = self.remove_duplicates()
        print("Original list:", self.numbers)
        print("Unique list:", unique_numbers)


def main():
    numbers = [10, 20, 10, 30, 40, 20, 50, 30]

    try:
        obj = RemoveDuplicates(numbers)
        obj.validate_input()
        obj.display_result()

    except TypeError as e:
        print("Error:", e)


if __name__ == '__main__':
    main()