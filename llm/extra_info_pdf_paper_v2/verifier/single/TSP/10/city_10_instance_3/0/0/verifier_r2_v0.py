import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        self.tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
        self.computed_cost = 294.17253892411236

    def test_tour_start_end_at_depot(self):
        # Check if the tour starts and ends at depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_all_cities_once(self):
        # Check if all cities are visited exactly once, except depot
        tour_cities = self.tour[1:-1]
        unique_cities = set(tour_cities)
        self.assertEqual(len(unique_cities), 9)  # 9 unique cities excluding depot

    def test_travel_cost_calculation(self):
        # Function to calculate Euclidean distance
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # Calculate the total travel cost
        calculated_cost = sum(euclidean_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour)-1))

        # Check if calculated cost matches the provided total travel cost
        self.assertAlmostEqual(calculated. cost, self.computed_cost, places=5)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    # Add test methods
    test_suite.addTest(TestTSPSolution('test_tour_start_end_at_depot'))
    test_suite.addTest(TestTSPSolution('test_visit_all_cities_once'))
    test_suite.addTest(TestTSPSolution('test_travel_cost_calculation'))

    # Run the tests
    results = unittest.TextTestRunner().run(test_suite)

    # Output based on test results
    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")