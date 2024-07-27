import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def check_solution(tour, total_cost, coordinates):
    # Check Requirement 1: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visit each city once, excluding the depot
    if set(tour) != set(range(len(coordinates))):
        return "FAIL"

    # Check Requirement 3: Accuracy of provided total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        computed_cost += calculate_euclidean_distance(coordinates[city_a][0], coordinates[city_a][1], 
                                                      coordinates[city_b][0], coordinates[city_b][1])

    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60),
    (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_cost = 349.1974047195548

result = check_solution(tour, total_cost, coordinates)
print(result)