def decypher(word):
    word_list = [x for x in word]
    decyphered_word = []
    temp_num = ""
    for i in word_list:
        if i.isdigit():
            temp_num += i
        else:
            decyphered_word.append(i)

    decyphered_word.append(decyphered_word[0])
    decyphered_word.insert(0,decyphered_word[-2])
    decyphered_word.insert(0,chr(int(temp_num)))
    decyphered_word.pop(2)
    decyphered_word.pop(-2)

    return "".join(decyphered_word)

message = input().split(" ")

for words in message:
    print(decypher(words), end=" ")
