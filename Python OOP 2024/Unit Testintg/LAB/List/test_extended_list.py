from unittest import TestCase, main
from extended_list import IntegerList

class TestIntegerList(TestCase):
    def setUp(self):
        self.integerList = IntegerList(1,0.5,3,-2)

    def test_correct_init(self):
        self.assertEqual([1,3,-2], self.integerList.get_data())

    def test_add_correct_value_to_list(self):
        expected = self.integerList.get_data() + [55]

        self.integerList.add(55)

        self.assertEqual(expected,self.integerList.get_data())

    def test_add_float_value_to_list(self):

        with self.assertRaises(ValueError) as ve:
            self.integerList.add(5.5)

        self.assertEqual("Element is not Integer",str(ve.exception))

    def test_remove_inbounds_index(self):
        self.integerList.remove_index(1)
        self.assertEqual([1,-2], self.integerList.get_data())

    def test_remove_out_of_bounds_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integerList.remove_index(1000000)

        self.assertEqual("Index is out of range",str(ie.exception))

    def test_get_correct_index(self):
        self.assertEqual(3,self.integerList.get(1))

    def test_get_out_of_bounds_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integerList.get(1000000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_correct_index(self):
        self.integerList.insert(1, 55)
        self.assertEqual([1, 55, 3, -2], self.integerList.get_data())

    def test_insert_out_of_range_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integerList.insert(500,4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_non_integer_value(self):
        with self.assertRaises(ValueError) as ve:
            self.integerList.insert(1,4.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_return_biggest_value(self):
        self.assertEqual(3, self.integerList.get_biggest())

    def test_returns_index_of_element(self):
        self.assertEqual(1, self.integerList.get_index(3))

if __name__ == "__main__":
    main()