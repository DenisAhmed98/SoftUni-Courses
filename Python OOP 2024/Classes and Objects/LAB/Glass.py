class Glass:
    content = 0
    capacity = 250

    def fill(self, ml):
        if Glass.content + ml <= Glass.capacity:
            Glass.content += ml
            return f"Glass filled with {ml} ml"
        else:
            return f"Cannot add {ml} ml"

    def empty(self):
        Glass.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{Glass.capacity - Glass.content} ml left"

glass = Glass()

print(glass.fill(100))

print(glass.fill(200))

print(glass.empty())

print(glass.fill(200))

print(glass.info())