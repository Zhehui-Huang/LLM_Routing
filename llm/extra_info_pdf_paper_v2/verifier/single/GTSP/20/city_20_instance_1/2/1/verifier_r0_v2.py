import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost):
    # City coordinates and groups as defined
    city_coords = {
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
        6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
        12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
        18: (50, 28), 19: (69, 9)
    }
    groups = [
        [5, 6, 7, 11, 17],
        [1, 4, 8, 13, 16],
        [2, 10, 15, 18, 19],
        [3, 9, 12, 14]
    ]

    # Verify Requirement 1: Tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify Requirement 2: Exactly one city from each group
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:
        found = False
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
                found = True
                break
        if not found:
            return "FAIL"
    
    if any(v != 1 for v in visited_groups):
        return "FAIL"

    # Calculate total cost (Requirement 3)
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coords[tour[i]]
        x2, y2 = city_coords[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Validate that the calculated cost is close to the given total cost (Requirement 5)
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Solution parameters
solution_tour = [0, 6, 13, 2, 9, 0]
solution_cost = 114.66

# Running the test
test_result = verify_solution(solution_tour, solution_cost)
print(test_result)