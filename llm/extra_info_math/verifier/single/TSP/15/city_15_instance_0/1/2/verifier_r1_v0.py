import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_tour_and_cost(cities, tour, reported_cost):
    # Check starting and ending at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check all cities are visited exactly once except depot
    visited = set(tour)
    if len(visited) != len(cities) or visited != set(range(len(cities))):
        return "FAIL"

    # Check the calculated total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given cities coordinates and their indices
cities = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39),   # City 14
]

# Tour reported by the solver
tour = [0, 2, 6, 5, 3, 13, 7, 4, 12, 14, 11, 9, 1, 10, 8, 0]
# Reported travel cost
reported_cost = 334.5574454652219

# Validating the solution
result = validate_tour_and_cost(cities, tour, reported_cost)
print(result)