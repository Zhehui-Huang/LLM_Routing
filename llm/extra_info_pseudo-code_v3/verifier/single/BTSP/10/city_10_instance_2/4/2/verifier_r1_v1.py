import math

# Provided solution
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_travel_cost = 418.32344417340323
maximum_distance_between_cities = 69.42621983083913

# City coordinates
coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Helper function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Test cases
def test_solution():
    # Requirement 1: Tour must start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city must be visited exactly once, except for the depot city 0 (twice)
    city_visit_counts = {key: 0 for key in coordinates.keys()}
    for city in tour:
        city_visit_counts[city] += 1
    city_visit_counts[0] -= 2  # Adjust depot city count for start and end visits
    if any(count != 1 for count in city_visit_counts.values()):
        return "FAIL"
    
    # Requirement 4, 5, 6, 7: Calculating total and max distances and compare it.
    calculated_total_distance = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    calculated_max_distance = max(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    if not math.isclose(calculated_total_distance, total_travel_cost, rel_tol=1e-9) or not math.isclose(calculated_max_distance, maximum_distance_between_cities, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run test
test_output = test_solution()
print(test_output)