from typing import List

from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.clients.adult import Adult

class BankApp:

    LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    CLIENTS_TYPES = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self,loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")
        new_loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENTS_TYPES:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.CLIENTS_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_client_by_id(client_id)
        loan = self.find_loan_by_type(loan_type)
        if not client.POSSIBLE_LOAN_TYPE == loan_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f'Successfully granted {loan_type} to {client.name} with ID {client_id}.'

    def remove_client(self, client_id: str):
        client = self.find_client_by_id(client_id)

        if client is None:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans_increased = 0

        for loan in self.loans:
            if loan.TYPE_LOAN == loan_type:
                loan.increase_interest_rate()
                loans_increased += 1
        return f"Successfully changed {loans_increased} loans."

    def increase_clients_interest(self, min_rate: float):
        clients_increased = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                clients_increased += 1
        return f"Number of clients affected: {clients_increased}."

    def get_statistics(self):
        total_income = sum([client.income for client in self.clients])
        granted_loans_count = sum([len(client.loans) for client in self.clients])
        granted_amount = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        not_granted_sum = sum([loan.amount for loan in self.loans])
        avg_client_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0

        return f"""Active Clients: {len(self.clients)}
Total Income: {total_income:.2f}
Granted Loans: {granted_loans_count}, Total Sum: {granted_amount:.2f}
Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {avg_client_rate:.2f}"""

    def find_client_by_id(self, client_id):
        collection = [c for c in self.clients if c.client_id == client_id]
        return collection[0] if collection else None

    def find_loan_by_type(self, loan_type):
        collection = [c for c in self.loans if c.TYPE_LOAN == loan_type]
        return collection[0] if collection else None
