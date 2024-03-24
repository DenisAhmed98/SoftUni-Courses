def reverse_text(text):
    rev = text[::-1]
    yield rev

for char in reverse_text("step"):
    print(char, end='')