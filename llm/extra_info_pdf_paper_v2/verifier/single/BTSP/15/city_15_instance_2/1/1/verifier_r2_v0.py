import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities, total_travel_cost, longest_distance):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Every city visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or set(range(len(cities))) != unique_cities:
        return "FAIL"
    
    # Calculations for Requirements 3 and 4
    actual_longest_distance = 0
    actual_total_distance = 0
    for i in range(1, len(tour)):
        distance = calculate_distance(cities[tour[i - 1]], cities[tour[i]])
        actual_total_distance += distance
        actual_longest_distance = max(actual_longest_distance, distance)
    
    # Requirement 4: Check distances
    if not math.isclose(actual_total_distance, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Requirement 3: Check longest distance
    if not math.isclose(actual_longest_distance, longest_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided data
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

provided_tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
provided_total_travel_cost = 322.50
provided_max_distance = 64.66

# Verify the solution
result = verify_tour(provided_tour, cities, provided_total_travel_cost, provided_max_distance)
print(result)