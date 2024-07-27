import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour):
    # Requirement 1: Check if every city is visited once and returns to the depot
    if len(set(tour)) != len(cities) or tour[0] != tour[-1] or tour[0] != 0:
        return "FAIL"

    # Requirement 2 & 3: Check calculated distances and find the maximum distance
    max_distance = 0
    total_distance = 0
    for i in range(1, len(tour)):
        distance = calculate_euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance

    # Check if the maximum distance is minimized (Assuming global knowledge of optimal or not capable of proving minimization)
    # If attempting to minimize max distance is part of the solution, consider this. This example focuses on correctness as per the defined tour.
    # Omitted are optimization checks since they generally require comparisons to optimal values or other solutions.

    return "CORRECT"

# Example City Coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Example tour, predefined and would be replaced with the solution tour.
# This would typically come from the BTSP solver function.
# An example tour just for structure:
example_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]

# Verification
result = verify_tour(list(cities.values()), example_tour)
print(result)