import math
import unittest

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
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
        self.groups = {
            0: [7, 9],
            1: [1, 3],
            2: [4, 6],
            3: [8],
            4: [5],
            5: [2]
        }
        self.tour = [0, 5, 6, 8, 3, 7, 2, 0]
        self.reported_distance = 341.1327378493923

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visits_one_city_from_each_group(self):
        visited = {}
        for city in self.tour:
            for group, cities in self.groups.items():
                if city in cities:
                    visited[group] = visited.get(group, 0) + 1
        self.assertTrue(all(count == 1 for count in visited.values()))

    def test_correct_calculation_of_travel_cost(self):
        total_cost = 0
        for i in range(1, len(self.tour)):
            total_cost += euclidean
            _distance(self.cities[self.tour[i-1]], self.cities[self.tour[i]])
        self.assertAlmostEqual(self.reported_distance, total_cost, places=5)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRobotTourSolution))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()