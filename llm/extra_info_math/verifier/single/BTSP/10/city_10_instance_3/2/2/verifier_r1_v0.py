import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities, tour, expected_total_cost, expected_max_distance):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour contains all cities exactly once (except depot city appearing twice)
    if sorted(tour) != sorted([0] + list(range(1, len(cities)))):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        max_dist = max(max_dist, dist)

    # Compare calculated cost and distance with expected values
    if not (math.isclose(total_cost, expected_total_total_cost, rel_tol=1e-5) and 
            math.isclose(max_dist, expected_max_distance, rel_tol=1e-5)):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Given results from the solver
tour = [0, 8, 7, 6, 5, 9, 3, 4, 1, 2, 0]
expected_total_cost = 402.01969629628246
expected_max_distance = 68.26419266350405

# Performing the unit test
test_result = verify_solution(cities, tour, expected_total_cost, expected_max_distance)
print(test_result)