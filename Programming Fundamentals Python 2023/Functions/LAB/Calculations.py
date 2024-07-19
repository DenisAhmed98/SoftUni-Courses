input_operator = input()
num_a = int(input())
num_b = int(input())

def solve(a,b,operator):
    result = 0
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result

print(solve(num_a,num_b,input_operator))