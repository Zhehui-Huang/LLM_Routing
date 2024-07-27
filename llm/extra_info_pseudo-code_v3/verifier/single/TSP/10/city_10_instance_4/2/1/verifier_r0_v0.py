import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_cost(tour, total_cost):
    # City coordinates
    cities = [
        (79, 15),  # Depot city 0
        (79, 55),
        (4, 80),
        (65, 26),
        (92, 9),
        (83, 61),
        (22, 21),
        (97, 70),
        (20, 99),
        (66, 62)
    ]
    
    # [Requirement 3]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Compute actual cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        computed_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # [Requirement 4] Check if the total cost reported is close to computed cost
    if not math.isclose(computed_custom_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # [Requirement 1]
    visited = set(tour[1:-1])  # Exclude the depot city at the start and end
    if len(visited) != len(cities) - 1:  # Should have visited all cities except depot exactly once
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Given solution
tour_solution = [0, 3, 6, 2, 8, 9, 1, 7, 5, 4, 0]
total_cost_solution = 328.58208011724435

# Verify the solution following the requirements
result = verify_tour_and_cost(tour_solution, total_cost_solution)
print(result)  # Output either "CORRECT" or "FAIL"