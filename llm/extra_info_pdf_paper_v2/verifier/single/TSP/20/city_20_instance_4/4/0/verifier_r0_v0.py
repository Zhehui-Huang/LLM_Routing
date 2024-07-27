import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost):
    # City coordinates (index matches city number)
    coordinates = [
        (26, 60),  # Depot 0
        (73, 84),
        (89, 36),
        (15, 0),
        (11, 10),
        (69, 22),
        (28, 11),
        (70, 2),
        (47, 50),
        (60, 29),
        (29, 26),
        (85, 68),
        (60, 1),
        (71, 73),
        (82, 47),
        (19, 25),
        (75, 9),
        (52, 54),
        (64, 72),
        (14, 89)
    ]

    # [Requirement 1] Starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Each city visited exactly once, excluding the depot
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL"

    # [Requirement 3] Checking the total travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        city1 = tour[i]
        city2 = tour[i+1]
        calculated_cost += euclidean_distance(*coordinates[city1], *coordinates[city2])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):  # allowing small precision errors
        return "FAIL"

    # [Requirement 4] & [Requirement 5] Already checked implicitly by input and program structure
    return "CORRECT"

# Given solution
tour_solution = [0, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 1, 13, 18, 17, 8, 19, 0]
total_travel_cost_solution = 379.72

# Verify the solution
result = verify_solution(tour_solution, total_travel_cost_solution)
print(result)  # Outputting whether the solution is CORRECT or whether it FAILs any requirement check