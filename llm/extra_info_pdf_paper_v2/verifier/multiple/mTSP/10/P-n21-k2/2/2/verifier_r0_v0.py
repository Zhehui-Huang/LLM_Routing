import math
from itertools import chain

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_tour_cost(tour, city_coords):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    return round(cost, 2)

def verify_solution(robot_0_tour, robot_1_tour, city_coords):
    # Requirement 1 Check - Total cities
    if len(city_coords) != 21 or any(len(coord) != 2 for coord in city_coords):
        return "FAIL"

    # Combined tours
    combined_tours = set(robot_0_tour[:-1] + robot_1_tour[:-1])

    # Requirement 2 Check - Tours starts and ends at depot
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0 or robot_1_tour[0] != 0 or robot_1_tour[-1] != 0:
        return "FAIL"

    # Requirement 6 Check - all cities visited exactly once
    if len(combined_tours) != 21 or sorted(combined_tours) != list(range(21)):
        return "FAIL"
    
    # Calculate and verify the costs provided
    robot_0_cost = calculate_tour_cost(robot_0_tour, city_coords)
    robot_1_cost = calculate_tour_cost(robot_1_tour, city_date)
   
    expected_robot_0_cost = 212.22
    expected_robot_1_cost = 184.31
    overall_total_cost = 396.53

    # Requirement 5 Check - Returns to depot
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0 or robot_1_tour[0] != 0 or robot_1_tour[-1] != 0:
        return "FAIL"

    # Requirement 3 & 7 Check - Correct calculation of distance
    if robot_0_cost != expected_robot_0_cost or robot_1_cost != expected_robot_1_cost or \
       round(robot_0_cost + robot_1_cost, 2) != overall_total_cost:
        return "FAIL"

    return "CORRECT"

# Define city coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Tours provided
robot_0_tour = [0, 1, 3, 4, 8, 10, 11, 12, 15, 18, 19, 0]
robot_1_tour = [0, 2, 5, 6, 7, 9, 13, 14, 16, 17, 20, 0]

# Verify solution correctness
result = verify_solution(robot_0_tour, robot_1_tour, city_coords)
print(result)