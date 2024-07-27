import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_solution(robots_routes, robots_capacity, demands, coordinates, robots_route_costs, reported_overall_cost):
    num_robots = len(robots_routes)
    total_demand = sum(demands)
    total_delivered = 0
    overall_cost = 0

    for robot_id in range(num_robots):
        route = robots_routes[robot_id]
        capacity_used = 0
        last_city = 0  # Depot is the starting point
        route_cost = 0
        
        if route[0] != 0 or route[-1] != 0:
            return "FAIL"

        for i in range(1, len(route)):
            city = route[i]
            demand = demands[city]
            capacity_used += demand
            if capacity_used > robots_capacity:
                return "FAIL"
            current_city = city
            route_cost += euclidean_distance(coordinates[last_city][0], coordinates[last_city][1],
                                              coordinates[current_city][0], coordinates[current_city][1])
            total_delivered += demand
            last_city = current_city
        
        # Returning to depot
        route_cost += euclidean_distance(coordinates[last_city][0], coordinates[last_city][1],
                                          coordinates[0][0], coordinates[0][1])
        
        if not math.isclose(route_cost, robots_route_costs[robot_id], abs_tol=0.01):
            return "FAIL"
        
        overall_cost += route_cost
    
    if total_delivered != total_demand:
        return "FAIL"
    
    if not math.isclose(overall_cost, reported_overall_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Define parameters
robots_capacity = 160
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
robots_routes = [
    [0, 6, 7, 5, 9, 2, 8, 3, 1, 4, 0],
    [0, 16, 10, 12, 15, 11, 18, 19, 13, 17, 14, 20, 0]
]
robots_route_costs = [131.01, 164.24]
reported_overall_cost = 295.24

result = validate_solution(robots_routes, robots_capacity, demands, coordinates, robots_route_costs, reported_overall_color)
print(result)  # This will print "CORRECT" if all is well, "FAIL" otherwise