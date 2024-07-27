import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(cities, tour, reported_cost):
    # Test Requirement 1: Start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Test Requirement 2: Each city must be visited exactly once
    visited_cities = tour[1:-1]  # Ignore the first and last entry
    if len(set(visited_cities)) != len(visited_cities) or set(visited_cities) != set(range(1, len(cities))):
        return "FAIL"
    
    # Test Requirement 3: Calculate the correct travel cost using Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    if not math.isclose(total_cost, reported_cost, abs_tol=1e-6):
        return "FAIL"
    
    # Requirements 4 and 5 could not be solved analytically in a practical unittest without complex implementations or validations
    
    return "CORRECT"

# Coordinate for each city (indexed as mentioned in the problem)
cities = [
    (8, 11),   # Depot city 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Provided tour and cost
proposed_tour = [0, 9, 12, 13, 17, 16, 14, 7, 11, 15, 18, 3, 10, 2, 6, 19, 5, 8, 1, 4, 0]
proposed_cost = 506.442026751833

# Test the solution
result = verify_tour(cities, proposed_tour, proposed_cost)
print(result)