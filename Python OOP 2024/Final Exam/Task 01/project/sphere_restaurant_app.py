from project.clients.base_client import BaseClient
from project.clients.vip_client import VIPClient
from project.clients.regular_client import RegularClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    WAITER_TYPES = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter
    }
    CLIENT_TYPES = {
        "RegularClient": RegularClient,
        "VIPClient": VIPClient
    }

    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.WAITER_TYPES:
            return f"{waiter_type} is not a recognized waiter type."

        if self._find_waiter_by_name(waiter_name) is not None:
            return f"{waiter_name} is already on the staff."

        new_waiter = self.WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.CLIENT_TYPES:
            return f"{client_type} is not a recognized client type."
        if self._find_client_by_name(client_name) is not None:
            return f"{client_name} is already a client."

        new_client = self.CLIENT_TYPES[client_type](client_name)
        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = self._find_waiter_by_name(waiter_name)
        if waiter is None:
            return f"No waiter found with the name {waiter_name}."
        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = self._find_client_by_name(client_name)
        if client is None:
            return f"{client_name} is not a registered client."
        points_earned = client.earning_points(order_amount)
        return f"{client_name} earned {points_earned} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = self._find_client_by_name(client_name)
        if client is None:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        discount, points_left = client.apply_discount()
        return f"{client_name} received a {discount}% discount. Remaining points {points_left}"

    def generate_report(self):
        report = ["$$ Monthly Report $$"]
        total_earnings = sum([waiter.calculate_earnings() for waiter in self.waiters])
        total_client_points = sum([client.points for client in self.clients])
        report.append(f"Total Earnings: ${total_earnings:.2f}")
        report.append(f"Total Clients Unused Points: {total_client_points}")
        report.append(f"Total Clients Count: {len(self.clients)}")
        report.append("** Waiter Details **")
        sorted_waiters = sorted(self.waiters, key=lambda waiter: waiter.calculate_earnings(), reverse=True)

        for w in sorted_waiters:
            report.append(w.__str__())

        return "\n".join(report)

    # Helper Functions
    def _find_waiter_by_name(self, waiter_name):
        waiters_filter = [w for w in self.waiters if w.name == waiter_name]
        return waiters_filter[0] if waiters_filter else None

    def _find_client_by_name(self, client_name):
        clients_filter = [c for c in self.clients if c.name == client_name]
        return clients_filter[0] if clients_filter else None


# Create an instance of SphereRestaurantApp
sphere_restaurant_app = SphereRestaurantApp()

# Hire some waiters
print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "John", 40))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 20))
print(sphere_restaurant_app.hire_waiter("InvalidWaiter", "JohnDoe", 10))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Charlie", 30))
print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "Frank", 50))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 60))
# Admit some clients
print(sphere_restaurant_app.admit_client("InvalidClient", "JohnDoe"))
print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
print(sphere_restaurant_app.admit_client("VIPClient", "Lila"))
print(sphere_restaurant_app.admit_client("RegularClient", "Bob"))
print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
print(sphere_restaurant_app.admit_client("RegularClient", "Oscar"))
# Process shifts
print(sphere_restaurant_app.process_shifts("John"))
print(sphere_restaurant_app.process_shifts("Alice"))
print(sphere_restaurant_app.process_shifts("Emily"))
print(sphere_restaurant_app.process_shifts("Frank"))
# Process client orders
print(sphere_restaurant_app.process_client_order("Bob", 100.0))
print(sphere_restaurant_app.process_client_order("Eve", 500.0))
print(sphere_restaurant_app.process_client_order("JohnDoe", 250.0))
print(sphere_restaurant_app.process_client_order("Bob", 750.0))
print(sphere_restaurant_app.process_client_order("Lila", 550.0))
print(sphere_restaurant_app.process_client_order("Oscar", 84.0))
# Apply discounts to clients
print(sphere_restaurant_app.apply_discount_to_client("Lila"))
print(sphere_restaurant_app.apply_discount_to_client("Eve"))
print(sphere_restaurant_app.apply_discount_to_client("JohnDoe"))
print(sphere_restaurant_app.apply_discount_to_client("Oscar"))
print(sphere_restaurant_app.apply_discount_to_client("Bob"))
# Generate report
print(sphere_restaurant_app.generate_report())