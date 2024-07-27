import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of cities: city index is the key, coordinates are the value (tuple)
        self.coordinates = {
            0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
            6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
            12: (56, 58), 13: (72, 43), 14: (6, 99)
        }
        # Given tour and cost
        self.tour = [0, 6, 11, 12, 4, 13, 7, 2, 3, 10, 9, 5, 8, 1, 14, 0]
        self.reported_cost = 383.7033875464016

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot city.")

    def test_visit_all_cities_exactly_once(self):
        without_depot = list(range(1, 15))
        tour_without_depot_and_end = self.tour[1:-1]
        self.assertCountEqual(tour_without_deport_and_end, without_deport, "Not all cities are visited exactly once.")

    def test_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += euclidean_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]])

        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5, msg=f"Reported travel cost is inaccurate. Calculated: {calculated_cost}")

def run_tests():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestTSPSolution))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Check if all tests passed
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Execute tests
print(run_tests())