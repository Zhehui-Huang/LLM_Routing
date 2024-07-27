import numpy as np

# Corrected coordinates dictionary
coordinates = [
    (35, 40),  # Depot city 0
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

# Corrected tour and cost
solution_tour = [0, 1, 5, 9, 7, 4, 12, 11, 6, 3, 8, 14, 13, 10, 2, 0]
solution_total_cost = 274.93705080

def compute_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # The tour must start and end at city 0 (depot)

    # Check if all cities are visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != 14 or any(city not in visited for city in range(1, 15)):
        return "FAIL"  # All cities must be visited exactly once

    # Calculate the total cost of the given tour
    calculated_cost = sum(compute_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

    # Compare the calculated cost with the provided cost
    if not np.isclose(calculated_cost, total_cost, rtol=1e-5):
        return "FAIL"  # The reported cost must match the calculated cost

    return "CORRECT"

# Executing the verification
result = verify_solution(solution_tour, solution_total_count)
print(result)