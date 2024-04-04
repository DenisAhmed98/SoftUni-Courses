from unittest import TestCase, main
#from UnitTestintg.Exercise.vehicle.project.vehicle import Vehicle
#for Judge
from project.vehicle import Vehicle

class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(350,17.5)

    def test_initialization_of_vehicle(self):
        self.assertEqual(350, self.vehicle.fuel)
        self.assertEqual(350, self.vehicle.capacity)
        self.assertEqual(17.5,self.vehicle.horse_power)
        self.assertEqual(1.25,self.vehicle.fuel_consumption)

    def test_drive_when_we_have_enough_fuel(self):
        expected = self.vehicle.fuel - (self.vehicle.fuel_consumption * 1)
        self.vehicle.drive(1)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_drive_with_NOT_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_amount_smaller_than_capacity(self):
        self.vehicle.fuel = 50
        expected = self.vehicle.fuel + 1
        self.vehicle.refuel(1)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_refuel_with_amount_larger_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_string_print_information(self):
        self.assertEqual("The vehicle has 17.5 " \
               f"horse power with 350 fuel left and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()