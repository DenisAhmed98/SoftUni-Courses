from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PRICE = 25.0
    PROTECTION = 90

    def __init__(self):
        super().__init__(ElbowPad.PROTECTION, ElbowPad.PRICE)

    def increase_price(self):
        ElbowPad.PRICE *= 1.1