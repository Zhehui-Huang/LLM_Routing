import unittest
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

class TestSolutionVerification(unittest.TestCase):
    
    def setUp(self):
        self.coordinates = [
            (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
            (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
            (75, 9), (52, 54), (64, 72), (14, 89)
        ]
        self.groups = [[5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]]
        self.solution_tour = [0, 13, 1, 14, 17, 8, 6, 15, 0]
        self.reported_cost = 229.03

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_tour_contains_one_city_from_each_group(self):
        tour_cities = self.solution_tour[1:-1]  # exclude the depot city at start and end
        visited_groups = set()
        for city in tour_cities:
            for idx, group in enumerate(self.groups):
                if city in group:
                    visited_groups.add(idx)
                    break
        self.assertEqual(len(visited_groups), len(self.groups))

    def test_tour_cost_calculation(self):
        calculated_cost = calculate_total_distance(self.solution_tour, self.coordinates)
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSolutionVerification('test_tour_start_end_at_depot'))
    suite.addTest(TestSolutionVerification('test_tour_contains_one_city_from_each_group'))
    suite.addTest(TestSolutionEachToTh("test_tour_cost_calculation"))
    return suite

runner = unittest.TextTestRunner()
result = runner.run(suite())

if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")