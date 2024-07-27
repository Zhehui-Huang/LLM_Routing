import math
from collections import Counter

# City coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Tours given in the solution
robots_tours = [
    [0, 22, 21, 0],
    [0, 19, 7, 0],
    [0, 8, 16, 0],
    [0, 4, 14, 0],
    [0, 15, 6, 0],
    [0, 18, 3, 0],
    [0, 13, 9, 0],
    [0, 11, 12, 10, 1, 2, 17, 5, 20, 0]
]

# Verification function
def verify_solution(robots_tours, expected_total_cost):
    all_cities_visited = [city for tour in robots_tours for city in tour]
    city_count = Counter(all_cities_visited)

    # Requirement 1: Each city visited exactly once, excluding the depot which is repeated
    if any(city_count[city] != 1 for city in range(1, 23)):
        return "FAIL"

    # Requirement 2: Each tour starts and ends at the depot
    if any(tour[0] != 0 or tour[-1] != 0 for tour in robots_tours):
        return "FAIL"

    # Requirement 3: Verify the travel cost is correctly calculated
    total_travel_cost = 0
    for tour in robots_tours:
        tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        total_travel_cost += tour_cost

    if not math.isclose(total_travel_cost, expected_total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Expected total cost from previous calculation
expected_total_cost = 657.0493532775374

# Verification result
verification_result = verify_solution(robots_tours, expected_total_cost)
print(verification_result)