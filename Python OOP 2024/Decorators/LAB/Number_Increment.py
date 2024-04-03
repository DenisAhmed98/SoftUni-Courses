def number_increment(numbers):
    def increase():
        increased = [x + 1 for x in numbers]
        return increased
    return increase()