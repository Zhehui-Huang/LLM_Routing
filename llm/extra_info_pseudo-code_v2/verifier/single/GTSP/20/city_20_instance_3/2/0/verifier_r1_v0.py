import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tour(cities, city_groups, tour, expected_cost):
    # Verify start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Extract tour cities excluding the depot (start and end)
    visited_cities = tour[1:-1]
    
    # Verify one city per group and all belong to the groups
    selected_groups = set()
    for city in visited_cities:
        found = False
        for i, group in enumerate(city_groups):
            if city in group:
                if i in selected_groups:
                    return False  # city group already selected
                selected_groups.add(i)
                found = True
                break
        if not found:
            return False  # city not found in any group
    
    if len(selected_groups) != len(city_groups):
        return False  # not all groups are visited
    
    # Calculate the actual travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        actual_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
    
    # Check if the cost matches (within a small tolerance due to floating point calculations)
    if not math.isclose(actual_cost, expected_cost, rel_tol=1e-9):
        return False
    
    return True

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        city_locations = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
                          (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
                          (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
                          (53, 76), (19, 72)]
        city_groups = [[4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]]
        given_tour = [0, 19, 6, 2, 13, 12, 18, 0]
        given_total_cost = 158.66
        
        self.assertTrue(verify_tour(city_locations, city_groups, given_tour, given_total_cost))

if __name__ == '__main__':
    unittest.main()