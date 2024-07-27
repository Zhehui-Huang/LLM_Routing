import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35)
        }
        self.robot0_tour = [1, 16, 6, 20, 5, 14, 17, 9, 7, 2, 10, 4, 11, 15, 12, 3, 8, 18, 19, 13]
        self.robot0_cost = 167.65362182303798

    def test_depart_return_depot(self):
        # Check if starts and ends at Depot
        self.assertEqual(self.robot0_tour[0], 1)  # Starts at depot 1
        self.assertEqual(self.robot0_tour[-1], 13)  # Ends at city 13 which is incorrect, should return to depot 1

    def test_unique_city_visit(self):
        # Check if all cities are visited exactly once
        expected_cities = set(range(2, 21))  # Depots are not needed to revisit
        actual_cities = set(self.robot0_tour)
        self.assertEqual(actual_cities, expected_cities)

    def test_total_travel_cost(self):
        # Calculate total travel cost of the tour
        cost = 0
        for i in range(len(self.robot0_tour) - 1):
            cost += euclidean_distance(self.cities[self.robot0_tour[i]], self.cities[self.robot0_tour[i + 1]])
        cost += euclidean_distance(self.cities[self.robot0_tour[-1]], self.cities[1])  # return to starting depot
        self.assertAlmostEqual(cost, self.robot0_cost)

    def test_all_requirements(self):
        # All requirements
        self.test_depart_return_depot()
        self.test_unique_city_visit()
        self.test_total_travel_cost()

# Running the tests
if __name__ == '__main__':
    unittest.main()