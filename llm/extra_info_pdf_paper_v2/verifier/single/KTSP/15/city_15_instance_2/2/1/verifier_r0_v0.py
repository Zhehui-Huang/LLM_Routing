import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

class TestKTSPSolution(unittest.TestCase):
    def test_tour(self):
        # Predefined city coordinates
        cities = {
            0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
            5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
            10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
        }

        # Solution provided
        tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
        expected_cost = 132.1185774560832

        # Requirement 1
        self.assertEqual(tour[0], 0, "Tour should start at city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at city 0")
        
        # Requirement 2
        self.assertEqual(len(set(tour)), 8, "Tour should include exactly 8 unique cities, including the depot")

        # Requirement 3
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        self.assertAlmostEqual(calculated_cost, expected_cost, places=5, msg="Calculated cost should match expected cost")

        # Requirement 4 & 5
        # Already captured by the logic but can be explicitly tested by verifying output format if needed
        # Here we are checking if the list indeed starts and ends with 0
        self.assertEqual(tour[0], 0, "Tour must start at city 0")
        self.assertEqual(tour[-1], 0, "Tour must end at city 0")
        # Total cost check is done in Requirement 3

        # All conditions must be accurate; print correct if all tests pass
        print("CORRECT")

# Execute the test case
unittest.main(argv=[''], exit=False)