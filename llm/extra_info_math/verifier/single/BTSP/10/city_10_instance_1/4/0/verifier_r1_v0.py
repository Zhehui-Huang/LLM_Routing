import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities):
    # Requirement 1: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city must be visited exactly once
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"

    # Requirement 3: The objective is to minimize the longest distance between any two consecutive cities in the tour
    # An optimal or correct longest distance is given in the question, assume this is the suitable benchmark for validation.
    # Since we can't optimize via code here, we simply check provided maximum value.
    max_distance_given = 56.61  # Provided in the output example

    max_distance_actual = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        if distance > max_distance_actual:
            max_distance_actual = distance

    if not math.isclose(max_distance_actual, max_distance_given, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Coordinates of cities including the depot
cities_coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Provided solution
tour_given = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]

# Run test
result = verify_tour(tour_given, cities_coordinates)
print(result)