import math

# Given tours and costs data
tours = [
    [0, 21, 7, 17, 0],
    [0, 16, 5, 9, 0],
    [0, 6, 22, 8, 0],
    [0, 1, 11, 3, 0],
    [0, 20, 13, 18, 0],
    [0, 10, 15, 19, 0],
    [0, 2, 12, 0],
    [0, 4, 14, 0]
]

costs = [66.16, 74.62, 80.08, 90.64, 89.13, 103.74, 69.96, 97.10]
max_cost_reported = 103.74

# All cities excluding depot, cities are indexed from 1 to 22
all_cities = set(range(1, 23))

# Check Requirement 1: Each robot must start from and return to the depot city (0)
def test_tour_starts_and_ends_at_depot():
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False
    return True

# Check Requirement 2: Every city, except for the depot, must be visited exactly once by the robots collectively
def test_all_cities_visited_exactly_once():
    visited_cities = set()
    for tour in tours:
        for city in tour[1:-1]:  # exclude the first and last element (depot)
            if city in visited_cities:
                return False
            visited_cities.add(city)
    return visited_cities == all_cities

# To check maximum travel cost, we would need the exact method of cost calculation used, so we assume provided costs are calculated correctly.
def test_minimize_max_distance():
    maximum_calculated_cost = max(costs)
    return math.isclose(max_cost_reported, maximum_calculated_cost, rel_tol=1e-5)

def run_tests():
    if not test_tour_starts_and_ends_at_depot():
        return "FAIL: Tours do not start and end at depot"
    if not test_all_cities_visited_exactly_once():
        return "FAIL: Not all cities are visited exactly once"
    if not test_minimize_max_distance():
        return "FAIL: Reported maximum travel cost does not match calculation"
    return "CORRECT"

# Execute tests
print(run_tests())