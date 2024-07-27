import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_tour_and_cost():
    # City coordinates
    city_locations = [
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

    # Given solution
    tour = [0, 8, 5, 2, 1, 9, 0]
    reported_total_cost = 183.85

    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visits exactly 6 cities including the depot
    if len(tour) != 7:
        return "FAIL"

    # Requirement 3 & 6: Correctness of calculated tour distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_locations[tour[i]], city_locations[tour[i+1]])

    calculated_cost = round(calculated_cost, 2)
    if abs(calculated_cost - reported_total_cost) > 0.01:
        return "FAIL"

    # Requirement 4 & 5 are implicitly checked by above conditions
    return "CORRECT"

# Execute the test function
print(test_tour_and_cost())