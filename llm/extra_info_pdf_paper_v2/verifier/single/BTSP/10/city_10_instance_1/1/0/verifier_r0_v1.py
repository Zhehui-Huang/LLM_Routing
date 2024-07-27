import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities, tour, given_total_cost, given_max_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # The robot must start and end at depot city 0.
    if sorted(tour[:-1]) != sorted(cities.keys()):
        return "FAIL"  # Must visit each city exactly once, not assuming multiple same-city visits.
    
    # Calculate cost and max distance in the given tour
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)

    # Check calculated cost and maximum distance
    if not math.isclose(calculated_total_cost, given_total_cost, rel_tol=1e-5) or not math.isclose(calculated_max_distance, given_max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given cities and test case
cities = {
    0: (53, 68),
    3: (22, 80),
    5: (54, 91),
    8: (17, 69),
}

proposed_tour = [0, 3, 8, 5, 0]
proposed_total_cost = 111.39
proposed_max_distance = 43.05

# Verify the solution
result = verify_solution(cities, proposed_tour, proposed_total_cost, proposed_max_distance)
print(result)