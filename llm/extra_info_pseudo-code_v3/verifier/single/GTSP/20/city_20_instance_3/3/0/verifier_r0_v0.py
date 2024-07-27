import math
import unittest

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.cities = {
            0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
            5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
            10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
            15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
        }
        # City groups
        self.groups = {
            0: [4, 10, 13, 17],
            1: [6, 7, 14],
            2: [9, 12, 16],
            3: [2, 5, 15],
            4: [1, 3, 19],
            5: [8, 11, 18]
        }
        # Proposed solution tour and its total travel cost
        self.tour = [0, 4, 7, 12, 15, 3, 18, 0]
        self.reported_cost = 227.40
    
    def calculate_distance(self, c1, c2):
        """ Helper to calculate Euclidean distance between two cities. """
        x1, y1 = self.cities[c1]
        x2, y2 = self.cities[c2]
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    def test_cities_in_tour(self):
        """ Test if only one city from each group is visited and tour starts/ends at depot. """
        # Check if ending and starting city is the depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
        # Check if one city from each group is in the tour
        for group, cities in self.groups.items():
            self.assertEqual(len(set(self.tour) & set(cities)), 1)
        
    def test_correct_costs(self):
        """ Test if the total travel cost is calculated correctly and matches the expected cost."""
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += self.calculate_distance(self.tour[i], self.tour[i+1])
        calculated_cost = round(calculated_cost, 2)
        self.assertEqual(calculated_cost, self.reported_cost)
        
    def test_solution(self):
        """ Run all tests """
        self.test_cities_in_tour()
        self.test_correct_costs()

# Creating a test suite and adding tests
suite = unittest.TestSuite()
suite.addTest(TestTravelingSalesmanSolution('test_solution'))

# Test runner
runner = unittest.TextTestRunner()
result = runner.run(suite)

# Based on the results, output "CORRECT" or "FAIL"
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")