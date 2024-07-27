import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tour_and_cost(robot_tour, robot_travel_cost, coordinates, demand, capacity):
    total_demand = 0
    last_city = robot_tour[0]
    calculated_cost = 0
    current_load = 0
    
    for i in range(1, len(robot_tour)):
        city = robot_tour[i]
        calculated_cost += calculate_euclidean_distance(*coordinates[last_city], *coordinates[city])
        last_city = city

        if city != 0:
            current_load += demand[city]
            if current_load > capacity:
                return False, 0, 0
        else:
            current_load = 0

        total_demand += demand[city] if city != 0 else 0

    return total_demand, calculated_cost, True

def unit_test_solution(robot_tours_data, coordinates, demands, capacity):
    overall_total_calculated_cost = 0
    all_cities_covered = set()

    for robot_tour, expected_cost in robot_tours_data:
        total_demand, calculated_cost, is_within_capacity = check_tour_and_cost(robot_tour, expected_demand, coordinates, demands, capacity)
        if not is_within_capacity:
            return "FAIL"
        overall_total_calculated_cost += calculated_cost
        all_cities_covered.update(robot_tour)

    all_cities_reached = all(c in all_cities_covered for c in range(1, len(coordinates))) and 0 in all_cities_covered
    if not all_cities_reached:
        return "FAIL"

    if abs(overall_total_calculated_cost - sum(expected_costs for _, expected_costs in robot_tours_data)) > 1e-2:
        return "FAIL"

    return "CORRECT"

# Data: robot tours and expected costs
robot_0_tour = [0, 11, 9, 14, 0, 17, 13, 0, 15, 19, 0, 18, 8, 3, 12, 0]
robot_1_tour = [0, 6, 1, 4, 2, 5, 0, 7, 20, 10, 16, 0]
robot_0_cost = 387.86
robot_1_cost = 172.51

# Test setup
robot_tours_data = [
    (robot_0_tour, robot_0_cost),
    (robot_1_tour, robot_1_cost)
]

coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
               (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Execute the test
result = unit_test_solution(robot_tours_data, coordinates, demands, 160)
print(result)