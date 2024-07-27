import unittest
from math import sqrt

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities with their coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# City groups
city_groups = {
    0: [1, 6, 14], 1: [5, 12, 13], 2: [7, 10], 3: [4, 11], 4: [2, 8], 5: [3, 9]
}

# Provided tour and travel cost
tour = [0, 14, 5, 10, 11, 8, 9, 0]
reported_cost = 166.75801920718544

# Validate the provided solution
class TourTest(unittest.TestCase):

    def test_tour_start_end_depot(self):
        """ Test if the tour starts and ends at the depot (city 0) """
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_visit_one_from_each_group(self):
        """ Test if the tour visits exactly one city from each group """
        visited = set()
        for city in tour[1:-1]:  # exclude the starting and ending depot city
            for group_id, group in city-groups.items():
                if city in group:
                    visited.add(group_id)
                    break
        self.assertEqual(len(visited), len(city_groups))

    def test_output_format(self):
        """ Test output format, starts and ends with the depot city """
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_travel_cost(self):
        """ Test the total reported travel cost is correct """
        calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(calculated_cost, reported_cost, places=5)

# Run the tests
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TourTest))

runner = unittest.TextTestRunner()
result = runner.run(suite)

# Output based on the test results
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")