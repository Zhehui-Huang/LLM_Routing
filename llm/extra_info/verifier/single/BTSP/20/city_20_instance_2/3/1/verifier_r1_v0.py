import math

def is_valid_tour(tour, total_cost_check, max_distance_check):
    # Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once except depot (0), which should be visited twice
    visited = set(tour)
    if len(visited) != 21 or 0 not in visited:
        return "FAIL"

    # Verify each value in tour is correct and within bounds
    for city in visited:
        if city < 0 or city > 19:
            return "FAIL"

    # Check maximal distance and total cost
    max_distance_actual = 0
    total_distance_actual = 0

    for i in range(1, len(tour)):
        city1 = tour[i - 1]
        city2 = tour[i]
        distance = dist(cities[city1], cities[city2])
        total_distance_actual += distance
        if distance > max_distance_actual:
            max_distance_actual = distance

    if math.isclose(total_distance_actual, total_cost_check) and math.isclose(max_distance_actual, max_distance_check):
        return "CORRECT"
    else:
        return "FAIL"

def dist(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Define cities coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48),
}

# Corresponding to provided example, adjust indices and values to real testing data
tour_example = [0, 1, 2, 3, 0]
total_cost_example = 100  # Adjust to actual estimated cost for the example
max_distance_example = 40  # Adjust to actual max distance for the example

# Run the test
test_result = is_valid_tour(tour_example, total_cost_example, max_distance_example)
print(test_result)