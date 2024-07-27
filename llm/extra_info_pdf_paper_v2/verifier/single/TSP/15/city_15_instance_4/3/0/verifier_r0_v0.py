import unittest
from math import sqrt

def calculate_euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
            4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
            8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
            12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        self.tour = [0, 1, 5, 9, 2, 7, 4, 12, 11, 6, 3, 8, 14, 13, 10, 0]
        self.reported_cost = 288.5242816725832

    def test_correct_number_of_cities(self):
        # Check if there are 15 cities including the depot
        self.assertEqual(len(self.cities), 15)

    def test_tour_starts_and_ends_at_depot(self):
        # Check start and end at depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_cities_visited_exactly_once(self):
        # Check each city visited exactly once (except the depot which is visited twice)
        unique_cities = set(self.tour)
        all_cities = set(self.cities.keys())
        self.assertTrue(all_cities.issubset(unique_cities))
        self.assertEqual(len(self.tour), len(all_cities) + 1)

    def test_calculate_total_travel_cost(self):
        # Calculate total travel distance based on the provided tour
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tourn[i + 1]]
            calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
        self.assertAlmostEqual(self.reported_cost, calculated_cost, places=5)

    def test_output_format(self):
        # Check output format
        self.assertIsInstance(self.tour, list)
        self.assertGreater(len(self.tour), 0)
        self.assertTrue(all(isinstance(item, int) for item in self.tour))
        self.assertIsInstance(self.reported_cost, float)

def run_test_cases():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Running the test cases
print(run_test_cases())