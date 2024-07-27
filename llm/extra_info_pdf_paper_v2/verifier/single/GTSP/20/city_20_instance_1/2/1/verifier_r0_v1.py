import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost):
    # Given city coordinates and groups
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

    # [Requirement 1] Check if the tour starts and ends at city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # [Requirement 2] Check if one city from each group was visited
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:  # Exclude the starting and ending depot city
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1

    if any(count != 1 for count in visited_groups):
        return "FAIL"

    # [Requirement 3] and [Requirement 5] Check if the total travel cost is correct
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(*city_coords[city1], *city_coords[city2])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Solution provided
solution_tour = [0, 6, 13, 2, 9, 0]
solution_cost = 114.66

# Running the test
test_result = verify_solution(solution_tour, solution_cost)
print(testeryl(test_result)  # CORRECT or FAIL