import unittest
from math import sqrt

# Given cities and groups
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

groups = {
    0: [5, 6, 16], 1: [8, 18, 19], 2: [11, 12, 13], 
    3: [1, 3, 9], 4: [2, 4, 14], 5: [10, 17], 6: [7, 15]
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class TourVerificationTests(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
        self.expected_cost = 266.71610174713
    
    def test_tour_requirements(self):
        # Check if tour starts and ends at the depot city
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city.")

        # Check if exactly one city from each group is visited
        visited = set(self.tour[1:-1])  # Exclude depot city from visit check
        unique_groups_visited = set()
        for city in visited:
            for group_idx, group_cities in groups.items():
                if city in group_cities:
                    unique_groups_visited.add(group_idx)
        self.assertEqual(len(unique_groups_visited), len(groups), "Not all groups are visited by the robot.")

        # Check if the travel cost is minimized
        computed_cost = sum(calculate_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(computed_cost, self.expected_cost, delta=0.001, "Provided travel cost does not match computed cost.")
        
        # If all tests pass
        print("CORRECT")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TourVerificationTests('test_tour_requirements'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if not result.wasSuccessful():
        print("FAIL")

run_tests()