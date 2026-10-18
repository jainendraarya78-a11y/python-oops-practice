class FrequencyCounter:
    def __init__(self, data):
        self.data = data

    def count_frequency(self):
        frequency = {}

        for item in self.data:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

        return frequency

    def display(self):
        print("Original List :", self.data)
        print("Frequency     :", self.count_frequency())


if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 1, 5, 4, 2, 5, 5]

    counter = FrequencyCounter(numbers)
    counter.display()