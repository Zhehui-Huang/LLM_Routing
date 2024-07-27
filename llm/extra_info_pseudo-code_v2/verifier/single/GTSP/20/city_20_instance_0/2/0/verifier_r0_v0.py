import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost):
    # Cities coordinates
    coordinates = [
        (8, 11),   # Depot city 0
        (40, 6),   # City 1
        (95, 33),  # City 2
        (80, 60),  # City 3
        (25, 18),  # City 4
        (67, 23),  # City 5
        (97, 32),  # City 6
        (25, 71),  # City 7
        (61, 16),  # City 8
        (27, 91),  # City 9
        (91, 46),  # City 10
        (40, 87),  # City 11
        (20, 97),  # City 12
        (61, 25),  # City 13
        (5, 59),   # City 14
        (62, 88),  # City 15
        (13, 43),  # City 16
        (61, 28),  # City 17
        (60, 63),  # City 18
        (93, 15)   # City 19
    ]

    # Groups of cities by index
    group_0 = [1, 3, 5, 11, 13, 14, 19]
    group_1 = [2, 6, 7, 8, 12, 15]
    group_2 = [4, 9, 10, 16, 17, 18]

    # Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check the robot visits exactly one city from each group
    if len(tour) != 5:  # considering starting/ending at depot plus one city from each group
        return "FAIL"

    groups = [group_0, group_1, group_2]
    visited = set(tour[1:-1])  # excluding the depot

    if any(len(visited.intersection(set(g))) != 1 for g in groups):
        return "FAIL"

    # Calculate and check total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        c1 = tour[i]
        c2 = tour[i+1]
        calculated_cost += euclidean_distance(*coordinates[c1], *coordinates[c2])

    # Check if calculated cost matches given total cost with a rounding approximation due to floating point precision
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"


# Provided solution's tour and total travel cost
tour = [0, 1, 8, 4, 0]
total_cost = 110.09

# Verify solution
result = verify_solution(tour, total_argument)
print(result)  # Output "CORRECT" if everything is OK, "FAIL" if it's not.