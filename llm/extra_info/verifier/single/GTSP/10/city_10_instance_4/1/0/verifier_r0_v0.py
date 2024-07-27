import math
import unittest

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, city_positions, city_groups):
    # Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if tour visits exactly one city from each group
    visited_group_ids = set()
    for city_index in tour[1:-1]:
        for group_id, cities in enumerate(city_groups):
            if city_index in cities:
                if group_id in visited_group_ids:
                    return False
                visited_group_ids.add(group_id)
                break
    
    if len(visited_group_ids) != len(city_groups):
        return False
    
    # Compute the total travel cost and compare with given value
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        city_a = city_positions[tour[i]]
        city_b = city_positions[tour[i + 1]]
        total_travel_cost += calculate_distance(city_a, city_b)
    
    expected_total_travel_cost = 371.19  # Provided as expected result
    if not math.isclose(total_travel_cost, expected_total_travel_path, rel_tol=1e-2):
        return False
    
    return True

class TestTourSolution(unittest.TestCase):
    def test_tour_and_cost(self):
        city_positions = {
            0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 
            4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70), 
            8: (20, 99), 9: (66, 62)
        }
        
        city_groups = [
            [1, 4], [2, 6], [7], [5], [9], [8], [3]
        ]
        
        tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
        
        correct = validate_solution(tour, city_positions, city_groups)
        
        self.assertTrue(correct, "The solution should meet all the problem constraints")

# Running the test
suite = unittest.TestLoader().loadTestsFromTestCase(TestTourSolution)
unittest.TextTestRunner().run(suite)