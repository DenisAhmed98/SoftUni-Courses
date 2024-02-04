def kwargs_length(**dictionary):
    return len(dictionary.items())

dictionary = {}

print(kwargs_length(**dictionary))