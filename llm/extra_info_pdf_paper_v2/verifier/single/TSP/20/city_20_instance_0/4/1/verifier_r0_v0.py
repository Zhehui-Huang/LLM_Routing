import math

# Given data
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
reported_cost = 349.2

# Check the requirements
def calculate_euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Check if all cities are visited exactly once except depot
def check_cities_visited_once(tour):
    visit_counts = {index: 0 for index in range(20)}
    for city in tour:
        visit_counts[city] += 1
    # Depot should be visited exactly twice (start and end), every other city exactly once
    return all(count == 1 for i, count in visit_counts.items() if i != 0) and visit_counts[0] == 2

# Calculate tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_idist_cost

def unit_test_tour_constraints(tour, reported_cost):
    if len(tour) != 21:
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if not check_cities_visited_once(tour):
        return "FAIL"
    # Calculate and compare tour cost
    calculated_cost = calculate_tour_cost(tour)
    if abs(calculated_cost - reported_cost) > 0.0001:  # Allowing a small error margin
        return "FAIL"
    return "CORRECT"

# Running the test
test_result = unit_test_tour_constraints(tour, reported_cost)
print(test_result)