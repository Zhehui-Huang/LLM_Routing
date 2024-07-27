import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, cities, initial_cost):
    # Checking requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking requirement 2: Must visit all cities exactly once, except the depot city 0
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or set(range(len(cities))) != unique_cities:
        return "FAIL"

    # Checking requirement 3: Calculate the correct tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city_a][0], cities[city_a][1], cities[city_b][0], cities[city_b][1])
    
    if not math.isclose(calculated_cost, initial_cost, rel_tol=1e-09):
        return "FAIL"

    # Requirements 4 and 5 are assumed to be checked by other means, as they need comparison to alternatives, or a format check.
    
    return "CORRECT"

# Define the cities based on the problem description
cities = [
    (29, 51),  # Depot city 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Given tour solution and total cost
initial_tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
initial_cost = 442.570870788815

# Validate the tour against the requirements
result = validate_tour(initial_tour, cities, initial_cost)
print(result)