import math

# Define the cities and their coordinates
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

# Obtained tour from the solution
tour = [0, 16, 14, 7, 12, 9, 11, 15, 18, 3, 10, 2, 6, 19, 5, 17, 13, 8, 1, 4, 0]
reported_cost = 349.20

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Verify if the robot starts and ends at depot
def test_start_end_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Verify if all cities are visited once
def test_visit_all_cities_once(tour):
    return sorted(tour[1:-1]) == list(range(1, 20))

# Verify the total travel cost
def test_total_travel_cost(tour):
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    return math.isclose(total_cost, reported_cost, rel_tol=1e-2)

# Check no subtours
def test_subtours(tour):
    city_set = set(tour)
    return len(city_set) == len(tour)  # No duplicate entries means no subtours

# Run all tests
def validate_solution(tour):
    if not test_start_end_at_depot(tour):
        return "FAIL: The tour does not start and end at the depot."
    if not test_visit_all_cities_once(tour):
        return "FAIL: Not all cities are visited exactly once."
    if not test_total_travel_cost(tour):
        return "FAIL: The total travel cost does not match the reported cost."
    if not test_subtours(tour):
        return "FAIL: There are subtours in the solution."
    return "CORRECT"

# Execute validation
print(validate_solution(tour))