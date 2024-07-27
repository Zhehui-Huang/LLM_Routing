import unittest
from math import sqrt

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 1, 3, 5, 6, 7, 8, 12, 13, 15, 16, 17, 19, 0]
        self.total_cost = 447.62897450253973
        self.coordinates = [
            (30, 56),  # City 0 (depot)
            (53, 42),  # City 1
            (1, 95),   # City 2
            (25, 61),  # City 3
            (69, 57),  # City 4
            (6, 58),   # City 5
            (12, 84),  # City 6
            (72, 77),  # City 7
            (98, 95),  # City 8
            (11, 0),   # City 9
            (61, 25),  # City 10
            (52, 0),   # City 11
            (60, 95),  # City 12
            (10, 94),  # City 13
            (96, 73),  # City 14
            (14, 47),  # City 15
            (18, 16),  # City 16
            (4, 43),   # City 17
            (53, 76),  # City 18
            (19, 72),  # City 19
        ]

    def test_tour_starts_and_ends_at_depot(self):
        """ Requirement 1: Tour starts and ends at the depot city. """
        self.assertEqual(self.tour[0], 0, "Tour should start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at city 0")
    
    def test_tour_visits_exactly_13_cities(self):
        """ Requirement 2: Tour must visit exactly 13 cities, including depot. """
        expected_cities_count = 13
        actual_cities_count = len(set(self.tour))
        self.assertEqual(actual_cities_count, expected_cities_count,
                         f"Tour should visit exactly {expected_cities_count} cities including the depot city.")
    
    def test_tour_travel_cost_correct(self):
        """ Requirement 4: Check the tour cost based on Euclidean distances. """
        def euclidean_distance(city1, city2):
            return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
        
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city_a = self.coordinates[self.tour[i]]
            city_b = self.coordinates[self.tour[i + 1]]
            calculated_cost += euclidean_distance(city_a, city_b)

        self.assertAlmostEqual(self.total_cost, calculated_cost, places=5,
                               msg="The calculated travel cost does not match the provided travel cost.")
    
    def test_output_format(self):
        """ Requirement 5: Ensure output format correctness for both tour and total cost. """
        self.assertIsInstance(self.tour, list, "Tour should be output as a list of city indices.")
        self.assertIsInstance(self.total_cost, float, "Total cost should be a float value.")
        self.assertEqual(self.tour[0], self.tour[-1], "Tour should start and end at the depot city (index 0).")
        self.assertEqual(len(set(self.tour)), 13, "Tour should include exactly 13 unique cities.")

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestKTSPSolution))
    runner = unittest.TextTestRunner()

    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")