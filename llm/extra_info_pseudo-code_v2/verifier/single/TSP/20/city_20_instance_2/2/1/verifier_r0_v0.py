import unittest
from math import sqrt

def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (3, 26),   # Depot city 0
            (85, 72),  # City 1
            (67, 0),   # City 2
            (50, 99),  # City 3
            (61, 89),  # City 4
            (91, 56),  # City 5
            (2, 65),   # City 6
            (38, 68),  # City 7
            (3, 92),   # City 8
            (59, 8),   # City 9
            (30, 88),  # City 10
            (30, 53),  # City 11
            (11, 14),  # City 12
            (52, 49),  # City 13
            (18, 49),  # City 14
            (64, 41),  # City 15
            (28, 49),  # City 16
            (91, 94),  # City 17
            (51, 58),  # City 18
            (30, 48)   # City 19
        ]
        self.tour = [0, 12, 19, 16, 11, 14, 6, 8, 10, 3, 4, 7, 18, 13, 17, 1, 5, 15, 9, 2, 0]
        self.calculated_cost = 488.05845927119896
    
    def test_tour_starts_and_ends_at_depot(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_each_city_visited_exactly_once(self):
        # Requirement 2
        visited_cities = self.tour[1:-1]  # Exclude the return to the depot
        unique_cities = set(visited_cities)
        self.assertEqual(len(visited_cities), len(unique_cities))
        self.assertEqual(set(range(1, 20)), unique_cities)
    
    def test_travel_cost_calculation(self):
        # Requirement 3
        total_cost = sum(euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_cost, self.calculated_cost, places=5)
    
    # Requirement 4 (Using the Lin-Kernighan algorithm) cannot be tested without the implementation details
    
    def test_output_format(self):
        # Requirement 5
        print("Tour:", self.tour)
        print("Total travel cost:", self.calculated_cost)

# Run the tests
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)