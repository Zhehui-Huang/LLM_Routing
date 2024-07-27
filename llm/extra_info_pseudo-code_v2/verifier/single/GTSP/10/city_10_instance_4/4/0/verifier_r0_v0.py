import unittest
from math import sqrt

# Function to calculate the Euclidean distance between two points
def calculate_distance(city1, city2):
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Class to perform the unit tests
class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
            5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
        }
        self.groups = {
            0: [1, 4], 1: [2, 6], 2: [7], 3: [5], 4: [9], 5: [8], 6: [3]
        }
        self.tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
        self.reported_cost = 371.19

    def test_start_end_depot(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_one_from_each_group(self):
        # Requirement 3
        visited = set(self.tour[1:-1])  # all visited cities except the start/end depot
        unique_group_count = 0
        
        for group in self.groups.values():
            if any(city in visited for city in group):
                unique_group_count += 1
                
        self.assertEqual(unique_group_count, len(self.groups))

    def test_tour_output_format(self):
        # Requirement 4
        self.assertIsInstance(self.tour, list)  # should be a list
        self.assertIsInstance(self.reported_cost, float)  # should be a number (float)

    def test_total_travel_cost(self):
        # Requirement 5
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])

        # Allow some tolerance for floating point arithmetic issues
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2)

    def test_solution(self):
        try:
            self.test_start_end_depot()
            self.test_visit_one_from_each_group()
            self.test_tour_output_format()
            self.test_total_travel_cost()
            result = "CORRECT"
        except AssertionError:
            result = "FAIL"
        print(result)

# Execute the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)