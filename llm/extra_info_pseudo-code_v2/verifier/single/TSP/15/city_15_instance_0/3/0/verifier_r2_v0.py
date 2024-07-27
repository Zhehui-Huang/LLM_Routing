import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost):
    cities = [
        (9, 93),  # City 0 (Depot)
        (8, 51),  # City 1
        (74, 99), # City 2
        (78, 50), # City 3
        (21, 23), # City 4
        (88, 59), # City 5
        (79, 77), # City 6
        (63, 23), # City 7
        (19, 76), # City 8
        (21, 38), # City 9
        (19, 65), # City 10
        (11, 40), # City 11
        (3, 21),  # City 12
        (60, 55), # City 13
        (4, 39)   # City 14
    ]

    # [Requirement 1] The robot must start and end the tour at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] The robot must visit all other cities exactly once.
    if sorted(tour) != list(range(15)):
        return "FAIL"

    # [Requirement 3, 4 and 5] Check the total distance and ensure it's the shortest as provided
    computed_cost = 0
    for i in range(len(tour)-1):
        city1 = tour[i]
        city2 = tour[i+1]
        computed_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1],
                                                      cities[city2][0], cities[city2][1])
    
    # Precision may vary slight due to floating point arithmetic, so we allow small tolerance
    if not math.isclose(computed_cost, total_travel_cost, abs_tol=1e-2):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Provided solution verification
result = verify_solution(
    tour=[0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0],
    total_travel_cost=373.97
)

print(result)