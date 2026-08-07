class RemoveDuplicates:
    def __init__(self, numbers):
        self.numbers = numbers

    def remove_duplicates(self):
        return list(set(self.numbers))