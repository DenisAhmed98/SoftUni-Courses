import math

from project.clients.base_client import BaseClient


class VIPClient(BaseClient):
    MEMBER_TYPE = "VIP"

    def __init__(self, name: str):
        super().__init__(name, membership_type=self.MEMBER_TYPE)

    def earning_points(self, order_amount: float):
        result = int(math.floor(order_amount/5))
        self.points += result

        return result
