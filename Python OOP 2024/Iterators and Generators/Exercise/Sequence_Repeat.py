class sequence_repeat:
    def __init__(self, sequence, length) -> None:
        self.sequence = sequence
        self.length = length
        self.start = 0
        self.sequenceCounter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.length:
            if self.sequenceCounter >= len(self.sequence):
                self.sequenceCounter = 0

            symbol = self.sequence[self.sequenceCounter]
            self.sequenceCounter += 1
            self.start += 1
            return symbol
        else:
            raise StopIteration



result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')