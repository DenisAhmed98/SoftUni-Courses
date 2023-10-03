book = input()
counter = 0
while True:
    bookshelf = input()
    counter +=1
    if book == bookshelf:
        print(f"You checked {counter-1} books and found it.")
        break
    elif bookshelf == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter-1} books.")
        break

