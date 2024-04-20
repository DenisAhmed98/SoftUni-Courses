from project.clients.base_client import BaseClient


class Student(BaseClient):
    TYPE_CLIENT = "Student"
    INTEREST_RATE = 2.0
    POSSIBLE_LOAN_TYPE = 'StudentLoan'

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INTEREST_RATE)

    def increase_clients_interest(self):
        self.interest += 1.0