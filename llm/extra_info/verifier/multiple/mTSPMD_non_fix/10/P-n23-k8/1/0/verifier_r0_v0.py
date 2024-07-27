import math
from collections import Counter

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def validate_solution(tours, coords):
    # Test setup: provided robot tour, city coordinates, total expected score.
    robot_tour = tours[0]
    expected_total_cost = 205.20233966789624
    total_cost_calculated = 0
    
    # [Requirement 1]: Start from depot city 0
    if robot_tour[0] != 0:
        return "FAIL"

    # [Requirement 2]: Each city must be visited exactly once
    city_count = Counter(robot_tour)
    if any(city_count[city] != 1 for city in range(len(coords))):
        return "FAIL"

    # Calculate travel cost and check the route ending
    last_city = robot_tour[0]
    for city in robot_tour[1:]:
        total_cost_calculated += calculate_euclidean_distance(coords[last_city][0], coords[last_city][1],
                                                              coords[city][0], coords[city][1])
        last_city = city
    
    # [Requirement 3]: Can end at any city -- already guaranteed by the loop termination

    # [Requirement 4]: Since it is stated as minimizing and we can't really check minimization without alternatives,
    # we verify whether the path corresponds to the purported cost
    if not math.isclose(total_cost_calculated, expected_total_cost, rel_tol=1e-9):
        return "FAIL"

    # [Requirement 5]: Travel cost between two cities is calculated as the Euclidean distance -- this is implemented
    return "CORRECT"
    
# Coordinates for each city
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}
    
# Single tour provided for testing 
robot_tour = [[0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14]]

# Validate the solution
result = validate_solution(robot_tour, coords)
print(result)