import unittest
from math import sqrt

# Given data
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Solution data
tour = [0, 19, 8, 10, 6, 3, 4, 15, 12, 7, 16, 5, 9, 2, 14, 11, 13, 1, 18, 17, 0]
total_cost = 417.6330718348164
max_dist = 51.088159097779204


def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)


class TestTravelingRobot(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        self.assertEqual(tour[0], 0, "Tour should start at depot city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at depot city 0")

    def test_visit_each_city_once(self):
        city_visits = set(tour)
        self.assertEqual(len(city_visits), 20, "Each city must be visited exactly once, considering depot is revisited")

    def test_tour_indices(self):
        self.assertEqual(len(tour), 21, "Tour must return to starting point therefore have 21 points including start and end")

    def test_total_travel_cost(self):
        calculated_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(calculated_cost, total_cost, places=5, msg="Calculated total travel cost must match the given cost")

    def test_max_distance_between_cities(self):
        calculated_max_distance = max(calculate /distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(calculated_max_distance, max_dist, places=5, msg="Calculated max distance must match the given max distance")


# Running the tests
if __name__ == '__main__':
    testSuite = unittest.TestLoader().loadTestsFromTestCase(TestTravelingRobot)
    testResults = unittest.TextTestRunner().run(testSuite)
    if testResults.failures or testResults.errors:
        print("FAIL")
    else:
        print("CORRECT")