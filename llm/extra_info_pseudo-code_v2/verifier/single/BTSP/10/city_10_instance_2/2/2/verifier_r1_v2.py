import math

def calculate_euclidean_distance(city_a, city_b):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def test_solution(tour, total_cost, max_distance):
    """ Test if the provided solution meets the expected requirements. """
    cities = {
        0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
        4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
        8: (49, 29), 9: (13, 17)
    }

    # [Requirement 1]: Ensuring all cities are visited exactly once
    if sorted(tour[:-1]) != sorted(cities.keys()):
        return "FAIL"

    # [Requirement 2]: Tour should start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the travel costs and max distance between consecutive cities
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)

    # [Requirement 3]: Check total travel cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    # [Requirement 4]: Check maximum distance between consecutive cities
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Using the provided solution to run the test
tour = [0, 8, 5, 4, 7, 6, 3, 2, 1, 9, 0]
total_travel_cost = 416.8322265347456
maximum_distance = 103.24727599312246

# Test the solution and print the result
print(test_solution(tour, total_travel_cost, maximum_distance))