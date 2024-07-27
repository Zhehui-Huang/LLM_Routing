import math

# Define the cities based on the given coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Tour and cost provided as a solution
tour = [0, 3, 14, 5, 7, 4, 10, 11, 16, 17, 19, 15, 18, 8, 1, 13, 12, 2, 9, 6, 0]
provided_total_cost = 376

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_validity(tour, provided_total_cost, total_cities=20):
    # Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all other cities are visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != total_cities - 1 or any(city not in visited for city in range(1, total_cities)):
        return "FAIL"

    # Calculate total travel cost and check
    calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if abs(calculated_cost - provided_total_cost) > 1e-4:  # Allowing a small tolerance for floating point precision
        return "FAIL"

    return "CORRECT"

# Evaluate the solution correctness
result = verify_tour_validity(tour, provided_total_cost)
print(result)