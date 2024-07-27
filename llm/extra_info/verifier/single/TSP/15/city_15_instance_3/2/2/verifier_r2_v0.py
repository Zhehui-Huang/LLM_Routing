import unittest
import math

# Provided city coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Tour provided as a solution
provided_tour = [0, 6, 13, 10, 9, 5, 14, 8, 11, 2, 7, 3, 12, 4, 1, 0]
provided_cost = 317.24

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_tour_distance(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

class TestTravelingSalesmanSolution(unittest.TestCase):
    def test_tour_start_and_end_at_depot(self):
        self.assertEqual(provided_tour[0], 0, "Tour should start at depot")
        self.assertEqual(provided_tour[-1], 0, "Tour should end at depot")
    
    def test_tour_visits_all_cities_once(self):
        visited_cities = sorted(provided_tour[1:-1])
        expected_cities = list(range(1, 15))
        self.assertEqual(visited_cities, expected_cities, "Tour should visit all cities exactly once")
    
    def test_tour_travel_cost(self):
        calculated_cost = calculate_total_tour_distance(provided_tour)
        self.assertAlmostEqual(calculated_cost, provided_cost, places=2, msg="Travel cost should be approximate to provided cost")
    
# Run the tests
if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestTravelingSalesmanSolution))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    print("CORRECT" if result.wasSuccessful() else "FAIL")