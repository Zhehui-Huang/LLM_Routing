import unittest
import math

# Constants for the test
CITIES = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

TOUR = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
TOTAL_COST = 322.5037276986899
MAX_DISTANCE = 64.66065264130884

def euclidean_distance(city1, city2):
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTSPSolution(unittest.TestCase):
    def test_start_end_depot(self):
        self.assertEqual(TOUR[0], 0, "Tour should start at the depot")
        self.assertEqual(TOUR[-1], 0, "Tour should end at the depot")
    
    def test_unique_visit(self):
        unique_cities = set(TOUR)
        self.assertEqual(len(unique_cities), 15, "All cities must be visited exactly once")
        self.assertEqual(unique_cities, set(CITIES.keys()), "All cities must be covered")
    
    def test_travel_cost_and_max_distance(self):
        total_cost_calculated = 0
        max_distance_calculated = 0
        for i in range(len(TOUR) - 1):
            distance = euclidean_distance(TOUR[i], TOUR[i+1])
            total_cost_calculated += distance
            if distance > max_distance_calculated:
                max_distance_calculated = distance
        self.assertAlmostEqual(total_cost_calculated, TOTAL_COST, places=5, msg="Total cost should match calculated total cost")
        self.assertAlmostEqual(max_distance_calculated, MAX_DISTANCE, places=5, msg="Max distance should match calculated max distance")

def main():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()