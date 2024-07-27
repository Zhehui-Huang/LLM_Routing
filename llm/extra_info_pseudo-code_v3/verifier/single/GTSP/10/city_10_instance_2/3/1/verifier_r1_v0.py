import unittest
from math import sqrt

def calculate_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, groups, city_coords, expected_cost):
    # Verify tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Verify only one city from each group is visited
    visited_groups = []
    for city in tour[1:-1]:
        for group_index, group in enumerate(groups):
            if city in group:
                if group_index in visited_groups:
                    return False
                visited_groups.append(group_index)

    if len(visited_groups) != len(groups):
        return False
    
    # Verify the total travel cost
    actual_cost = 0
    for i in range(len(tour)-1):
        actual_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    
    if not (expected_cost - 0.01 <= actual_cost <= expected_cost + 0.01):
        return False
    
    return True

class TestSolution(unittest.TestCase):
    def test_solution(self):
        city_coords = [
            (90, 3),  # depot city 0
            (11, 17), # city 1
            (7, 27),  # city 2
            (95, 81), # city 3
            (41, 54), # city 4
            (31, 35), # city 5
            (23, 95), # city 6
            (20, 56), # city 7
            (49, 29), # city 8
            (13, 17)  # city 9
        ]
        groups = [
            [3, 6],  # Group 0
            [5, 8],  # Group 1
            [4, 9],  # Group 2
            [1, 7],  # Group 3
            [2]      # Group 4
        ]
        tour = [0, 6, 5, 9, 1, 2, 0]
        expected_cost = 185.15738901984233
        
        result = verify_tour(tour, groups, city_coords, expected_cost)
        self.assertTrue(result)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestSolution('test_solution'))
    test_result = unittest.TextTestRunner().run(test_suite)
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")