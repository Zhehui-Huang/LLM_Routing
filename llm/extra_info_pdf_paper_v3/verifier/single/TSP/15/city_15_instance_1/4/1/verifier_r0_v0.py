import math

# Provided cities and coordinates
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

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to validate the tour
def validate_tour(tour):
    # Requirement 1: Starts and ends at depot 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    # Requirement 2: Each city visited once except depot
    visited = set(tour)
    if len(visited) != len(cities) or set(range(15)) != visited:
        return False
    return True

# Function to validate cost
def validate_cost(tour, provided_cost):
    # Requirement 3: Total travel cost calculated via Euclidean distance
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    return math.isclose(total_cost, provided_cost, rel_tol=1e-9)

# Expected output and tour
expected_tour = [0, 9, 3, 7, 1, 6, 13, 2, 10, 4, 12, 11, 8, 14, 5, 0]
expected_cost = 486.49

# Unit tests
if validate_tour(expected_tour) and validate_cost(expected_tour, expected_cost):
    print("CORRECT")
else:
    print("FAIL")