import unittest
from typing import List
from math import sqrt

def calculate_euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return total_cost

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
            (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
            (83, 96), (60, 50), (98, 1)
        ]
        self.tour = [0, 3, 9, 10, 4, 12, 11, 2, 8, 14, 7, 1, 6, 13, 5, 0]
        self.reported_cost = 409.1088687629702

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_all_cities_once(self):
        all_cities = set(range(15))
        visited_cities = set(self.tour)
        self.assertEqual(visited_cities, all_cities)

    def test_travel_cost_calculation(self):
        calculated_cost = calculate_total_travel_cost(self.tour, self.cities)
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTour))
    runner = unittest.TextTestRunner()
    test_result = runner.run(test_suite)
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")