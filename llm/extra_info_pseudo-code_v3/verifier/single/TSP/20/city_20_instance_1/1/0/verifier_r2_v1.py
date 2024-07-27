import unittest
import math

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of cities including the depot city
        self.cities = [
            (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
            (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
            (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
            (50, 28), (69, 9)
        ]
        self.tour = [0, 6, 2, 9, 13, 12, 8, 1, 15, 19, 18, 17, 11, 10, 16, 4, 7, 5, 14, 3, 0]
        self.calculated_cost = 405.1098708113318
    
    def test_tour_starts_and_ends_at_depot(self):
        # Requirement 3
        self.assertEqual(self.tour[0], 0)  # Start at depot
        self.assertEqual(self.tour[-1], 0) # End at depot

    def test_visit_all_cities_exactly_once(self):
        # Requirement 1
        visits = set(self.tour[1:-1])  # Exclude the repeated depot city at the end for the check
        self.assertEqual(len(visits), 19)  # Should have visited all cities except the depot exactly once

    def test_travel_cost(self):
        # Requirement 2 & 6
        total_distance = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            total_distance += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(total_distance, self.calculated_cost, places=5)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVRPSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Execute the test function and print the result
output = run_tests()
print(output)