from unittest import TestCase, main
from project.restaurant import Restaurant

class TestRestaurant(TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Test", 50)

    def test_correct__init(self):
        self.assertEqual(self.restaurant.name, "Test")
        self.assertEqual(self.restaurant.capacity, 50)
        self.assertEqual(self.restaurant.waiters, [])

    def test_wrong_name_expect_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = " "

        self.assertEqual(str(ve.exception),"Invalid name!")

    def test_wrong_capacity_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -5

        self.assertEqual(str(ve.exception),"Invalid capacity!")

    def test_add_waiters(self):
        ex = self.restaurant.add_waiter("Ivan")

        self.assertEqual(ex, "The waiter Ivan has been added.")
        self.assertEqual(self.restaurant.waiters, [{'name': 'Ivan'}])

    def test_add_waiters_full_capacity(self):
        self.restaurant.capacity = 0
        ex = self.restaurant.add_waiter("Ivan")

        self.assertEqual(ex, "No more places!")
        self.assertEqual(self.restaurant.waiters, [])

    def test_add_waiters_existing_name(self):
        self.restaurant.add_waiter("Ivan")

        ex = self.restaurant.add_waiter("Ivan")

        self.assertEqual(ex, "The waiter Ivan already exists!")
        self.assertEqual(self.restaurant.waiters, [{'name': 'Ivan'}])

    def test_remove_waiter_correct(self):
        self.restaurant.add_waiter("Ivan")
        ex = self.restaurant.remove_waiter("Ivan")

        self.assertEqual(ex, "The waiter Ivan has been removed.")
        self.assertEqual(self.restaurant.waiters, [])

    def test_remove_waiter_with_wrong_name(self):
        ex = self.restaurant.remove_waiter("Ivan")

        self.assertEqual(ex, "No waiter found with the name Ivan.")
        self.assertEqual(self.restaurant.waiters, [])

    def test_get_waiters_correct(self):
        self.restaurant.add_waiter("Ivan")
        self.restaurant.add_waiter("Pesho")

        ex = self.restaurant.get_waiters()
        self.assertEqual(ex,[{'name': 'Ivan'}, {'name': 'Pesho'}])

    def test_get_waiter_empty(self):
        self.restaurant.add_waiter("Ivan")
        self.restaurant.add_waiter("Pesho")
        ex = self.restaurant.get_waiters(500, 1000)
        self.assertEqual(ex, [])

    def test_get_total_earnings(self):
        self.restaurant.add_waiter("Ivan")
        self.restaurant.add_waiter("Pesho")

        ex = self.restaurant.get_total_earnings()
        self.assertEqual(ex, 0)



if __name__ == "__main__":
    main()