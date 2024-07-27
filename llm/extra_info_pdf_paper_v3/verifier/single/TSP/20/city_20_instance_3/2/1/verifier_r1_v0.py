import unittest
from math import sqrt

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 56), # Depot
            (53, 42),
            (1, 95),
            (25, 61),
            (69, 57),
            (6, 58),
            (12, 84),
            (72, 77),
            (98, 95),
            (11, 0),
            (61, 25),
            (52, 0),
            (60, 95),
            (10, 94),
            (96, 73),
            (14, 47),
            (18, 16),
            (4, 43),
            (53, 76),
            (19, 72)
        ]
        self.tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
        self.total_cost = 458.36719998557066

    def test_starts_and_ends_at_depot(self):
        """ Test if the tour starts and ends at the depot city, which is city 0 """
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot.")
    
    def test_visits_all_cities_exactly_once(self):
        """ Test if all cities are visited exactly once, except the depot which should be visited twice (start, end) """
        from collections import Counter
        city_visit_counts = Counter(self.tour)
        self.assertEqual(city_visit_counts[0], 2, "Depot city should be visited exactly twice.")
        for city_index in range(1, len(self.cities)):
            self.assertEqual(city_visit_counts[city_index], 1, f"City {city_index} is not visited exactly once.")
    
    def test_tour_cost_calculation(self):
        """ Test if the total cost matches the expected travel cost using Euclidean distance """
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i+1]]
            calculated_cost += sqrt((x1 - x2)**2 + (y1 - y2)**2)
        self.assertAlmostEqual(calculated_paylode_cost, self.total_cost, places=5, \
                               msg=f"Calculated cost {calculated_cost} does not match provided cost {self.total_cost}.")
    
    def test_correct_output_format(self):
        """ Test if output format is correct and all requisite elements are present """
        self.assertIsInstance(self.turbines, list, "Tour should be a list of indices.")
        self.assertIsInstance(self.total_cost, float, "Total travel cost should be a float.")

# Run the tests
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTourSolution))
runner = unittest.TextTestRunner()
result = runner.run(suite)

# Output result based on test outcomes
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")