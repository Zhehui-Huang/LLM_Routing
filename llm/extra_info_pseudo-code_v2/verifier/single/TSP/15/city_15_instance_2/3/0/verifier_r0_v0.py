import math

# Define the cities and their coordinates
cities = {
    0: (54, 87),  # Depot
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Define the proposed tour and its cost
proposed_tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
proposed_cost = 322.5

# Calculates the Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check if tour starts and ends at the depot
def check_start_end(tour, depot=0):
    return tour[0] == depot and tour[-1] == depot

# Check if all cities are visited exactly once, except the depot which must be visited twice
def check_visit_once(tour):
    from collections import Counter
    count = Counter(tour)
    return all(count[i] == 1 for i in cities if i != 0) and count[0] == 2

# Calculate the total tour cost and compare with the proposed cost
def check_total_cost(tour, expected_cost):
    total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return math.isclose(total_cost, expected_cost, rel_tol=1e-5)

# Compliance unit test
def test_tour_validation():
    # [Requirement 1] Tour starts and ends at depot
    if not check_start_end(proposed_tour):
        return "FAIL"
    
    # [Requirement 2] All cities visited exactly once except the depot
    if not check_visit_once(proposed_tour):
        return "FAIL"

    # [Requirement 3] Travel Cost Check
    if not check_total_cost(proposed_tour, proposed_cost):
        return "FAIL"
    
    return "CORRECT"

# Test the tour
result = test_tour_validation()
print(result)