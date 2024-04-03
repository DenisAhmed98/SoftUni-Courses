def make_underline(function): 
    def wrapper(*args):
        result = "<u>"+function(*args)+"</u>"
        return result
    return wrapper

def make_italic(function): 
    def wrapper(*args):
        result = "<i>"+function(*args)+"</i>"
        return result
    return wrapper

def make_bold(function): 
    def wrapper(*args):
        result = "<b>"+function(*args)+"</b>"
        return result
    return wrapper

@make_bold
@make_italic
@make_underline
def greet(name):

    return f"Hello, {name}"

print(greet("Peter"))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))