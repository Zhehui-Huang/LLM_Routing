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
    
    # [Requirement 2] Check start and end at Depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 1] Each city exactly once except depot
    if len(set(tour[1:-1])) != 9:  # Means the cities 1 to 9 should be distinct and visited once
        return "FAIL"
    
    # Calculate actual travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        computed_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # [Requirement 4] Check if calculated cost is close to the given total cost
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # All requirements matched
    return "CORRECT"

# Solution output for verification
tour_solution = [0, 3, 6, 2, 8, 9, 1, 7, 5, 4, 0]  # Example tour from the task
total_cost_solution = 328.58208011724435  # Example cost from the task

# Verify the solution following the requirements
result = verify_tour_and_cost(tour_solution, total_cost_solution)
print(result)  # Output either "CORRECT" or "FAIL"