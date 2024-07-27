import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_solution(robots_routes, robots_capacity, demands, coordinates):
    num_robots = len(robots_routes)
    total_demand = sum(demands)
    total_delivered = 0
    overall_cost = 0

    # Validate each robot's route
    for robot_id in range(num_robots):
        route = robots_routes[robot_id]
        capacity_used = 0
        last_city = 0  # start from depot initially
        route_cost = 0

        # Check route starts and ends at the depot
        if route[0] != 0 or route[-1] != 0:
            return "FAIL"

        # Check demands and capacity
        for city in route[1:-1]:  # skip the depot at the start and end
            demand = demands[city]
            capacity_used += demand
            total_delivered += demand

            # Check individual robot capacity is not exceeded
            if capacity_used > robots_capacity:
                return "FAIL"

            # Calculate travel cost
            current_city = city
            route_cost += euclidean_distance(coordinates[last_city][0], coordinates[last_city][1],
                                              coordinates[current_city][0], coordinates[current_city][1])
            last_city = current_city
        # Return to depot cost
        route_cost += euclidean_distance(coordinates[last_city][0], coordinates[last_node][1],
                                          coordinates[0][0], coordinates[0][1])

        # Summing the overall system cost
        overall_cost += route_cost
        
        # Check reported cost
        actual_cost = robots_route_costs[robot_id]
        if not math.isclose(route_cost, actual_cost, abs_tol=0.01):
            return "FAIL"

    # Check if all demands are met
    if total_delivered != total_demand:
        return "FAIL"

    # Compare calculated overall cost with the reported total cost
    reported_overall_cost = 295.24  # From the given results
    if not math.isclose(overall_cost, reported_overall_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Define tours and demands as per the task description and provided solution
robots_routes = [
    [0, 6, 7, 5, 9, 2, 8, 3, 1, 4, 0],
    [0, 16, 10, 12, 15, 11, 18, 19, 13, 17, 14, 20, 0]
]

robots_route_costs = [
    131.01,
    164.24
]

robots_capacity = 160
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

result = validate_solution(robots_routes, robots_capacity, demands, coordinates)
print(result)