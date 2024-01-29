def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return f"Enter valid values!"
    def area():
        return length * width
    def perimeter():
        rect_perim = 2*length + 2*width
        return 2*(length+width)
    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

print(rectangle(2, 10))