import math

# City Coordinates
cities = [
    (8, 11),   # City 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Provided solution
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 32.38826948140329
max_distance = 32.38826948140329

def check_tour(tour, cities, expected_total_cost, expected_max_distance):
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check all cities visited exactly once
    if sorted(tour[:-1]) != list(range(20)):
        return "FAIL"

    # Calculate total travel cost and max distance
    actual_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        actual_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance

    # Check if calculated total cost and max distance match expected values
    if not (math.isclose(actual_cost, expected_total_cost, rel_tol=1e-5) and 
            math.isclose(actual_max_distance, expected_max_distance, rel_tol=1e-5)):
        return "FAIL"

    return "CORRECT"

# Verify the tour
result = check_tour(tour, cities, total_travel_cost, max_distance)
print(result)