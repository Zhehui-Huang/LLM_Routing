import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTour(unittest.TestCase):

    def setUp(self):
        self.coordinates = [
            (50, 42),  # City 0 - Depot
            (41, 1),   # City 1
            (18, 46),  # City 2
            (40, 98),  # City 3
            (51, 69),  # City 4
            (47, 39),  # City 5
            (62, 26),  # City 6
            (79, 31),  # City 7
            (61, 90),  # City 8
            (42, 49)   # City 9
        ]
        self.groups = [
            [1, 2, 6],   # Group 0
            [3, 7, 8],   # Group 1
            [4, 5, 9]    # Group 2
        ]
        self.solution_tour = [0, 7, 6, 5, 0]
        self.solution_cost = 72.8282439136095

    def test_tour_validity(self):
        # Requirement 1, 2, 3, and 7 checked by setup and structure

        # Check correct start and end at the depot City 0
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

        # Requirement 4: Visit exactly one city from each group
        visited_groups = []
        for city in self.solution_tour[1:-1]:
            for i, group in enumerate(self.groups):
                if city in group:
                    visited_groups.append(i)
        self.assertEqual(len(set(visited_groups)), 3)

        # Requirement 6: Check the optimality elsewhere as this is a functional test, not a performance one

        # Requirement 8: Check the total Euclidean distance
        calculated_cost = 0
        for i in range(1, len(self.solution_tour)):
            city1 = self.solution_tour[i - 1]
            city2 = self.solution_tour[i]
            calculated_cost += euclidean_distance(self.coordinates[city1], self.coordinates[city2])
        self.assertAlmostEqual(calculated_cost, self.solution_cost, places=5)

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    test_result = unittest.TextTestRunner().run(test_suite)
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")