import unittest
from math import sqrt

def compute_euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour_solution(tour, total_cost):
    # Coordinates for each city index
    coordinates = {
        0: (8, 11), 
        1: (40, 6), 
        2: (95, 33), 
        3: (80, 60), 
        4: (25, 18), 
        5: (67, 23), 
        6: (97, 32), 
        7: (25, 71),
        8: (61, 16), 
        9: (27, 91), 
        10: (91, 46), 
        11: (40, 87), 
        12: (20, 97),
        13: (61, 25), 
        14: (5, 59), 
        15: (62, 88),
        16: (13, 43), 
        17: (61, 28), 
        18: (60, 63), 
        19: (93, 15)
    }

    # Check Requirement 1: Each city is visited exactly once, except depot
    visited = set(tour)
    if len(visited) != len(coordinates) or len(tour) != len(coordinates) + 1:
        return "FAIL"

    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Correct calculation of the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i+1]
        calculated_cost += compute_euclidean_distance(*(coordinates[city1]+coordinates[city2]))
    
    if not (abs(calculated_cost - total_cost) < 1e-4):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Unit test class
class TestTourSolution(unittest.TestCase):
    def test_solution(self):
        tour = [0, 4, 0]
        total_cost = 36.76955262170047
        result = validate_toursolution(tour, total_cost)
        self.assertEqual(result, "CORRECT")

# Run the tests
unittest.main(argv=[''], exit=False)