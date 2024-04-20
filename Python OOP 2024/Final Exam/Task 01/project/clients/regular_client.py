import math

from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    MEMBER_TYPE = "Regular"

    def __init__(self, name: str):
        super().__init__(name, membership_type=self.MEMBER_TYPE)

    def earning_points(self, order_amount: float):
        result = int(math.floor(order_amount /10))
        self.points += result

        return result
