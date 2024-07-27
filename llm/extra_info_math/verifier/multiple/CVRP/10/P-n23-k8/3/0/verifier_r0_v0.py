def test_solution(tours, demands, capacities, costs):
    depot = 0
    visited = [False] * len(demands)
    over_capacity = False
    all_costs_consistent = True
    total_computed_cost = 0

    # Check if each route begins and ends at the depot
    begins_and_ends_at_depot = all(tour[0] == depot and tour[-1] == depot for tour in tours)

    # Check if each city is visited exactly once
    for tour in tours:
        for city in tour[1:-1]:  # Exclude the depot
            if visited[city]:
                return "FAIL"
            visited[city] = True
    
    # Ensure all cities are visited exactly once, excluding the depot (city 0)
    if not all(visited[1:]):
        return "FAIL"

    # Check if the demands and capacities are satisfactorially considered:
    for i, tour in enumerate(tours):
        route_demand = 0
        for city in tour[1:-1]:
            route_demand += demands[city]
        
        if route_demand > capacities:
            over_capacity = True
            break
    
    # Check total travel costs and per tour cost for consistency and minimization
    # Assume costs are calculated accurately external to this verification
    for cost, tour in zip(costs, tours):
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += ((coordinates[tour[i+1]][0] - coordinates[tour[i]][0]) ** 2 + 
                          (coordinates[tour[i+1]][1] - coordinates[tour[i]][1]) ** 2) ** 0.5
        total_computed_cost += tour_cost
        if not (abs(tour_cost - cost) < 0.01):  # Allow for minor floating-point inaccuracies
            all_costs_consistent = False

    if not over_capacity and begins_and_ends_at_depot and all_costs_consistent:
        # Further verify the total cost minimization:
        if abs(sum(costs) - total_computed_cost) < 0.01:
            return "CORRECT"
        else:
            return "FAIL"
    else:
        return "FAIL"

# Given results
tours = [
    [0, 2, 0], [0, 4, 0], [0, 3, 18, 19, 0], [0, 9, 17, 13, 0], [0, 5, 14, 22, 0],
    [0, 8, 10, 0], [0, 1, 11, 12, 15, 0], [0, 6, 16, 0], [0, 7, 20, 21, 0]
]
costs = [42.05, 44.05, 92.62, 85.54, 67.94, 68.29, 84.95, 28.44, 47.08]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
capacities = 40

# Coordinates used for distance calculations between cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

print(test_solution(tours, demands, capacities, costs))