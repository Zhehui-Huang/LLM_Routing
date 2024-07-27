import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tsp_solution(tour, reported_cost):
    # City coordinates
    city_coordinates = [
        (90, 3),   # Depot city 0
        (11, 17),  # City 1
        (7, 27),   # City 2
        (95, 81),  # City 3
        (41, 54),  # City 4
        (31, 35),  # City 5
        (23, 95),  # City 6
        (20, 56),  # City 7
        (49, 29),  # City 8
        (13, 17)   # City 9
    ]

    # [Requirement 1] Check if all cities are visited exactly once
    visited = set(tour)
    if len(visited) != 11 or any(tour.count(city) != 1 for city in range(1, 10)):
        return "FAIL"

    # [Requirement 2] Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 3 & 5] Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Compare calculated cost and reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Test the given solution
tour_given = [0, 3, 4, 6, 7, 5, 9, 1, 2, 8, 0, 0]
total_cost_given = 374.96
result = verify_tvp_solution(tour_given, total_cost_given)
print(result)