import math
import unittest

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour(tour, total_cost, city_coords, city_groups):
    # Verify the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Verify each group is visited exactly once
    visited_groups = set()
    for idx in tour[1:-1]:  # ignore depot at start and end
        matched_group = False
        for group_num, group in enumerate(city_groups):
            if idx in group:
                if group_num in visited_groups:
                    return False
                visited_groups.add(group_num)
                matched_group = True
                break
        if not matched_group:
            return False
    
    # Check all groups are visited
    if len(visited_groups) != len(city_groups):
        return False
    
    # Calculate the tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_sum += euclidean_distance(*city_coords[city1], *city_coords[city2])
    
    # Compare the calculated cost with the given one
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-3):
        return False
    
    return True

class TestTravelingSalesmanSolution(unittest.TestCase):
    def test_solution(self):
        city_coords = [
            (35, 40), (39, 41), (81, 30), (5, 50),
            (72, 90), (54, 46), (8, 70), (97, 62),
            (14, 41), (70, 44), (27, 47), (41, 74),
            (53, 80), (21, 21), (12, 39)
        ]
        city_groups = [
            [3, 8], [4, 13], [1, 2], [6, 14], [5, 9],
            [7, 12], [10, 11]
        ]
        tour = [0, 12, 5, 1, 13, 14, 8, 10, 0]
        total_cost = 168.5
        
        self.assertTrue(verify_tour(tour, total_cost, city_coords, city_groups))

# Run the tests
unittest.main(argv=[''], exit=False)