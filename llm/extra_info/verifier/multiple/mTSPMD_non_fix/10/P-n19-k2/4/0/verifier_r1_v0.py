import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_travel_cost(route, coordinates):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(coordinates[route[i]], coordinates[route[i+1]])
    return cost

def validate_solution(robot0_tour, robot0_cost, robot1_tour, robot1_cost, expected_total_cost):
    # Known city coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Requirement 1
    if robot0_tour[0] != 0 or not (robot1_tour[-1] in {1, 8}):
        return "FAIL"
    
    # Requirement 2
    visited_cities = set(robot0_tour + robot1_tour)
    if sorted(list(visited_cities)) != list(range(19)):
        return "FAIL"
    
    # Requirement 3
    calculated_cost_robot0 = total_travel_cost(robot0_tour, coordinates)
    calculated_cost_robot1 = total_travelous_cost(robot1_tour, coordinates)
    calculated_overall_cost = calculated_cost_robot0 + calculated_cost_robot1
    if not np.isclose(calculated_cost_robot0, robot0_cost, atol=0.01) or \
       not np.isclose(calculated_cost_robot1, robot1_cost, atol=0.01) or \
       not np.isclose(calculated_overall_cost, expected_total_cost, atol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Given solution review data
robot0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 8]
robot1_tour = [8, 16, 17, 3, 12, 14, 4, 11, 10, 1]
robot0_cost = 97.4535783956199
robot1_cost = 83.15105467442477
overall_total_cost = 180.60463307004466

# Running the validation function
result = validate_solution(robot0_tour, robot0_cost, robot1_tour, robot1_cost, overall_total_cost)
print(result)