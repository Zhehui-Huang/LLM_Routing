import unittest
import math

# Define the location of each city
city_locations = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), 
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), 
    (53, 76), (19, 72)
]

# Given solution tour and its costs
tour = [0, 0, 19, 1, 11, 9, 10, 14, 7, 0, 13, 6, 16, 5, 15, 4, 17, 3, 18, 2, 0, 12, 8, 1, 0, 0]
total_travel_cost = 982.4882770790441
max_distance_between_cities = 69.52697318307479

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city_locations[city1]
    x2, y2 = city_locations[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestTSPSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
    
    def test_each_city_visited_exactly_once(self):
        visits = [0] * len(city_locations)
        for city in tour:
            if city != 0:  # ignore the depot city repeated visits
                visits[city] += 1
        for i in range(1, len(visits)):
            self.assertEqual(visits[i], 1)

    def test_total_travel_cost(self):
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
        self.assertAlmostEqual(calculated_cost, total_travel_cost, places=5)

    def test_maximum_distance_between_cities(self):
        max_distance = 0
        for i in range(len(tour) - 1):
            distance = calculate_euclidean_distance(tour[i], tour[i + 1])
            if distance > max_distance:
                max_distance = distance
        self.assertAlmostEqual(max_distance, max_distance_between_cities, places=5)
    
    def test_tour_completeness(self):
        visited = set(tour)
        self.assertEqual(len(visited), len(city_locations))  # Including depot, should visit all

# Running the tests
if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # Method names in class TestTSPSolution that start with test
    tests = loader.loadTestsFromTestCase(TestTSPSolution)
    test_suite.addTests(tests)

    # Run tests
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")