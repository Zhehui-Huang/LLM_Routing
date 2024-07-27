import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(cities, proposed_tour, proposed_cost):
    # City coordinates from the problem description
    coordinates = [
        (90, 3), (11, 17), (7, 27), (95, 81), (41, 54),
        (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
    ]

    # Check if tour starts and ends at the depot city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Check if all cities except depot are visited exactly once
    city_visit_count = {i: 0 for i in range(len(coordinates))}
    for city in proposed_tour:
        city_visit_count[city] += 1

    if city_visit_count[0] != 2:  # depot city should be visited twice
        return "FAIL"
    if any(count != 1 for idx, count in city_visit_count.items() if idx != 0):  # other cities visited exactly once
        return "FAIL"

    # Check the calculated distance matches the proposed cost
    calculated_cost = 0
    for i in range(len(proposed_tour) - 1):
        calculated_cost += calculate_distance(coordinates[proposed_tour[i]], coordinates[proposed_tour[i + 1]])

    if not math.isclose(calculated_cost, proposed_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
total_cost = 354.91

# Output the result of verification
print(verify_solution(10, tour, total_cost))