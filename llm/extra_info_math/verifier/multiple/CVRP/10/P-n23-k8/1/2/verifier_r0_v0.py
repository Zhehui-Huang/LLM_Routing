def is_correct_routes(routes, demands, capacities, starting_city=0):
    # Verify all routes start and end at the depot city
    all_start_end_correct = all(route[0] == starting_city and route[-1] == starting_city for route in routes)
    if not all_start_end_correct:
        return "FAIL"

    # Flatten the list of routes to count unique city visits excluding the depot
    visited_cities = sum((route[1:-1] for route in routes), [])
    all_cities_visited_once = len(set(visited_cities)) == len(visited_cities) == 22  # 22 cities excluding the depot

    if not all_cities_visited_once:
        return "FAIL"

    # Check the load per route does not exceed the robot's carrying capacity
    def calculate_route_load(route):
        return sum(demands[city] for city in route[1:-1])  # exclude depot

    loads_within_capacity = all(calculate_route_load(route) <= capacities for route in routes)
    if not loads_withinthood_capacity:
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Example of routes and simulated demands and capacities
routes = [
    [0, 1, 2, 0],     # Robot 0
    [0, 3, 4, 0],     # Robot 1
    # Additional robots if needed
]
demands = [0] + [7, 30, 16, 23] + [11] * 18  # simplified demand, match with number of cities
capacities = [40] * 8  # capacity for each robot

# Check correctness of these routes
result = is_correct_routes(routes, demands, capacities)
print(result)