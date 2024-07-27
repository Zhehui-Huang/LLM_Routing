import math

def euclidean_distance(cityA, cityB):
    return math.sqrt((cityA[0] - cityB[0])**2 + (cityA[1] - cityB[1])**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0.0
    for i in range(1, len(tour)):
        cityA = coordinates[tour[i-1]]
        cityB = coordinates[tour[i]]
        total_cost += euclidean_distance(cityA, cityB)
    return total_cost

def verify_solution(tours, costs, max_cost, coordinates):
    # Verify Requirement 1
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Start or End city is not the Depot."
    
    # Verify Requirement 4 and 6
    calculated_costs = [calculate_total_travel_cost(tour, coordinates) for tour in tours]
    calculated_max_cost = max(calculated_costs)
    for idx, cost in enumerate(costs):
        if not math.isclose(cost, calculated_costs[idx], rel_tol=1e-9):
            return "FAIL: Cost calculation error."
    if not math.isclose(calculated_max_cost, max_cost, rel_tol=1e-9):
        return "FAIL: Max cost calculation error."
    
    # Verify Requirement 2
    visited = set()
    for tour in tours:
        visited.update(tour)
    expected_visited = set(range(len(coordinates)))  # includes the depot
    if visited != expected_visited:
        return "FAIL: Not all cities visited correctly."

    # Requirement 3, 5 already checked indirectly
    return "CORRECT"

# City coordinates including the depot (index aligns with city index)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Given solution
tours = [
    [0, 1, 3, 4, 8, 10, 11, 12, 14, 16, 17, 0],
    [0, 2, 5, 6, 7, 9, 13, 15, 18, 0]
]
costs = [212.21732723337922, 116.70009709276687]
max_cost = 212.21732723337922

# Validation
result = verify_solution(tours, costs, max_cost, coordinates)
print(result)