import unittest
import math

# Coordinates of the cities
cities = [
    (9, 93),   # 0 - Depot
    (8, 51),   # 1
    (74, 99),  # 2
    (78, 50),  # 3
    (21, 23),  # 4
    (88, 59),  # 5
    (79, 77),  # 6
    (63, 23),  # 7
    (19, 76),  # 8
    (21, 38),  # 9
    (19, 65),  # 10
    (11, 40),  # 11
    (3, 21),   # 12
    (60, 55),  # 13
    (4, 39)    # 14
]

def calculate_cost(tour):
    """Calculate the total Euclidean distance of the tour."""
    total_cost = 0.0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(total_cost, 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
        self.reported_cost = 373.97

    def test_start_and_end_at_depot(self):
        """Test if the tour starts and ends at the depot."""
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_all_cities_once(self):
        """Test if all cities are visited exactly once."""
        expected_cities = set(range(15))
        visited_cities = set(self.tour[:-1])  # Omit the last city as it's the return to the depot
        self.assertEqual(visited_cities, expected_cities)

    def test_total_travel_cost(self):
        """Test the correctness of the total travel cost."""
        calculated_cost = calculate_cost(self.tour)
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2)

    def test_output_format(self):
        """Test the output format requirement."""
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.reported_cost, float)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")
        
run_tests()