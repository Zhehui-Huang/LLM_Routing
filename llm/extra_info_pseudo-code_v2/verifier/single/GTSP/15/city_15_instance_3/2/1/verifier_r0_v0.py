import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # City coordinates
        self.cities = {
            0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 
            4: (54, 93), 5: (34, 73), 6: (6, 61), 7: (86, 69), 
            8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30), 
            12: (70, 95), 13: (29, 64), 14: (32, 79)
        }
        # Groups of cities
        self.groups = [
            [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], 
            [2, 8], [3, 9]
        ]
        # Provided solution tour and its cost
        self.tour = [0, 10, 11, 2, 3, 12, 1, 0]
        self.reported_cost = 238.9111036098412

    def euclidean_distance(self, city_a, city_b):
        return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)
    
    def calculate_total_cost(self, tour):
        total_cost = 0
        for i in range(1, len(tour)):
            total_cost += self.euclidean_distance(self.cities[tour[i-1]], self.cities[tour[i]])
        return total_cost
    
    def test_tour_begins_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at depot city")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city")

    def test_tour_visits_one_city_from_each_group(self):
        visited_groups = []
        for city in self.tour[1:-1]:  # Exclude the depot city at start and end
            for index, group in enumerate(self.groups):
                if city in group:
                    visited_groups.append(index)
        unique_groups_visited = len(set(visited_groups))
        self.assertEqual(unique_groups visited, len(self.groups), f"Tour should visit one city from each of the {len(self.groups)} groups")

    def test_total_travel_cost(self):
        calculated_cost = self.calculate_total_cost(self.tour)
        # Allow a small margin for floating point precision issues
        self.assertAlmostEqual(calculated_cost, self.reported_cost, delta=0.001, msg="Reported travel cost does not match calculated cost")
    
    def runAllTests(self):
        self.setUp()
        self.test_tour_begins_and_ends_at_depot()
        self.test_tour_visits_one_city_from_each_group()
        self.test_total_travel_cost()
        print("CORRECT")

# Running the tests
try:
    TestTourSolution().runAllTests()
except AssertionError as e:
    print("FAIL: ", str(e))