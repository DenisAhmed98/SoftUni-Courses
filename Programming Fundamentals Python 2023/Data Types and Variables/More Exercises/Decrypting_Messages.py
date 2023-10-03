key = int(input())
lines = int(input())
output = ""
for character in range (lines):
    symbol = input()
    decrypting = ord(symbol)+key
    output += str(chr(decrypting))

print(output)
