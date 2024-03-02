class Stack:
    def __init__(self):
        self.data = []

    def push(self, el):
        self.data.append(el)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not self.data

    def __str__(self):
        reversed_data = reversed(self.data)
        result = ", ".join(reversed_data)
        return f"[{result}]"