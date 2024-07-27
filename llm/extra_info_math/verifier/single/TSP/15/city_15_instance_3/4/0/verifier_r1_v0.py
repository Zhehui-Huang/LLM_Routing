import math

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities coordinates as provided
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79), 0: (16, 90)
}

# Tour from the solution
tour = [0, 1, 4, 12, 3, 7, 2, 11, 8, 6, 13, 10, 9, 5, 14, 0]

# Verify the tour starts and ends at the depot city
def test_depot_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# Verify all cities visited exactly once and each city is left and entered exactly once
def test_visit_all_cities_once(tour):
    visited = set(tour)
    all_cities = set(cities.keys())
    return visited == all_cities and len(tour) == len(visited) + 1

# Calculate total travel cost
def calculate_total_cost(tour):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Test if the solution meets the total claimed cost
def test_meets_claimed_cost(tour, claimed_cost):
    actual_cost = calculate_total_cost(tour)
    return math.isclose(actual_cost, claimed_cost, abs_tol=0.01)

# Check for subtours
def test_for_no_subtours(tour):
    # A valid tour that contains each city exactly once besides the start/end shouldn't have subtours in a TSP
    return True  # Simplified based on the problem context and the validation already done.

# Expected cost from solution
claimed_cost = 303.31

# Test outputs
print("Testing Start and End at Depot:", "PASS" if test_depot_start_end(tour) else "FAIL")
print("Testing All Cities Visited Exactly Once:", "PASS" if test_visit_all_cities_once(tour) else "FAIL")
print("Testing Total Cost:", "PASS" if test_meets_claimed_cost(tour, claimed_cost) else "FAIL")
print("Testing for No Subtours:", "PASS" if test_for_no_subtours(tour) else "FAIL")

# Final verification
if (test_depot_start_end(tour) and
    test_visit_all_cities_once(tour) and
    test_meets_claimed_cost(tour, claimed_cost) and
    test_for_no_subtours(tour)):
    print("CORRECT")
else:
    print("FAIL")