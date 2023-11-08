text = input()

while text != "end":
    text_rev = ""
    for c in reversed(text):
        text_rev += c
    print(f"{text} = {text_rev}")
    text = input()