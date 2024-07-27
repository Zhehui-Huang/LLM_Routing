import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
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
        self.robot0_tour = [1] + [16, 6, 20, 5, 14, 17, 9, 7, 2, 10, 4, 11, 15, 12, 3, 8, 18, 19, 13] + [1]
        self.robot0_cost = 167.65362182303798

    def test_depart_return_depot(self):
        """ Test if the tour starts and ends at the designated depot. """
        self.assertEqual(self.robot0_tour[0], 1)  # Starts at depot 1
        self.assertEqual(self.robot0_tour[-1], 1)  # Ends at depot 1

    def test_unique_city_visit(self):
        """ Test if all cities are visited exactly once excluding depots. """
        cities_visited = self.robot0_tour[1:-1]
        self.assertEqual(len(set(cities_visited)), 19)
        self.assertEqual(len(cities_visited), 19)

    def test_total_travel_cost(self):
        """ Calculating and verifying the total travel cost of the tour. """
        total_cost = sum(euclidean_distance(self.cities[self.robot0_tour[i]], self.cities[self.robot0_tour[i + 1]])
                         for i in range(len(self.robot0_tour) - 1))
        self.assertAlmostEqual(total_cost, self.robot0_cost, places=5)

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)