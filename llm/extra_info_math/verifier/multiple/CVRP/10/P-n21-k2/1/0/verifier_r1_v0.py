def calculate_euclidean_distance(p1, p2):
    from math import sqrt
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tours, demands, capacities, coordinates):
    visited_cities = set()
    total_demand_on_route = [0] * len(tours)
    total_cost = [0] * len(tours)
    overall_cost = 0
    
    # Requirement 1: Each route must begin and end at the depot city
    for idx, route in enumerate(tours):
        if route[0] != 0 or route[-1] != 0:
            return "FAIL"
    
    # Requirement 2: Each city (excluding the depot) is visited exactly once across all tours
    for route in tours:
        for city in route[1:-1]:  # Exclude starting and ending 0s
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

    if visited_cities != set(range(1, len(demands))):  # Check if all cities are visited
        return "FAIL"

    # Requirement 3: The total demand on each route does not exceed the capacity of the robot
    for idx, route in enumerate(tours):
        for city in route[1:-1]:  # Exclude starting and ending 0s
            total_demand_on_route[idx] += demands[city]
        
        if total_demand_on_route[idx] > capacities[idx]:
            return "FAIL"
    
    # Requirement 4: Minimize the total travel cost for all tours
    # This requirement will be validated conceptually since we don't know the true minimal cost.
    for idx, route in enumerate(tours):
        for i in range(len(route) - 1):
            cost = calculate_euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]])
            total_cost[idx] += cost
        overall_cost += total_cost[idx]
    
    # Output actual costs: This is for debugging or logging, can be commented out in production.
    print("Total Travel Cost for each robot:", total_cost)
    print("Overall Total Travel Cost:", overall_cost)

    return "CORRECT"

# Example usage with data of the problem and given solution
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
               (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacities = [160, 160]

tours = [
    [0, 8, 7, 6, 4, 3, 2, 1, 0],
    [0, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 5, 0]
]

print(verify_solution(tours, demands, capacities, coordinates))