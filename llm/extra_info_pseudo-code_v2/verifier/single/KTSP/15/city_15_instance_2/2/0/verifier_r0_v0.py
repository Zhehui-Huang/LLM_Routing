import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return total_cost

def verify_solution(tour, total_cost, coordinates):
    # Requirement 1: Check if exactly 8 cities are visited, including the start and end at the depot
    if len(set(tour)) != 8 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Ignored in checking as it is about input setup

    # Requirement 3: Check computed travel cost matches the reported cost
    computed_cost = calculate_total_travel_cost(tour, coordinates)
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # Requirement 4: Cannot be tested here as it pertains to algorithm process adherence

    # Requirement 5: Starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    return "CORRECT"

# Assuming the tour and total cost are given by the earlier message
given_tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
given_total_cost = 132.1185774560832

# Cities coordinates including the depot
coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

result = verify_solution(given_tour, given_total_cost, coordinates)
print(result)