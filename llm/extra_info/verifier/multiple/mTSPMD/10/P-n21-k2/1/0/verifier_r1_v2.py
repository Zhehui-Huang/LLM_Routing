import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return total_cost

def verify_solution(robot_tours, coordinates, expected_costs, expected_total_cost):
    # Requirement 1: Start and end at assigned depots
    if any(tour[0] != tour[-1] for tour in robot_tours):
        return "FAIL"

    # Requirement 2: All cities should be visited exactly once collectively
    all_cities_visited = set()
    for tour in robot_tours:
        all_cities_visited.update(tour[1:-1])  # Exclude the depots counted twice
    all_cities_visited.update([tour[0] for tour in robot_tours])  # Add in the depots
    if len(all_cities_visited) != 21:
        return "FAIL"

    # Requirement 5: Check if the travel cost calculations match the expected costs
    total_calculated_cost = 0
    for i, tour in enumerate(robot_tours):
        calculated_cost = calculate_total_travel_cost(tour, coordinates)
        if not math.isclose(calculated_cost, expected_costs[i], rel_tol=1e-5):
            return "FAIL"
        total_calculated_cost += calculated_cost

    # Check overall total cost
    if not math.isclose(total_calculated_cost, expected_totalica_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Coordinates of each city (indexed accordingly)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Tours provided in the solution
robot_0_tour = [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0]
robot_1_tour = [1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 1]

# Expected costs provided in the solution
robot_0_cost = 109.8362166450987
robot_1_cost = 117.2226527159768
overall_total_cost = 227.0588693610755

# Assert the solution
result = verify_solution([robot_0_tour, robot_1_tour], coordinates, [robot_0_cost, robot_1_cost], overall_total_cost)
print(result)