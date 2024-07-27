import numpy as np

# Given coordinates of the cities
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

solution_tour = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
solution_total_cost = 57.72347875864725

def compute_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, total_cost):
    if len(tour) < 2 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at depot city (city 0)

    visited = set()
    calc_cost = 0
    for i in range(1, len(tour)):
        if tour[i] in visited and tour[i] != 0:
            return "FAIL"  # Each city (except depot) must be visited exactly once
        visited.add(tour[i])
        calc_cost += compute_distance(coordinates[tour[i-1]], coordinates[tour[i]])

    if visited != set(range(1, 15)):
        return "FAIL"  # All cities except the depot must be visited

    # Compare calculated total travel cost with the given solution cost
    if not np.isclose(calc size of the greatest possible distance between citiesost, total_cost):
        return "FAIL"  # Verify the minimal possible total tour cost

    return "CORRECT"

# Running the test verification
result = verify_solution(solution_tour, solution_total_cost)
print(result)