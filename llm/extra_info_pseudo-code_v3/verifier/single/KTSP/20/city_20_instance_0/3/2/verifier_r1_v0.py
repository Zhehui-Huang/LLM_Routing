import unittest
import math

# Function to calculate the Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Test cases provided for validation
class TestSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.cities = {
            0: (8, 11),
            1: (40, 6),
            8: (61, 16),
            17: (61, 28)
        }
        # Provided solution to test
        self.tour = [0, 1, 8, 17, 0]
        self.total_cost = 123.31
    
    def test_starts_and_ends_at_depot(self):
        # Testing Requirement 1
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_four_cities_including_depot(self):
        # Testing Requirement 2
        self.assertEqual(len(set(self.tour)), 4)  # Set to exclude duplicate of starting/ending city

    def test_euclidean_distance_used(self):
        # Testing Requirement 4
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            calculated_cost += euclidean_distance(*self.cities[city1], *self.cities[city2])
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=2)

    def test_output_format(self):
        # Testing Requirement 5 and 6
        is_correct_format = isinstance(self.tour, list) and all(isinstance(i, int) for i in self.tour)
        self.assertTrue(is_correct_format)
        self.assertIsInstance(self.total_cost, float)

# Running the unit tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)