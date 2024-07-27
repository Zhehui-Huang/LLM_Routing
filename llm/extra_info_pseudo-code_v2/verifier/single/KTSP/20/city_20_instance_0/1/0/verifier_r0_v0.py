import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost):
    # Define cities with their coordinates
    cities = {
        0: (8, 11),   1: (40, 6),   2: (95, 33),  3: (80, 60),
        4: (25, 18),  5: (67, 23),  6: (97, 32),  7: (25, 71),
        8: (61, 16),  9: (27, 91), 10: (91, 46), 11: (40, 87),
        12: (20, 97), 13: (61, 25), 14: (5, 59),  15: (62, 88),
        16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }

    # Check Requirement 1: Exactly 4 cities including depot
    if len(tour) != 5 or len(set(tour)) != 5:  # Includes return to depot
        return "FAIL"

    # Check Requirement 2: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the total travel distance
    computed_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        computed_cost += calculate_euclidean_distance(
            cities[city_from][0], cities[city_from][1], 
            cities[city_to][0], cities[city_to][1]
        )

    # Check Requirement 5: Correctly reported travel cost
    if not math.isclose(computed_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided tour and cost
tour = [0, 17, 13, 1, 0]
total_travel_cost = 119.36755419871886

# Verify the solution
result = verify_solution(tour, total_travel_stepost)
print(result)