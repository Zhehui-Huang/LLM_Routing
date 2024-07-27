import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(coordinates, tour, total_cost, max_distance):
    # Checking that there are 21 nodes
    if len(coordinates) != 21:
        return "FAIL"

    # Checking that each coordinate is a tuple with two integers
    if not all(isinstance(city, tuple) and len(city) == 2 for city in coordinates):
        return "FAIL"

    # Checking the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking that each city is visited exactly once (excluding the return to the depot)
    if len(set(tour)) != len(coordinates) or len(tour) != len(coordinates) + 1:
        return "FAIL"

    # Calculate the total traveled distance and the maximum distance between consecutive cities
    computed_total_cost = 0
    computed_max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        computed_total_cost += dist
        computed_max_distance = max(computed_max_distance, dist)

    # Check the total travel cost and the maximum distance
    computed_total_cost = round(computed_total_cost, 2)
    computed_max_distance = round(computed_max_distance, 2)
    if computed_total_cost != total_cost or computed_max_distance != max_distance:
        return "FAIL"

    return "CORRECT"

# Coordinates of cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Simulated output from a hypothetical BTSP algorithm
simulated_tour = [0, 4, 7, 14, 8, 12, 18, 3, 1, 10, 11, 16, 9, 15, 17, 5, 2, 13, 6, 19, 0]
simulated_total_cost = 949.43
simulated_max_distance = 114.55

# Perform the test
test_result = test_solution(coordinates, simulated_tour, simulated_total_cost, simulated_max_modifier_distance)
print(test_result)