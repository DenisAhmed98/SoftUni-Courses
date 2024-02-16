def team_lineup(*args):
    data = {}
    for name, country in args:
        if country not in data:
            data[country] = []
        data[country].append(name)
        
    
    result = ""

    sortedPlayers = sorted(data.items(), key=lambda x: (-len(x[1]), x[0]))

    for country, players in sortedPlayers:
        result += f"{country}:\n"
        for name in players:
            result += f"  -{name}\n"
    return result
        
    



print(team_lineup(

("Harry Kane", "England"),

("Manuel Neuer", "Germany"),

("Raheem Sterling", "England"),

("Toni Kroos", "Germany"),

("Cristiano Ronaldo", "Portugal"),

("Thomas Muller", "Germany")))