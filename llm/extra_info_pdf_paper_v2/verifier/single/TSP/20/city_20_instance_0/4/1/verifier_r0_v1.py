import math

# City coordinates
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

# Solution provided
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
reported_cost = 349.2

def calculate_euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def validate_tour(tour, reported_cost):
    # Check if all cities are visited exactly once, with depot revisited
    if set(tour) != set(range(20)) or tour.count(0) != 2:
        return "FAIL: Incorrect city visits."

    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot."

    # Check the reported cost
    calculated_cost = calculate_tour_cost(tour)
    if not math.isclose(calculated_cost, reported_cost, abs_tol=1e-1):
        return f"FAIL: Cost discrepancy. Calculated: {calculated_cost}, Reported: {reported_cost}"
    
    return "CORRECT"

# Test the tour and cost
test_result = validate_tour(tour, reported_cost)
print(test_result)