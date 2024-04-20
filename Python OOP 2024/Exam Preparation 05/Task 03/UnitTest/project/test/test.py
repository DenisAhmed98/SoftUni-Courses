from project.second_hand_car import SecondHandCar
from unittest import TestCase, main

class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("BMW","Sport", 6000, 12000)
        self.car_compare = SecondHandCar("Audi", "Sport", 4000, 10000)

    def test_init_correct(self):
        self.assertEqual(self.car.model, "BMW")
        self.assertEqual(self.car.car_type, "Sport")
        self.assertEqual(self.car.mileage, 6000)
        self.assertEqual(self.car.price, 12000)
        self.assertEqual(self.car.repairs, [])

    def test_low_price_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual(str(ve.exception), 'Price should be greater than 1.0!')

    def test_small_mileage_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 0

        self.assertEqual(str(ve.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_new_price_correct(self):
        ex = self.car.set_promotional_price(10000)

        self.assertEqual(ex, 'The promotional price has been successfully set.')
        self.assertEqual(self.car.price, 10000)

    def test_set_new_price_higher_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(15000)

        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')
        self.assertEqual(self.car.price, 12000)

    def test_set_new_price_equal_to_old_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(12000)

        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')
        self.assertEqual(self.car.price, 12000)

    def test_need_repair_correct(self):
        ex = self.car.need_repair(500, "engine")

        self.assertEqual(ex, 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 12500)
        self.assertEqual(self.car.repairs, ['engine'])

    def test_need_repair_with_too_expensive_price_expect_Repair_Impossible(self):
        ex = self.car.need_repair(7000, "engine")

        self.assertEqual(ex, 'Repair is impossible!')
        self.assertEqual(self.car.price, 12000)
        self.assertEqual(self.car.repairs, [])

    def test__gt__correct_Expect_True(self):
        ex = self.car.__gt__(self.car_compare)
        self.assertEqual(ex, True)

    def test__gt__correct_Expect_False(self):
        self.car_compare.price = 50000
        ex = self.car.__gt__(self.car_compare)
        self.assertEqual(ex, False)

    def test__gt__Car_type_mismatch_Expect_Error(self):
        self.car_compare.car_type = "Family"
        ex = self.car.__gt__(self.car_compare)
        self.assertEqual(ex, 'Cars cannot be compared. Type mismatch!')

    def test__str__(self):
        ex = self.car.__str__()
        r = f"Model BMW | Type Sport | Milage 6000km\n" \
            "Current price: 12000.00 | Number of Repairs: 0"
        self.assertEqual(ex, r)




if __name__ == "__main__":
    main
