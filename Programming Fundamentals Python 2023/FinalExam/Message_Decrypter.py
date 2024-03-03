import re
number_of_inputs = int(input())

pattern = r"([$][A-Z][a-z]{3,}[$]: (\[(\d+)\]\|){3})|([%][A-Z][a-z]{3,}[%]: (\[(\d+)\]\|){3})"
word_pattern = r"([A-Z][a-z]{3,})"
for check in range(number_of_inputs):
    message = input()
    if message[0] == "$" or message[0] == "%":
        match =re.findall(pattern, message)
        if match:
            word = "".join(re.findall(word_pattern, message))
            numbers = " ".join(re.findall(r"\d+", message))
            token = numbers.split(" ")
            if len(token) > 3:
                print("Valid message not found!")
            else:
                print(f"{word}: {chr(int(token[0]))}{chr(int(token[1]))}{chr(int(token[2]))}")
        else:
            print("Valid message not found!")
    else:
        print("Valid message not found!")