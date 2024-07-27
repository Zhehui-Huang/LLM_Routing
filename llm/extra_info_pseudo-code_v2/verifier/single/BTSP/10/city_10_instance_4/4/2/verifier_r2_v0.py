import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def validate_tour(tour, cities):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Fail: Requirement 1"

    # Requirement 2: Visit each city exactly once
    unique_cities = set(tour)
    if len(tour) - 1 != len(cities) or len(unique_cities) != len(cities):
        return False, "Fail: Requirement 2"

    # Calculate the tour cost and check maximum distance
    max_distance = 0
    total_distance = 0
    for i in range(len(tour) - 1):
        city_index1 = tour[i]
        city_index2 = tour[i+1]
        distance = calculate_distance(cities[city_index1], cities[city_index2])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance

    # Check processed total cost and maximum distance
    processed_total_cost = 408.41360886151256
    processed_max_distance = 61.68468205316454

    if not math.isclose(total_distance, processed_total_cost, rel_tol=1e-5):
        return False, "Fail: Total cost mismatch"
    if not math.isclose(max_distance, processed_max_value, rel_tol=1e-5):
        return False, "Fail: Max distance not minimized correctly"

    return True, "CORRECT"

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
valid, message = validate_tour(tour, cities)
print(message)