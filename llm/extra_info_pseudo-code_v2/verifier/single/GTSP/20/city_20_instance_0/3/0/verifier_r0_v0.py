import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_requirements(tour, cities, groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Start and end city should be the depot city 0
    
    visited_groups = set()
    for city_index in tour[1:-1]:  # Exclude the first and last index (depot)
        for i, group in enumerate(groups):
            if city_index in group:
                visited_groups.add(i)
                break
    
    if len(visited_groups) != len(groups):
        return "FAIL"  # Must visit at least one city from each group
    
    # Calculate the total travel cost from the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    actual_cost = 191.98723836274047  # Provided expected result
    if abs(total_cost - actual_cost) > 1e-5:  # Allowing some floating point tolerance
        return "FAIL"
    
    return "CORRECT"

class TestSolution(unittest.TestCase):
    def test_solution(self):
        cities = {
            0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 
            5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 
            10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 
            15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
        }
        groups = {
            0: [1, 3, 5, 11, 13, 14, 19],
            1: [2, 6, 7, 8, 12, 15],
            2: [4, 9, 10, 16, 17, 18]
        }
        
        proposed_tour = [0, 1, 8, 17, 2, 4, 0]
        result = check_requirements(proposed_tours, cities, groups)
        self.assertEqual(result, "CORRECT")

if __name__ == '__main__':
    unittest.main()