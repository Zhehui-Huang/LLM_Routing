import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tours_requirement(solution, demands, coordinates, capacities):
    # Unpacking solution details
    robot_tours = [solution["Robot 0 Tour"], solution["Robot 1 Tour"]]
    robot_costs = [solution["Robot 0 Total Travel Cost"], solution["Robot 1 Total Travel Cost"]]
    total_cost = solution["Overall Total Travel Cost"]
    
    # Requirement: Each robot's tour must start and end at depot city 0.
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Load demands and verify if each is met
    city_service = [0] * len(demands)
    for i, tour in enumerate(robot_tours):
        current_load = 0
        for j in range(1, len(tour) - 1):
            city_service[tour[j]] += demands[tour[j]]
            current_load += demands[tour[j]]
            if current_load > capacities[i]:
                return "FAIL"  # Exceeding robot capacity
        if not all(x == y for x, y in zip(city_service[1:], demands[1:])):
            return "FAIL"  # All demands are not met exactly
    
    # Verify all cities are visited at least once
    visited = set()
    for tour in robot_tours:
        visited.update(tour)
    if len(visited) < len(demands):
        return "FAIL"
    
    # Calculate and check Euclidean distances against provided costs
    calculated_total_cost = 0
    for idx, tour in enumerate(robot_tours):
        travel_cost = 0
        for k in range(len(tour) - 1):
            travel_cost += calculate_distance(coordinates[tour[k]], coordinates[tour[k+1]])
        if not math.isclose(travel_cost, robot_costs[idx], abs_tol=1e-2):
            return "FAIL"
        calculated_total_demo_cost += travel_cost

    if not math.isclose(calculated_total_cost, total_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Data about cities, demands, coordinates and capacities
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
capacities = [160, 160]

# Solution given for verification
solution = {
    "Robot 0 Tour": [0, 6, 17, 14, 8, 18, 3, 4, 0],
    "Robot 0 Total Travel Cost": 130.62,
    "Robot 1 Tour": [0, 0, 16, 1, 10, 12, 15, 11, 19, 13, 9, 7, 5, 20, 0],
    "Robot 1 Total Travel Cost": 155.53,
    "Overall Total Travel Cost": 286.15
}
# Run the check
result = check_tours_requirement(solution, demands, coordinates, capacities)
print(result)