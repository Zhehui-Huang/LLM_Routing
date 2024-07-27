import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(cities_coordinates, robot_tours, expected_costs):
    # Unpack data
    robot_0_tour, robot_1_tour = robot_tours
    robot_0_cost, robot_1_cost, total_cost = expected_costs
    
    # Validate if all cities are visited exactly once
    all_cities = set(range(len(cities_coordinates)))
    visited_cities = set(robot_0_tour + robot_1_tour)
    if all_cities != visited_cities:
        return "FAIL"
    
    # Calculate costs for Robot 0
    robot_0_real_cost = sum(
        calculate_euclidean_distance(cities_coordinates[robot_0_tour[i]][0], cities_coordinates[robot_0_tour[i]][1], 
                                     cities_coordinates[robot_0_tour[i+1]][0], cities_coordinates[robot_0_tour[i+1]][1])
        for i in range(len(robot_0_tour) - 1)
    )
    
    # Calculate costs for Robot 1
    robot_1_real_cost = sum(
        calculate_euclidean_distance(cities_coordinates[robot_1_tour[i]][0], cities_coordinates[robot_1_tour[i]][1], 
                                     cities_coordinates[robot_1_tour[i+1]][0], cities_coordinates[robot_1_tour[i+1]][1])
        for i in range(len(robot_1_tour) - 1)
    )
    
    # Compare calculated costs with provided costs
    if not (math.isclose(robot_0_real_cost, robot_0_cost, rel_tol=1e-5) and
            math.isclose(robot_1_real_cost, robot_1_cost, rel_tol=1e-5) and
            math.isclose(robot_0_real_cost + robot_1_real_cost, total_cost, rel_tol=1e-5)):
        return "FAIL"
    
    return "CORRECT"

# Cities' coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Robot tours as provided
robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 0, 17]
robot_1_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 16]

# Expected travel costs
robot_0_cost = 141.23991691092212
robot_1_cost = 93.96788504111024
total_cost = 235.20780195203236

# Validate solution
result = validate_solution(
    cities_coordinates, 
    (robot_0_tour, robot_1_tour), 
    (robot_0_cost, robot_1_cost, total_cost)
)
print(result)