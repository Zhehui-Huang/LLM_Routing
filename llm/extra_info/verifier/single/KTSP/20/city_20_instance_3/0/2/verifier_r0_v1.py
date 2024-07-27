import math
import unittest

def calculate_distance(city1, city2):
    """Calculates Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
            5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
            10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
            15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
        }
        self.test_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 0]
        self.reported_cost = 273.74

    def test_tour_start_end_at_depot(self):
        """Test if the tour starts and ends at the depot (city 0)."""
        self.assertEqual(self.test_tour[0], 0)
        self.assertEqual(self.test_tour[-1], 0)

    def test_tour_length(self):
        """Test if the tour has 13 cities including the depot city."""
        self.assertEqual(len(set(self.test_tour)), 13)

    def test_tour_correctness_of_cost(self):
        """Test if the reported cost matches calculated cost."""
        calculated_cost = sum(calculate_distance(self.cities[self.test_tour[i]], self.cities[self.test_tour[i + 1]])
                               for i in range(len(self.test_tour) - 1))
        self.assertAlmostEqual(calculated, self.reported_cost, places=2)

    def test_output_format(self):
        """Test if the output format requirement is satisfied."""
        self.assertIsInstance(self.test_tour, list)
        self.assertIsInstance(self.reported_cost, (int, float))
        self.assertEqual(len(self.test_tour), 14)  # 13 cities and returns to depot

def perform_test_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

perform_test_suite()