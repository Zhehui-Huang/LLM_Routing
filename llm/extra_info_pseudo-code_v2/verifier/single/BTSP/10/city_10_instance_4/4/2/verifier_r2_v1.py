import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def validate_tour(tour, cities):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit each city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities):
        return "FAIL"

    previous_city = tour[0]
    max_distance = 0
    total_distance = 0
    for i in range(1, len(tour)):
        current_city = tour[i]
        distance = calculate_distance(cities[previous_city], cities[current_city])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance
        previous_city = current_city

    # Validate processed values
    expected_total_cost = 408.41360886151256
    expected_max_distance = 61.68468205316454
    if not math.isclose(total_distance, expected_total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Data Setup
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]

# Validation
result = validate_tour(tour, cities)
print(result)