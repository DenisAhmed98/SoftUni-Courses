sentence = input()
sentence= sentence.lower()
counter = 0

counter += sentence.lower().count("water")
counter += sentence.lower().count("sun")
counter += sentence.lower().count("fish")
counter += sentence.lower().count("sand")
print(counter)
