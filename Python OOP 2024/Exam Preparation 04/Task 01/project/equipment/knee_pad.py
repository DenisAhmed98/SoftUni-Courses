from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PRICE = 15.0
    PROTECTION = 120

    def __init__(self):
        super().__init__(KneePad.PROTECTION, KneePad.PRICE)

    def increase_price(self):
        KneePad.PRICE *= 1.2

