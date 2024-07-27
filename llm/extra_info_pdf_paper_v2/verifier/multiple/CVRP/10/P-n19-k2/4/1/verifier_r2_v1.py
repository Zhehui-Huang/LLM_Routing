import unittest
from math import sqrt

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
            16: (62, 63), 17: (63, 69), 18: (45, 35)
        }
        self.demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
        self.tours = [
            [0, 16, 8, 3, 17, 13, 9, 12, 14, 11, 5, 7, 0],
            [0, 4, 15, 10, 2, 18, 1, 6, 0]
        ]
        self.robot_capacities = [160, 160]

    def test_city_counts(self):
        self.assertEqual(len(self.coordinates), 19)

    def test_demands_are_met(self):
        for tour in self.tours:
            load = sum(self.demands[city] for city in tour if city != 0)
            self.assertLessEqual(load, max(self.robot_capacities))

    def test_all_cities_delivered(self):
        all_cities = set(range(1, 19))
        delivered_cities = set(city for tour in self.tours for city in tour if city != 0)
        self.assertEqual(all_cities, delivered_cities)

    def test_tour_validity(self):
        initial_city = 0
        for tour in self.tours:
            self.assertEqual(tour[0], initial_city)
            self.assertEqual(tour[-1], initial_city)

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