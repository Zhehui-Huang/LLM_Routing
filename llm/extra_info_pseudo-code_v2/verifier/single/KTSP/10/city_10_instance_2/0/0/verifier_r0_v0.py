import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (90, 3),
            1: (11, 17),
            2: (7, 27),
            3: (95, 81),
            4: (41, 54),
            5: (31, 35),
            6: (23, 95),
            7: (20, 56),
            8: (49, 29),
            9: (13, 17)
        }
        self.tour = [0, 8, 5, 1, 9, 0]  # Given solution tour
        self.total_cost = 174.69  # Given solution cost

    def test_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "The tour should start at depot city 0")
        self.assertEqual(self.tour[-1], 0, "The tour should end at depot city 0")

    def test_exact_six_cities_visited(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 6, "The tour should visit exactly 6 cities including depot")

    def test_distance_calculation(self):
        computed_cost = 0
        for i in range(len(self.tour)-1):
            city1 = self.tour[i]
            city2 = self.tour[i+1]
            computed_cost += calculate_euclidean_distance(*self.cities[city1], *self.cities[city2])
        # Allow small floating point error margin
        self.assertAlmostEqual(computed_cost, self.total_cost, places=2, msg="The total travel cost should match the given total")

    def test_output_format(self):
        self.assertIsInstance(self.tour, list, "Tour should be output as a list")
        self.assertIsInstance(self.total_cost, float, "Total cost should be output as a float")

# Additional testing or implementation would be required here to directly test [Requirement 6], 
# regarding the use of the specific GVNS algorithm, which often involves examination of the algorithmic implementation itself.

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)