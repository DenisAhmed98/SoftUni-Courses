def vowel_filter(function):
    def wrapper():
        res = function()
        filtered = [x for x in res if x.lower() in "aeiou"]
        return filtered
    return wrapper