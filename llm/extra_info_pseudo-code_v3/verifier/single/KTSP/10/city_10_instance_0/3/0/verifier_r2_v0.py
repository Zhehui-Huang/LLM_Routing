import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_solution(tour, total_cost, cities):
    if len(tour) != 5:
        return "FAIL"
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != 5:  # Checks for duplicate entries
        return "FAIL"
    
    if not all(city in range(10) for city in tour):
        return "FAIL"
    
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Define the cities coordinates with city index as keys
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Given solution tour and its total cost
tour_solution = [0, 5, 4, 8, 0]
total_travel_cost_solution = 107.01182829616894

# Verify the solution
result = validate_solution(tour_solution, total_travel_counter_solution, cities)
print(result)