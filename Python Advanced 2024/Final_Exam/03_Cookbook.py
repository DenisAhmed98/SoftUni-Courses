def cookbook(*args):
    book = {}
    result = ""
    for name, cuisine, ingredients in args:
        if cuisine not in book:
            book[cuisine] = {}
        book[cuisine][name] = ingredients

    sortedBook = dict(sorted(book.items(), key=lambda sub: (-len(sub[1]), sub[0])))

    for country, recipes in sortedBook.items():
        result += f"{country} cuisine contains {len(recipes)} recipes:\n"
        sorted_recipes = dict(sorted(recipes.items()))
        for name, ingredients in sorted_recipes.items():
            result += f"  * {name} -> Ingredients: {', '.join(ingredients)}\n"

    return result
matrix = [[0, 0],[1,1]]
print(matrix[2][2])


print(cookbook(
                    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
                      ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
                      ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
                      ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
                      ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
                      ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
                      ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
                      ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"])))