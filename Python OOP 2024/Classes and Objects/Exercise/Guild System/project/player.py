class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = dict()
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        else:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        info = f"Name: {self.name}\n\
Guild: {self.guild}\n\
HP: {self.hp}\n\
MP: {self.mp}\n"

        for key,value in self.skills.items():
            info = info + f"==={key} - {value}\n"

        return info
