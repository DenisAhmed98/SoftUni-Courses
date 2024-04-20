from project.clients.base_client import BaseClient


class Adult(BaseClient):
    TYPE_CLIENT = "Adult"
    INTEREST_RATE = 4.0
    POSSIBLE_LOAN_TYPE = 'MortgageLoan'

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INTEREST_RATE)

    def increase_clients_interest(self):
        self.interest += 2.0