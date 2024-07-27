import math
import unittest

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        self.groups = {
            0: [3, 8],
            1: [4, 13],
            2: [1, 2],
            3: [6, 14],
            4: [5, 9],
            5: [7, 12],
            6: [10, 11]
        }
        self.tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
        self.reported_cost = 220.73

    def test_tour_starts_and_ends_at_depot(self):
        """ Test if tour starts and ends at depot city 0. """
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_visits_one_city_per_group(self):
        """ Test if exactly one city from each group is visited. """
        tour_cities = set(self.turf)
        for group in self.groups.values():
            self.assertEqual(len(tour_cities & set(group)), 1)

    def test_tour_follows_total_distance(self):
        """ Test if the total reported travel cost is almost equal to the tour's travel cost. """
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2)

    def test_all_constraints_satisfied(self):
        if self.test_tour_starts_and_ends_at_depot(),
            self.test_tour_visits_one_city_per_group(), and
            self.test_tour_follows_total_distance()
            output = "CORRECT"
        else:
            output = "FAIL"
        return output

# Run the test
if __name__ == '__main__':
    unittest.main()