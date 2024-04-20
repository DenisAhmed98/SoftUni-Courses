from project.trip import Trip
from unittest import TestCase, main

class TestTripClass(TestCase):

    DESTINATION_PRICES_PER_PERSON = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}

    def setUp(self) -> None:
        self.trip= Trip(500, 2, True)
    
    def test__init__(self):
        self.assertEqual(self.trip.budget, 500)
        self.assertEqual(self.trip.travelers, 2)
        self.assertEqual(self.trip.is_family, True)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})
    
    def test_travlers_init_less_than_one_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
         
        self.assertEqual(str(ve.exception), "At least one traveler is required!")
    
    def test_is_family_with_2_people_and_True_expected_True(self):
        test = Trip(500,2,True)

        self.assertEqual(test.is_family, True)
    
    def test_is_family_with_1_people_and_True_expected_False(self):
        test = Trip(500,1,True)

        self.assertEqual(test.is_family, False)
    
    def test_is_family_with_5_people_and_False_expected_False(self):
        test = Trip(500,5,False)

        self.assertEqual(test.is_family, False)
    
    def test_book_a_trip_expect_Destination_not_offered(self):
        ex = self.trip.book_a_trip("Germany")
        r = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(ex, r)
    
    def test_book_a_trip_expect_not_enough_budget_with_family(self):
        family = Trip(50,2,True)
        ex = family.book_a_trip("Australia")

        r = 'Your budget is not enough!'
        self.assertEqual(ex, r)
    
    def test_book_a_trip_expect_with_family(self):
        family = Trip(20000,2,True)
        ex = family.book_a_trip("Australia")
        req = 20000 - family.budget

        r = f'Successfully booked destination Australia! Your budget left is {family.budget:.2f}'
        self.assertEqual(ex, r)
        self.assertEqual({'Australia': req},family.booked_destinations_paid_amounts)
    
    def test_booking_status_expect_No_bookings_yet(self):
        test = Trip(20000,2,True)
        ex = test.booking_status()

        self.assertEqual(f'No bookings yet. Budget: {test.budget:.2f}', ex)
    
    def test_booking_status_expect_destinations_listed(self):
        family = Trip(20000,2,True)
        family.book_a_trip("Australia")
        ex = family.booking_status()
        r = "Booked Destination: Australia\n" \
            "Paid Amount: 10260.00\n" \
            "Number of Travelers: 2\n" \
            "Budget Left: 9740.00"
            
        self.assertEqual(r, ex)




    
    
    



if __name__ == "__main__":
    main()
