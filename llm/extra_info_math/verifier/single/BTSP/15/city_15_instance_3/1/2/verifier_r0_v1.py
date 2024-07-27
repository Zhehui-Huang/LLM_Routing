import math

# Provided city coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def calculate_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Solution provided
solution = {
    'Tour': [0, 6, 13, 9, 8, 14, 1, 3, 12, 4, 7, 2, 11, 10, 5, 0],
    'Total travel cost': 400.12,
    'Maximum distance between consecutive cities': 48.37
}

def verify_solution(solution):
    tour = solution['Tour']
    total_travel_cost = solution['Total travel cost']
    max_distance = solution['Maximum distance between consecutive cities']
    
    # Requirement 1: Starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once
    if sorted(tour[1:-1]) != sorted(range(1, 15)):
        return "FAIL"
    
    # Tracking for total cost calculation and maximum distance calculation
    calculated_total_cost = 0.0
    calculated_max_distance = 0.0
    
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i + 1])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # Requirement 3: Minimized max distance
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-2) or not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Output the verification result
print(verify_solution(solution))