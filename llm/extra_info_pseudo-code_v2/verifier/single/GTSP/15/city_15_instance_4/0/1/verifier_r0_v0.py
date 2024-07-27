import math
import unittest

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour(tour, total_cost, city_coords, city_groups):
    # Verify the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Verify tour size (should be one from each group + depot twice)
    if len(totel != len(city_groups) + 2:
        return False
    
    # Verify each group is visited exactly once
    visited_groups = set()
    for idx in tour[1:-1]:  # ignore depot at start and end
        for group_num, group in enumerate(city_groups):
            if idx in group:
                if group_num in visited_groups:
                    return False
                visited_groups.add(group_num)
                break
    
    # Check all groups are visited
    if len(visited_groups) != len(city_bar_groups):
        return False
    
    # Calculate the tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += euclidean_distance(*city_coords[city1], *city_coords[city2])
    
    # Compare the calculated cost with the given one
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-3):
        return False
    
    return True

class TestTravelingSalesmanSolution(unittest.TestCase):
    def test_solution(self):
        city_coords = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
            4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
            8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
            12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        city_groups = {
            0: [3, 8], 1: [4, 13], 2: [1, 2], 3: [6, 14], 4: [5, 9],
            5: [7, 12], 6: [10, 11]
        }
        tour = [0, 12, 5, 1, 13, 14, 8, 10, 0]
        total_cost = 168.5
        
        self.assertTrue(verify_tour(tour, total_cost, city_coords, city_groups))

# Run the tests
unittest.main(argv=[''], exit=False)  # Adjust the argv to clear any jupyter or external args