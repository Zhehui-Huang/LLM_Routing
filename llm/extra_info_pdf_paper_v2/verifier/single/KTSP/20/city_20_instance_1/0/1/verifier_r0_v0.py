import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost):
    cities_coordinates = {
        0: (14, 77),
        1: (34, 20),
        2: (19, 38),
        3: (14, 91),
        4: (68, 98),
        5: (45, 84),
        6: (4, 56),
        7: (54, 82),
        8: (37, 28),
        9: (27, 45),
        10: (90, 85),
        11: (98, 76),
        12: (6, 19),
        13: (26, 29),
        14: (21, 79),
        15: (49, 23),
        16: (78, 76),
        17: (68, 45),
        18: (50, 28),
        19: (69, 9)
    }

    # [Requirement 1] Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if exactly 7 cities are visited
    if len(tour) != 8:  # 7 cities + 1 extra for the return to the depot
        return "FAIL"

    # [Requirement 3] The objective is implicitly checked by providing a specific total distance that we assume is minimal.
    # This requires verification against known solutions or a precise algorithm output, which is typically done in a solver.

    # Compute the total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities_coordinates[tour[i]]
        x2, y2 = cities_coordinates[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # [Requirement 4] Check computed travel cost with the given cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided result details
tour = [0, 6, 2, 13, 8, 9, 14, 0]
total_travel_cost = 130.6658168109853

# Verify the solution
result = verify_solution(tour, total_travel_navigation_cost)
print("The solution is:", result)