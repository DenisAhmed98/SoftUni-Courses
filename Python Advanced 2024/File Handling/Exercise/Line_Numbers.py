from string import punctuation

with open("Files\File02.txt", "r") as file:
    text = file.readlines()

output_file = open('Files\File02_Results.txt', 'w')

for line in range(len(text)):
    letters = 0
    marks = 0
    for symbol in text[line]:

        if symbol.isalpha():
            letters +=1
        elif symbol in punctuation:
            marks +=1

   
    output_file.write(f"Line { line + 1 }: {''.join(text[line][:-1])} ({letters})({marks})\n")

output_file.close()
