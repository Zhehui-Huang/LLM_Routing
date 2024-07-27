import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

class TestTravelingSalesmanSolution(unittest.TestCase):
    
    def setUp(self):
        self.coordinates = [
            (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
            (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
            (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
            (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
        ]
        self.tour = [0, 6, 2, 19, 15, 18, 17, 12, 13, 8, 9, 11, 10, 16, 4, 7, 5, 14, 3, 1, 0]
        self.calculated_cost = 610.8605077173856

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_all_cities_exactly_once(self):
        sorted_cities = sorted(self.tour)
        expected_cities = list(range(0, 20))
        expected_cities.append(0)  # Adding depot city again as it should return to start.
        self.assertEqual(sorted_cities, expected_cities)

    def test_calculated_distance(self):
        total_distance = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            total_distance += euclidean_distance(self.coordinates[city1], self.coordinates[city2])
        self.assertAlmostEqual(total_distance, self.calculated_cost)

# Setup test suite and run the tests
suite = unittest.TestSuite()
suite.addTest(TestTravelingSalesmanSolution('test_tour_starts_and_ends_at_depot'))
suite.addTest(TestTravelingSalesmanSolution('test_visit_all_cities_exactly_once'))
suite.addTest(TestTravelingSalesmanSolution('test_calculated_distance'))

runner = unittest.TextTestRunner()
result = runner.run(suite)

# Checking if all tests passed
if len(result.failures) == 0 and len(result.errors) == 0:
    print("CORRECT")
else:
    print("FAIL")