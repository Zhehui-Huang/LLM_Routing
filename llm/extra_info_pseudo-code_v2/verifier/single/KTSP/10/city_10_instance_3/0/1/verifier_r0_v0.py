import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_solution(tour, total_cost):
    # City coordinates as provided
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }

    # [Requirement 1] Check if 7 unique cities are visited
    if len(set(tour)) != 8 or len(tour) != 8:  # Includes depot city twice (start and end)
        return "FAIL"

    # [Requirement 2] Check if the tour starts and ends at the depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the total travel cost and compare with given total_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # [Requirement 3] Verify calculated cost is close to the given total cost
    # Allowing a small error margin due to potential floating point precision issues
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    # [Requirement 4] Already implicitly checked by output format in parameters but ensuring the format as well
    if not isinstance(tour, list) or not isinstance(total_cost, (float, int)):
        return "FAIL"

    return "CORRECT"

# The given solution
tour = [0, 4, 1, 7, 3, 5, 2, 0]
total_cost = 327.71

# Execute check and print result
result = check_solution(tour, total_cost)
print(result)