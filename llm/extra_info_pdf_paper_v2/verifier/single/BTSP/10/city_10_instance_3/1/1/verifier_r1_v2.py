import math

# Given data and solution tour
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
solution_tour = [0, 1, 2, 4, 3, 9, 5, 6, 7, 8, 0]
reported_total_cost = 379.34
reported_max_distance = 68.26

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Verify Requirement 1: Start and end at depot city 0
def test_start_end_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Verify Requirement 2: Each city must be visited exactly once
def test_visit_once(tour):
    visited = set(tour)
    expected = set(range(len(cities)))
    return visited == expected and len(tour) == len(cities) + 1  # Including return to depot

# Verify Requirement 3: Compare computed and reported longest distance between consecutive cities
def test_max_distance_accuracy(tour, reported_max_distance):
    max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    return math.isclose(max_distance, reported_max_distance, rel_tol=1e-2)

# Calculate total travel cost of the tour
def calculate_total_cost(tour):
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return total_cost

# Run verification tests
def run_tests(tour, reported_max_distance, reported_total_cost):
    if not test_start_end_depot(tour):
        return "FAIL"
    if not test_visit_once(tour):
        return "FAIL"
    total_cost = calculate_total_cost(tour)
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-2):
        return "FAIL"
    if not test_max_distance_accuracy(tour, reported_max_distance):
        return "FAIL"
    return "CORRECT"

# Execute tests and print the result
result = run_tests(solution_tour, reported_max_distance, reported_total_cost)
print(result)