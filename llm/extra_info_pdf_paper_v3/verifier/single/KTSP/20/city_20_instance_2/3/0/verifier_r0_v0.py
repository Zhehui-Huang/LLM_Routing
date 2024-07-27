import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def test_solution(tour, total_cost):
    # Constraint: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Constraint: Exactly 10 cities, including the depot
    if len(set(tour)) != 10:
        return "FAIL"

    # Constraint: Output tour starting and ending at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Define the coordinates of each city
    coordinates = [
        (3, 26),   # Depot city 0
        (85, 72),  # City 1
        (67, 0),   # City 2
        (50, 99),  # City 3
        (61, 89),  # City 4
        (91, 56),  # City 5
        (2, 65),   # City 6
        (38, 68),  # City 7
        (3, 92),   # City 8
        (59, 8),   # City 9
        (30, 88),  # City 10
        (30, 53),  # City 11
        (11, 14),  # City 12
        (52, 49),  # City 13
        (18, 49),  # City 14
        (64, 41),  # City 15
        (28, 49),  # City 16
        (91, 94),  # City 17
        (51, 58),  # City 18
        (30, 48)   # City 19
    ]

    # Verify Euclidean distance calculation for total cost
    computed_total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        computed_total_cost += calculate_distance(x1, y1, x2, y2)

    if abs(computed_total_cost - total_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Given solution details
tour = [0, 12, 15, 13, 18, 7, 11, 19, 16, 14, 0]
total_cost = 175.47723265355

# Test the solution
result = test_solution(tour, total_cost)
print(result)