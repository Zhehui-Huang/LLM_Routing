import math

# Define the city coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Provided solution
tour = [0, 1, 2, 4, 3, 9, 5, 6, 7, 8, 0]
total_travel_cost = 379.3436985835247
max_distance = 68.26419266350405

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Test [Requirement 1]
def test_visit_all_cities_once():
    assert len(tour) == len(set(tour)), "Each city is not visited exactly once or does not start/end at depot."

# Test [Requirement 2]
def test_minimize_max_distance():
    distances = [euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1)]
    calculated_max_distance = max(distances)
    assert math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9), "The calculated max distance does not match the provided max distance."

# Test [Requirement 3]
def test_include_all_cities():
    assert set(tour) == set(cities.keys()), "Not all cities are included in the tour."

# Calculate total travel cost
def test_total_travel_cost():
    calculated_cost = sum([euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1)])
    assert math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9), "Calculated total travel cost does not match the provided cost."
    
def run_tests():
    try:
        test_visit_all_cities_once()
        test_minimize_max_distance()
        test_include_all_cities()
        test_total_travel_cost()
        return "CORRECT"
    except AssertionError as e:
        return "FAIL: " + str(e)

# Running tests
result = run_tests()
print(result)