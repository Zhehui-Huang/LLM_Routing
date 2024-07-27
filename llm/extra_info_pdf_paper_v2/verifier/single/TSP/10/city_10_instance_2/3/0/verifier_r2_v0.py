import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost, cities):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: All cities from 1 to 9 visited exactly once
    all_cities = set(range(1, 10))
    visited_cities = set(tour[1:-1])  # Exclude the starting and ending depot city 0
    if visited_cities != all_cities:
        return "FAIL"

    # Requirement 5: Output includes the tour starting and ending at city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Calculate the given tour cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Requirement 3 and 6: Check the total travel cost computed with the Euclidean distance
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks are passed:
    return "CORRECT"

# Coordinates for each city
cities = [
    (90, 3),    # Depot city 0
    (11, 17),   # City 1
    (7, 27),    # City 2
    (95, 81),   # City 3
    (41, 54),   # City 4
    (31, 35),   # City 5
    (23, 95),   # City 6
    (20, 56),   # City 7
    (49, 29),   # City 8
    (13, 17)    # City 9
]

# Tour and total cost from the provided solution
provided_tour = [0, 0, 8, 5, 9, 1, 2, 7, 4, 6, 3]
provided_total_cost = 276.75001398566405

# Running the test
result = test_solution(provided_tour, provided_total_cost, cities)
print(result)