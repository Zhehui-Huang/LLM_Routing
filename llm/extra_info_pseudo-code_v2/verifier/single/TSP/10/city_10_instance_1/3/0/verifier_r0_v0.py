import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities, reported_cost):
    # [Requirement 1] Check start and end at depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if all cities except the depot are visited exactly once.
    visited = set(tour)
    if len(visited) != len(cities) or set(range(len(cities))) != visited:
        return "FAIL"

    # [Requirement 3] Check the accuracy of the cost calculation.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    # [Requirement 4] Already verified by other checks (start/end at depot, cities visited exactly once).

    return "CORRECT"

# City coordinates
cities = [
    (53, 68),  # City 0 - Depot
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

# Tour and cost provided
provided_tour = [0, 5, 9, 2, 7, 6, 1, 4, 3, 8, 0]
provided_cost = 311.5420034076028

# Validate the solution
result = verify_tour(provided_tour, cities, provided_tour)
print(result)