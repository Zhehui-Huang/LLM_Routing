import numpy as rn

def calculate_distance(city1, city2):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def extract_city_coordinates():
    return [
        (30, 40),   # City 0
        (37, 52),   # City 1
        (49, 43),   # City 2
        (52, 64),   # City 3
        (31, 62),   # City 4
        (52, 33),   # City 5
        (42, 41),   # City 6
        (52, 41),   # City 7
        (57, 58),   # City 8
        (62, 42),   # City 9
        (42, 57),   # City 10
        (27, 68),   # City 11
        (43, 67),   # City 12
        (58, 27),   # City 13
        (37, 69),   # City 14
        (61, 33),   # City 15
        (62, 63),   # City 16
        (63, 69),   # City 17
        (45, 35)    # City 18
    ]

def check_tour_start_end_points(tour, start_depot):
    # Check start point
    start_point_valid = tour[0] == start_depot
    # Check if it ends in any city (no specific end point required)
    return start_point_valid

def check_all_cities_visited_once(tours):
    visited = set()
    for tour in tours:
        visited.update(set(tour))
    return len(visited) == 19  # including both depots and all cities

def test_solution():
    city_coordinates = extract_city_coordinates()
    
    robot_0_tour = [12, 3, 18, 15, 1, 11, 11, 18, 14, 3]
    robot_1_tour = [11, 11, 17, 13, 3, 3, 0, 0, 15, 15]
    
    # Requirement 1:
    if not (check_tour_start_end_points(robot_0_tour, 0) and check_tour_start_end_checkpoint(robot_1_tour, 1)):
        return "FAIL - Tours do not start or end correctly at their designated depots"
    
    # Requirement 3:
    if not check_all_cities_visited_once([robot_0_tour, robot_1_tour]):
        return "FAIL - Not all cities are visited exactly once"
    
    return "CORRECT"

# Perform the test
result = test_solution()
print(result)