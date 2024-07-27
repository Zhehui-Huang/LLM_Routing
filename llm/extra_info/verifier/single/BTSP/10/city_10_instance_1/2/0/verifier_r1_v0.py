import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }

    # Requirement 1: Check all cities exactly once and start/end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != sorted(list(cities.keys())):
        return "FAIL"

    # Requirement 2: Calculate and verify total travel cost
    calculated_total_cost = 0
    max_calculated_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > max_calculated_given:
            max_calculated_given = distance

    if not math.isclose(calculated_total_cost, total_cost, abs_tol=1e-2):
        return "FAIL"

    # Requirement 3: Check if maximum distance matches
    if not math.isclose(max_calculated_given, max_distance, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 0, 8, 3, 5, 2, 9, 7, 1, 6, 0, 4, 0, 0]
total_travel_cost = 344.22
maximum_distance_between_cities = 56.61

output = verify_solution(tour, total_travel_cost, maximum_distance_between_cities)
print("Result:", output)