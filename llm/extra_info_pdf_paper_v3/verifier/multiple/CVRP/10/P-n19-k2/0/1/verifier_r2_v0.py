import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_route_cost(route, coordinates):
    total_cost = 0
    for i in range(1, len(route)):
        total_cost += euclidean_distance(coordinates[route[i - 1]], coordinates[route[i]])
    return total_cost

def check_routes(robot_tours, robot_costs, demands, coordinates, robot_capacities):
    total_calculated_cost = 0
    all_visited_cities = set()

    # Check for route completion and starting at the depot
    for index, tour in enumerate(robot_tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        total_calculated_cost += calculate_total_route_cost(tour, coordinates)

    # Check demands are met exactly once and total cost correctness
    total_demand_delivery = {i: 0 for i in range(len(demands))}
    for robot, tour in enumerate(robot_tours):
        current_load = 0
        for city in tour[1:-1]:  # skipping the depot city at start and end
            current_load += demands[city]
            total_demand_delivery[city] += demands[city]
            all_visited_cities.add(city)
        
        if current_load > robot_capacities[robot]:
            return "FAIL"

    if any(total != demands[city] for city, total in total_demand_delivery.items() if city != 0):
        return "FAIL"

    # Compare the computed total cost with the given total cost
    given_total_cost = sum(robot_costs)
    if not math.isclose(total_calculated_cost, given_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Coordinates and demands as provided in the example
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35),
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacities = [160, 160]

# Tours given as example results
robot_tours = [
    [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
    [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
]
robot_costs = [129.15, 172.59]
overall_cost = 301.7480840160281  # Given overall total travel cost, ignored in favor of individual sum

# Execute the test
result = check_routes(robot_tours, robot_costs, demands, coordinates, robot_capacities)
print(result)