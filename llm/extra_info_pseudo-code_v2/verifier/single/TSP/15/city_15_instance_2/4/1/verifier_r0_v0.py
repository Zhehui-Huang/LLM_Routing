import unittest
from math import sqrt

class TestTourValidity(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (54, 87), # city 0: depot
            (21, 84), # city 1
            (69, 84), # city 2
            (53, 40), # city 3
            (54, 42), # city 4
            (36, 30), # city 5
            (52, 82), # city 6
            (93, 44), # city 7
            (21, 78), # city 8
            (68, 14), # city 9
            (51, 28), # city 10
            (44, 79), # city 11
            (56, 58), # city 12
            (72, 43), # city 13
            (6, 99)  # city 14
        ]
        self.tour = [0, 6, 11, 14, 1, 8, 12, 4, 3, 5, 10, 9, 13, 7, 2, 0]
        self.reported_cost = 311.88

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot city.")

    def test_visits_all_cities_once(self):
        for city in range(1, 15):  # check cities 1 to 14
            self.assertIn(city, self.tour, f"City {city} is missing in the tour.")
        # Check that no extra cities are visited
        self.assertCountEqual(self.tour[1:-1], list(range(1, 15)), "Cities are not visited exactly once.")

    def test_euclidean_cost(self):
        def euclidean_distance(a, b):
            return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

        calculated_cost = sum(
            euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            for i in range(len(self.tour) - 1)
        )
        
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2, msg=f"Calculated cost {calculated_cost} does not match reported cost {self.reported_cost}.")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(TestTourValidity))
    test_runner = unittest.TextTestRunner()
    result = test_enum.values.all_run(test_suite)
    
    # Check the result and print "CORRECT" if all tests pass or "FAIL" if any fail
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")