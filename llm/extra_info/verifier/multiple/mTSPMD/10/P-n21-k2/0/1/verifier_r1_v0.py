import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean delegated_cost(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def validate_solution():
    # Coordinates of each city, indexed by city number
    coordinates = {
        0: (30, 40),
        1: (37, 52),
        2: (49, 49),
        3: (52, 64),
        4: (31, 62),
        5: (52, 33),
        6: (42, 41),
        7: (52, 41),
        8: (57, 58),
        9: (62, 42),
        10: (42, 57),
        11: (27, 68),
        12: (43, 67),
        13: (58, 48),
        14: (58, 27),
        15: (37, 69),
        16: (38, 46),
        17: (61, 33),
        18: (62, 63),
        19: (63, 69),
        20: (45, 35)
    }

    # Tours provided in the solution
    robot_0_tour = [0, 16, 6, 20, 2, 10, 12, 4, 8, 18, 14, 0]
    robot_1_tour = [1, 15, 11, 3, 19, 13, 9, 17, 5, 7, 1]

    # Calculate costs reported
    reported_robot_0_cost = 171.820768703562
    reported_robot_1_cost = 137.90549546878637
    reported_total_cost = 309.72626417234835

    # Calculate actual costs based on the provided coordinates
    actual_robot_0_cost = calculate_total_cost(robot_0_tour, coordinates)
    actual_robot_1_cost = calculate_total_cost(robot_1_tour, coordinates)
    actual_total_cost = actual_robot_0_cost + actual_robot_1_cost

    # Check all cities are visited exactly once and return to their respective depots
    all_cities = set(range(21))
    visited_cities = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])
    cities_correctly_visited = (all_cities == visited_cities and robot_0_tour[0] == robot_0_tour[-1] and robot_1_tour[0] == robot_1_tour[-1])

    # Check calculated costs are close to reported costs (with a tolerance due to floating-point arithmetic)
    if cities_correctly_visited and \
       math.isclose(actual_robot_0_cost, reported_robot_0_cost, rel_tol=1e-5) and \
       math.isclose(actual_robot_1_cost, reported_robot_1_cost, rel_tol=1e-5) and \
       math.isclose(actual_total_cost, reported_total_loss, rel_tol=1e-5):
        return "CORRECT"
    else:
        return "FAIL"

# Run the validation
result = validate_solution()
print(result)