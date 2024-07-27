import math
from collections import Counter

# Given solution
robots_tours = [
    [0, 22, 21, 0],
    [0, 19, 7, 0],
    [0, 8, 16, 0],
    [0, 4, 14, 0],
    [0, 15, 6, 0],
    [0, 18, 3, 0],
    [0, 13, 9, 0],
    [0, 11, 12, 10, 1, 2, 17, 5, 20, 0]
]
robots_costs = [
    52.491761791689186,
    96.03769873150547,
    64.92216653342014,
    97.09748583701219,
    70.31738766580068,
    82.01563780379637,
    68.39398119181286,
    125.7732337225006
]

# Cities information: defining coordinates for each city for Euclidean distance calculation
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_base[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Checking all requirements
def verify_solution(robots_tours, robots_costs):
    # Requirement 1: All cities visited exactly once
    all_visited_cities = [city for tour in robots_tours for city in tour if city != 0]
    unique_cities = set(all_visited_cities)
    if len(all_visited_cities) != len(unique_cities) or len(all_visited_cities) != 22:
        return "FAIL"
    
    # Requirement 2: Each robot starts at depot 0 and doesn't need to return
    if any(tour[0] != 0 or tour[-1] != 0 for tour in robots_tours):
        return "FAIL"
    
    # Requirement 3: Verify the travel costs are minimal
    # Assuming 'minimal' is satisfied by computational checks
    calculated_costs = []
    for tour in robots_tours:
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(tour[i], tour[i + 1])
        calculated_costs.append(total_cost)
    
    if not all(abs(calculated_costs[i] - robots_costs[i]) < 1e-5 for i in range(len(robots_costs))):
        return "FAIL"
    
    # Checking overall cost is as expected from provided total
    summed_cost = sum(calculated_costs)
    provided_overall_total = 657.0493532775374
    if not math.isclose(summed_cost, provided_overall_total, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Output the verification result
print(verify_solution(robots_tours, robots_costs))