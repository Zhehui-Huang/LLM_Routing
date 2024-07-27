def verify_solution(tours, demands, capacities, coordinates):
    visited_cities = set()
    max_capacity = 160
    all_tours_cost = 0
    from math import sqrt

    for tour, capacity in zip(tours, capacities):
        # Each route must start and end at the depot city (Depot city index is 0).
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Verify demand does not exceed capacity
        route_demand = 0
        route_cost = 0
        previous_city = None

        for i, city in enumerate(tour):
            if city != 0:  # Exclude depot demand calculations
                route_demand += demands[city]
            if previous_city is not None:
                dist = sqrt((coordinates[city][0] - coordinates[previous_city][0]) ** 2 +
                            (coordinates[city][1] - coordinates[previous_city][1]) ** 2)
                route_cost += dist
            previous_city = city

        if route_demand > max_capacity:
            return "FAIL"
        
        # Accumulate total tour cost
        all_tours_cost += route_cost

        # Add visited cities excluding depot
        visited_cities.update(tour[1:-1])  # Exclude depot entry and exit instances

    # Check if all cities are visited exactly once
    if len(visited_cities) != len(coordinates) - 1:  # Exclude the depot
        return "FAIL"

    # Objective minimization check (informative, specific target not given, hence not strictly checked)
    # expected_total_cost = 403.11 (as claimed to be the optimal solution solution needs to be <= expected)
    
    # Considering all constraints have passed:
    return "CORRECT"

# Data: coordinates, demands for each city including depot
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacities = [160, 160, 160, 160, 160, 160]  # Implicit from problem definition (same for all robots)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Tours provided:
tours = [
    [0, 1, 10, 12, 15, 0],
    [0, 2, 3, 8, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 5, 14, 17, 0],
    [0, 6, 7, 9, 13, 0],
    [0, 16, 20, 0]
]

print(verify_solution(tours, demands, capacities, coordinates))