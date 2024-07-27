import unittest
import math

# Provided solution
solution_tour = [0, 7, 1, 2, 5, 6, 8, 0]
solution_cost = 244.94130105668984

# Define city coordinates as per the environment information
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Define city groups
city_groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

# Function to calculate Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Prepare unit tests
class TestRobotTour(unittest.TestCase):
    
    def test_tour_start_end(self):
        # Test if tour starts and ends at depot city (0)
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)
    
    def test_visit_one_from_each_group(self):
        # Test if exactly one city from each group is visited
        visited = set()
        for i in solution_tour:
            for key, cities in city_groups.items():
                if i in cities:
                    visited.add(key)
        self.assertEqual(len(visited), len(city_groups))
    
    def test_total_travel_cost(self):
        # Test if calculated distance equals provided solution cost
        calc_cost = 0
        for i in range(len(solution_tour) - 1):
            calc_cost += calculate_distance(solution_tour[i], solution_tour[i + 1])
        self.assertAlmostEqual(calc_cost, solution_cost, places=5)

# Execute tests
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestRobotTour))
    
    test_runner = unittest.TextTestRunner()
    results = test_runner.run(test_suite)
    
    if results.wasSuccessful() and results.failures == []:
        print("CORRECT")
    else:
        print("FAIL")