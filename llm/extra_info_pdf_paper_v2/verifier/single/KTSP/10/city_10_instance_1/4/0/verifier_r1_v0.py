import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour_solution(tour, cost, coordinates):
    # Verify if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify if the tour includes exactly 5 distinct cities
    if len(set(tour)) != 6:  # including depot visited twice
        return "FAIL"

    # Check if all cities in tour are valid and calculate the total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        if tour[i] < 0 or tour[i] >= len(coordinates):
            return "FAIL"
        computed_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])

    # Check computed cost against provided cost with a small tolerance for floating point arithmetic
    if not math.isclose(computed_cost, cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Given city coordinates
coordinates = [
    (53, 68),  # Depot city 0
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

# Provided solution
solution_tour = [0, 4, 8, 3, 5, 0]
solution_cost = 110.38072506104011

# Validate the solution
result = verify_tour_solution(solution_tour, solution_cost, coordinates)
print(result)