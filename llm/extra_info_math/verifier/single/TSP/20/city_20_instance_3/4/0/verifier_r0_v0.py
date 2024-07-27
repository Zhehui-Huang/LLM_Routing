import math

# Function to calculate the Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Defined cities based on given coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Tour and cost reported from the solver
tour = [0, 19, 3, 0, 19, 3, 0, 19, 3, 0, 19, 3, 0, 19, 3, 0, 19, 3, 0, 19, 0]
reported_cost = 272.94

# Function to validate the tour
def validate_tour(tour, cities):
    # Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check each city visited exactly once, except depot
    unique_visits = set(tour)
    if len(tour) != len(unique_visits) or len(unique_visits) != len(cities):
        return "FAIL"

    # Calculate and check the correctness of the travel cost
    total_calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    
    # Considering some float precision errors in calculations
    if not math.isclose(total_calculated_cost, reported_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Call the validation function and print the result
result = validate_tour(tour, cities)
print(result)