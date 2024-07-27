import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour)-1):
        city1 = tour[i]
        city2 = tour[i+1]
        total_cost += euclidean_distance(coordinates[city1][0], coordinates[city1][1], coordinates[city2][0], coordinates[city2][1])
    return total_cost

def validate_solution(tours, costs, overall_cost, coordinates):
    # Check for unique city visits
    all_cities_visited = set()
    for tour in tours:
        all_cities_visited.update(tour)
    
    if len(all_cities_visited) != 21 or set(range(21)) != all_cities_visited:
        return "FAIL"
    
    # Check the tour starts and ends at designated depots
    if tours[0][0] != 0 or tours[1][0] != 1:
        return "FAIL"
    
    # Calculate and validate costs
    calculated_costs = []
    for tour in tours:
        calculated_costs.append(calculate_total_tour_cost(tour, coordinates))
    
    for idx, cost in enumerate(calculated_costs):
        if not math.isclose(cost, costs[idx], rel_tol=1e-05):
            return "FAIL"
    
    if not math.isclose(sum(costs), overall_cost, rel_tol=1e-05):
        return "FAIL"
    
    return "CORRECT"

# Coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Tours provided in the solution
tours = [
    [0, 2, 3, 19, 8, 9, 17, 14, 5, 7],
    [1, 10, 4, 11, 15, 12, 18, 13, 16, 6, 20]
]

# Costs provided in the solution
costs = [109.94578970125879, 110.8913892252273]
overall_cost = 220.8371789264861

# Verify the solution
result = validate_solution(tours, costs, overall_cost, coordinates)
print(result)