import math
import unittest

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour(tour, cities):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if all cities are visited exactly once
    visited = set(tour)
    if visited != set(range(len(cities))):
        return False
    
    return True

def calculate_total_cost(tour, cities):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    return total_cost, max_distance

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (50, 42), 1: (41, 1), 2: (18, 46),
            3: (40, 98), 4: (51, 69), 5: (47, 39),
            6: (62, 26), 7: (79, 31), 8: (61, 90),
            9: (42, 49)
        }
        self.tour = [0, 9, 4, 8, 3, 2, 5, 6, 7, 1, 0]
        self.expected_total_cost = 292.55
        self.expected_max_distance = 56.46

    def test_tour_validation(self):
        result = check_tour(self.tour, self.cities)
        self.assertTrue(result)

    def test_total_travel_cost(self):
        total_cost, max_distance = calculate_total_cost(self.tour, [self.cities[i] for i in range(len(self.cities))])
        self.assertAlmostEqual(total_cost, self.expected_total_cost, places=2)

    def test_max_distance_between_consecutive_cities(self):
        _, max_distance = calculate_total_cost(self.tour, [self.cities[i] for i in range(len(self.cities))])
        self.assertAlmostEqual(max_distance, self.expected_max_distance, places=2)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestSolution))

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")