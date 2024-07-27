import unittest
from math import sqrt

# Coordinates of all cities including depots
cities = {
    0: (30, 40),  1: (37, 52),  2: (49, 43),  3: (52, 64),  4: (31, 62),
    5: (52, 33),  6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Solution provided
solution = {
    "Robot 0": {
        "tour": [0, 6, 18, 5, 7, 2, 1, 10, 11, 4, 14, 12, 3, 8, 16, 17, 9, 15, 13, 0],
        "cost": 205.16651737648868
    },
    "Robot 1": {
        "tour": [1, 4, 11, 14, 12, 3, 16, 17, 8, 9, 15, 13, 5, 7, 2, 18, 6, 0, 10, 1],
        "cost": 181.5881391145628
    },
    "overall_cost": 386.7546564910515
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

class TestTSPSolution(unittest.TestCase):

    def test_all_cities_visited_once_and_route_validity(self):
        visited_cities = set()
        for robot, data in solution.items():
            if robot == 'overall_cost':
                continue
            tour = data['tour']
            # Check the tour starts and ends at the robot's designated depot
            self.assertTrue(tour[0] == tour[-1])
            self.assertIn(tour[0], (0, 1))
            # Check all cities in the tour are valid and count them
            for i in range(len(tour)):
                self.assertIn(tour[i], cities)
                visited_cities.add(tour[i])
        # Ensure all cities including depots are visited exactly once
        self.assertEqual(len(visited_cities), len(cities))

    def test_costs(self):
        calculated_costs = {}
        for robot, data in solution.items():
            if robot == 'overall_cost':
                continue
            tour = data['tour']
            total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            calculated_costs[robot] = total_cost
            # Check individual robot tour costs match given cost
            self.assertAlmostEqual(data['cost'], total_cost, places=5)

        # Check overall cost
        total_calculated_cost = sum(calculated_costs.values())
        self.assertAlmostEqual(solution['overall_cost'], total_calculated_cost, places=5)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_all_cities_visited_once_and_route_validity'))
    suite.addTest(TestTSPUtility('test_costs'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Run the tests
test_result = test_suite()
print(test_result)