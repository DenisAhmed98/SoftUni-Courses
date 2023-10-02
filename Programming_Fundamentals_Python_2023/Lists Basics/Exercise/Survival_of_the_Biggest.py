list = [int(x) for x in input().split()]
remover = int(input())
for x in range (remover):
    list.remove(min(list))
joined_string = ", ".join(map(str,list))
for x in joined_string:
    print(x, end="")