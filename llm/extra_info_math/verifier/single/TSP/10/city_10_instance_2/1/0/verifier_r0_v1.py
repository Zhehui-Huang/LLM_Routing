import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost, cities):
    """Verify TSP solution against given requirements."""
    # [Requirement 1] Start and end at depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city visited exactly once, except depot
    visited = set(tour)
    if len(visited) != len(cities) or set(range(len(cities))) != visited:
        return "FAIL"

    # [Requirement 3 & 4] Calculate travel cost with possible floating point tolerance
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, cost, abs_tol=0.1):
        return "FAIL"

    # [Requirement 5] No subtours check
    if len(tour) != len(set(tour)) + 1:  # depot city can appear twice (start and end)
        return "FAIL"

    return "CORRECT"

# Coordinates of cities including the depot city (index 0)
cities = [
    (90, 3),  # City 0 (Depot)
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Results from the MILP solver
tour = [0, 3, 0]
total_travel_cost = 156.32018423735306

# Verify the solution using the refactored verification function
result = verify_solution(tour, total_travel_cost, cities)
print(result)