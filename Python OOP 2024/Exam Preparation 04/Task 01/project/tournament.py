from typing import List

from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam
from project.equipment.base_equipment import BaseEquipment
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad

class Tournament:

    VALID_EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    VALID_TEAMS_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        try:
            equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]
        except KeyError:
            return "Invalid equipment type!"

        instance = equipment()
        self.equipment.append(instance)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        try:
            team = self.VALID_TEAMS_TYPES[team_type](team_name,country,advantage)
        except KeyError:
            return "Invalid team type!"

        if len(self.teams) < self.capacity:
            self.teams.append(team)
            return f"{team_type} was successfully added."
        else:
            return "Not enough tournament capacity."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self._find_last_equipment_by_type(equipment_type)
        team = self._find_team_by_name(team_name)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def _find_last_equipment_by_type(self, equipment_type):
        collection = [eq for eq in self.equipment if eq.__class__.__name__ == equipment_type]
        return collection[-1] if collection else None

    def _find_team_by_name(self, team_name):
        collection = [t for t in self.teams if t.name == team_name]
        return collection[0] if collection else None

    def remove_team(self, team_name: str):
        team = [t for t in self.teams if t.name == team_name]
        if not team:
            raise Exception("No such team!")
        if team[0].wins > 0:
            raise Exception(f"The team has {team[0].wins} wins! Removal is impossible!")
        self.teams.remove(team[0])
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        times = 0
        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                times += 1
        return f"Successfully changed {times}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        teamA = [t for t in self.teams if t.name == team_name1]
        teamB = [t for t in self.teams if t.name == team_name2]

        if teamA.__class__.__name__ == teamB.__class__.__name__:
            points_teamA = teamA[0].advantage
            points_teamB = teamB[0].advantage
            for e in teamA[0].equipment:
                points_teamA += e.protection
            for e in teamB[0].equipment:
                points_teamB += e.protection

            if points_teamA > points_teamB:
                teamA[0].win()
                return f"The winner is {team_name1}."
            elif points_teamA < points_teamB:
                teamB[0].win()
                return f"The winner is {team_name2}."
            else:
                return "No winner in this game."

        else:
            raise Exception("Game cannot start! Team types mismatch!")

    def get_statistics(self):
        teams_sorted = sorted(self.teams, key=lambda t: -t.wins)
        statistics = [f"Tournament: {self.name}",
        f"Number of Teams: {len(self.teams)}",
        "Teams:"]

        for t in teams_sorted:
            statistics.append(t.get_statistics())

        return "\n".join(statistics)

