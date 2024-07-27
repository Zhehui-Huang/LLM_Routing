import math

# Cities' coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Provided solution details
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
reported_total_cost = 410.03585920085146
reported_max_distance = 89.00561780022652

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, reported_total_cost, reported_max_distance):
    """Verify the solution against the provided requirements."""
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at city 0
    if len(set(tour)) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL"  # All cities must be visited exactly once

    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i+1])
        total_cost += distance
        max_distance = max(max_distance, distance)

    # Compare calculated values with reported values
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(max_distance, reported_max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Unit test to verify the solution
solution_status = verify_solution(tour, reported_total_cost, reported_max_distance)
print(solution_status)