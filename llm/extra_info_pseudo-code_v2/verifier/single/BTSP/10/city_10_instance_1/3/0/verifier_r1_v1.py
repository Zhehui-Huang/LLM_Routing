import math

# Define the city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Provided solution details
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
reported_total_cost = 291.41
reported_max_distance = 56.61

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Verify Requirement 2: Starts and ends at City 0
def test_starts_ends_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Verify Requirement 3: Visits each city exactly once
def test_visit_each_city_once(tour):
    visited = set(tour)
    return len(tour) - 1 == len(visited) - 1 == 9  # Extra check for uniqueness except the depot repeat

# Verify Requirement 6: Tour includes output from city 0 back to city 0 and all cities in between
def test_proper_output_format(tour):
    return isinstance(tour, list) and all(isinstance(city, int) for city in tour)

# Verify Requirement 8: Accurate maximum distance reporting
def test_max_distance(tour, reported_max_distance):
    max_distance = max(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return math.isclose(max_distance, reported_max_distance, abs_tol=0.01)

# Verify Requirement 7: Accurate travel cost calculation
def test_total_travel_cost(tour, reported_total_cost):
    total_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return math.isclose(total_cost, reported_total_cost, abs_tol=0.01)

# Unit tests execution
if (test_starts_ends_at_depot(tour) and
    test_visit_each_city_once(tour) and
    test_proper_output_format(tour) and
    test_max_distance(tour, reported_max_distance) and
    test_total_travel_cost(tour, reported_total_cost)):
    print("CORRECT")
else:
    print("FAIL")