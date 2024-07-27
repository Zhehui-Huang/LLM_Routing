import unittest
from math import sqrt

# Given cities coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# Solution provided
tour = [0, 6, 11, 2, 12, 1, 8, 4, 3, 13, 14, 7, 10, 5, 9, 0]
total_cost = 570.1589065502892
max_distance = 74.33034373659252

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTSPSolution(unittest.TestCase):
    def test_tour_validity(self):
        """ Check if each city is visited exactly once, and the tour starts and ends at city 0 """
        self.assertEqual(len(tour), len(cities) + 1)  # Check if tour length is correct (15 cities + return)
        self.assertEqual(tour[0], tour[-1])  # Tour should start and end at the depot
        self.assertCountEqual(tour[1:-1], list(cities.keys()))  # Each city visited once

    def test_total_travel_cost(self):
        """ Check if the calculated total travel cost matches the expected total cost """
        calculated_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(calculated_cost, total_question_cost, places=5)

    def test_max_distance_between_consecutive_cities(self):
        """ Check if the maximum distance between any two consecutive cities is as expected """
        calculated_max_distance = max(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(calculated_max_distance, max_distance, places=5)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")