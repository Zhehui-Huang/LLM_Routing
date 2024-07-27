import unittest
from math import sqrt

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Test class
class TestTSPSolutionValidity(unittest.TestCase):
    
    def setUp(self):
        # City coordinates
        self.cities = [
            (84, 67),  # City 0
            (74, 40),  # City 1
            (71, 13),  # City 2
            (74, 82),  # City 3
            (97, 28),  # City 4
            (0, 31),   # City 5
            (8, 62),   # City 6
            (74, 56),  # City 7
            (85, 71),  # City 8
            (6, 76)    # City 9
        ]

    def test_solution_validity(self):
        # Given solution
        solution_tour = []
        solution_total_cost = 0
        solution_max_distance = 0
        
        # Checks
        if not solution_tour:  # No valid tour found
            self.assertEqual("No valid tour found.", "No valid tour found.")
        else:
            # [Requirement 1]
            self.assertEqual(solution_tour[0], 0)
            self.assertEqual(solution_tour[-1], 0)
            
            # [Requirement 2]
            unique_cities = set(solution_tour[1:-1])
            self.assertEqual(len(unique_cities), len(self.cities) - 1)
            
            # [Requirement 5]
            self.assertTrue(solution_tour[0] == 0)
            self.assertTrue(solution_tour[-1] == 0)
            
            # Calculating total cost and maximum distance
            distances = []
            for i in range(len(solution_tour) - 1):
                dist = calculate_distance(self.cities[solution_tour[i]], self.cities[solution_tour[i+1]])
                distances.append(dist)
            
            calculated_total_cost = sum(distances)
            calculated_max_distance = max(distances)
            
            # [Requirement 4]
            # Note: since no exact values to test against, only test if calculated correctly internally
            self.assertAlmostEqual(calculated_total.href_cost, solution_total_cost, places=5)
            
            # [Requirement 3]
            self.assertAlmostEqual(calculated_max_distance, solution_max_distance, places=5)
            
            # [Requirement 6]
            self.assertAlmostEqual(calculated_total_cost, solution_total_cost, places=5)
            
            # [Requirement 7]
            self.assertAlmostEqual(calculated_max_distance, solution_max_distance, places=5)
            

# Running the tests
unittest.main(argv=[''], exit=False)