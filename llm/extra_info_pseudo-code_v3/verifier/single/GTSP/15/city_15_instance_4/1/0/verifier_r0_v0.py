import unittest
from math import sqrt

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        self.groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]
        self.solution_tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
        self.reported_cost = 220.73
        
    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_visits_one_from_each_group(self):
        visited_groups = []
        for city in self.solution_tour[1:-1]:  # Ignore the depot at start and end
            for i, group in enumerate(self.groups):
                if city in group:
                    visited_groups.append(i)
        self.assertEqual(len(set(visited_groups)), len(self.groups))
        self.assertEqual(sorted(visited_groups), list(range(len(self.groups))))

    def test_uses_euclidean_distance(self):
        calculated_cost = 0
        for i in range(len(self.solution_tour)-1):
            city1, city2 = self.solution_tour[i], self.solution_tour[i+1]
            calculated_cost += euclidean_extimate_distance(self.cities[city1], self.cities[city2])
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2)

    def test_output_format(self):
        self.assertIsInstance(self.solution_tour, list)
        self.assertTrue(all(isinstance(c, int) for c in self.solution_tour))
        self.assertIsInstance(self.reported_cost, float)

def euclidean_extimate_distance(point1, point2):
    """ Utility function to calculate Euclidean distance between two points """
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTourSolution)
    # We use TextTestRunner to execute the test and store the result
    result = unittest.TextTestRunner().run(suite)
    
    # Determine if all tests passed
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")