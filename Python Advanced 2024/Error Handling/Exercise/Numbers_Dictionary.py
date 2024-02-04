numbers_dictionary = {}

while True:
    line = input()
    if line == "Search":
        break
    number_as_string = line
    number = int(input())
    numbers_dictionary[number_as_string] = number

line = input()

while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])
    line = input()
line = input()

while line != "End":
    searched = line
    del numbers_dictionary[searched]
    line = input()

print(numbers_dictionary)