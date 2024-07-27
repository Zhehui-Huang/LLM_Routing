import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

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
    cities_visited_once = all(tour.count(city) == 1 for city in range(1, 10))

    # [Requirement 2] Check tour starts and ends at depot city 0
    starts_and_ends_at_depot = tour[0] == 0 and tour[-1] == 0

    # [Requirement 3 & 5] Calculate the total travel cost and compare
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Check total cost against reported
    cost_match = math.isclose(total_cost, reported_cost, rel_tol=1e-5)

    # Check and return status
    if cities_visited_once and starts_and_ends_at_depot and cost_match:
        return "CORRECT"
    else:
        return "FAIL"

# Test the given solution
tour_given = [0, 3, 4, 6, 7, 5, 9, 1, 2, 8, 0]
total_cost_given = 374.96
result = verify_tsp_solution(tour_given, total_cost_given)
print(result)