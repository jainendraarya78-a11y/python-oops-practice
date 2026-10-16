class RemoveDuplicates:
    """A class to remove duplicate values from a list of numbers."""

    def __init__(self, numbers):
        """Initialize the class with a list of numbers."""
        self.numbers = numbers

    def validate_input(self):
        """Check whether the input is a list."""
        if not isinstance(self.numbers, list):
            raise TypeError("Input must be a list.")

    def remove_duplicates(self):
        """Remove duplicate values while preserving the original order."""
        unique_numbers = []

        for number in self.numbers:
            if number not in unique_numbers:
                unique_numbers.append(number)

        return unique_numbers

    def display_result(self):
        """Display the original list and the list without duplicates."""
        unique_numbers = self.remove_duplicates()

        print("Original List :", self.numbers)
        print("Unique List   :", unique_numbers)


def main():
    """Run the RemoveDuplicates program."""
    numbers = [10, 20, 10, 30, 40, 20, 50, 30]

    try:
        obj = RemoveDuplicates(numbers)
        obj.validate_input()
        obj.display_result()

    except TypeError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()