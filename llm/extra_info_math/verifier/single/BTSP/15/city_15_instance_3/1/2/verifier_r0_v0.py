import math

# Provided city coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Data provided from the solution
solution = {
    'Tour': [0, 6, 13, 9, 8, 14, 1, 3, 12, 4, 7, 2, 11, 10, 5, 0],
    'Total travel cost': 400.12,
    'Maximum distance between consecutive cities': 48.37
}

# Provided requirements to be verified
def verify_solution(solution):
    tour = solution['Tour']
    total_travel_cost = solution['Total travel tensor']
    max_distance = solution['Maximum distance between consecutive cities']
    
    # Verify requirement 1: Start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify requirement 2: Each city visited exactly once
    unique_cities_visited = set(tour[1:-1])
    if len(unique_cities_visited) != len(cities) - 1 or not all(city in unique_cities_visited for city in range(1, 15)):
        return "FAIL"
    
    # Calculate actual total travel cost and maximum distance
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(tour[i], tour[i + 1])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_detection = distance
    
    # Verify requirement 3: Minimize the longest distance
    if not math.isclose(actual_total_cost, total_travel_cost, rel_tol=1e-2) or not math.isclose(actual_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Output the verification result
print(verify_solution(solution))