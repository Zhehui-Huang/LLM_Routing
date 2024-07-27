import math

# Input data from the problem
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Solution provided
tour = [0, 7, 1, 2, 4, 6, 5, 9, 8, 3, 0]
total_travel_cost = 373.4782116274554
maximum_distance = 95.2732911156112

# Validate the solution
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_requirements(tour, cities, expected_cost, expected_max_dist):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Every city must be visited exactly once
    if sorted(tour) != sorted(list(range(len(cities))) + [0]):
        return "FAIL"

    # Calculate total travel cost and max distance
    total_cost = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_dist:
            max_dist = dist

    # Check calculated cost and max distance against expected values
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5) or not math.isclose(max_dist, expected_max_dist, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Running the test function
result = check_requirements(tour, cities, total_travel_cost, maximum_distance)
print(result)