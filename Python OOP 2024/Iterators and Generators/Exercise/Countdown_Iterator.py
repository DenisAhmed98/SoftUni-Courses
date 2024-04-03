class countdown_iterator:
    def __init__(self, number) -> None:
        self.number = number
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number >= 0:
            i = self.number
            self.number -= 1
            return i
        else:
            raise StopIteration



iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")