import math

def calculate_distance(city1, city2):
    return math.dist(city1, city2)

# Data - city coordinates
cities = {
    0: (3, 26),
    12: (11, 14),
    14: (18, 49),
    16: (28, 49),
    19: (30, 48)
}

# Provided solution
tour_given = [0, 12, 14, 16, 19, 0]
total_cost_given = 97.17955920904124
max_distance_given = 35.6931365951495

def test_tour(tour, cities):
    # Requirement 1: Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check each city is visited exactly once
    unique_cities = set(tour[1:-1])  # Exclude the repeated depot city at the start/end
    if len(unique_cities) != len(cities) - 1:  # -1 because depot is not included in the check
        return "FAIL"
    
    # Requirement 3: Check if the max distance between any two consecutive cities is as given
    max_distance_calculated = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        if distance > max_distance_calculated:
            max_distance_calculated = distance
    
    # To account for floating-point arithmetic issues, use a tolerance
    tolerance = 1e-5
    if not (abs(max_distance_calculated - max_distance_given) <= tolerance):
        return "FAIL"
    
    return "CORRECT"

# Running the test
result = test_tour(tour_given, cities)
print(result)  # This should output "CORRECT" if all conditions are met