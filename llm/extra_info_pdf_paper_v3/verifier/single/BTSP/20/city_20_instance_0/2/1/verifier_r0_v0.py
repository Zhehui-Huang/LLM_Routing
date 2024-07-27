import math

# Definition of the cities and their positions
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# The solution output
solution = {
    'Tour': [0, 4, 1, 8, 13, 17, 2, 6, 19, 3, 10, 5, 7, 9, 11, 15, 18, 12, 14, 16, 0],
    'Total travel cost': 513.018254565361,
    'Maximum distance between consecutive cities': 63.7808748764079
}

def verify_solution(solution, cities):
    tour = solution['Tour']
    # [Requirement 1] Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if all cities are visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or not all(city in unique_cities for city in cities):
        return "FAIL"
    
    # [Requirement 3] Check the maximum distance between consecutive cities in the tour
    max_calculated_distance = 0
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_calculated_cost += distance
        if distance > max_calculated_distance:
            max_calculated_distance = distance
    
    if not math.isclose(max_calculated_distance, solution['Maximum distance between consecutive cities'], rel_tol=1e-5):
        return "FAIL"

    if not math.isclose(total_calculated_cost, solution['Total travel cost'], rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Execute the verification
result = verify_solution(solution, cities)
print(result)