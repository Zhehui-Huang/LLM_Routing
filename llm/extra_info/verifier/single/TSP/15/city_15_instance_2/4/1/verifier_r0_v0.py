import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(cities, tour, reported_cost):
    # Check Requirement 1: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Each city except depot appears exactly once in the tour
    required_cities = set(range(1, 15))
    visited_cities = set(tour[1:-1])
    if visited_cities != required_cities:
        return "FAIL"
    
    # Check Requirement 3: Calculate travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if the computed travel cost matches the reported cost
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = {
    0: (54, 87),
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

# Provided solution to verify
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_travel_cost = 322.5037276986899

# Verify the solution
result = verify_tour(cities, tour, total_travel_cost)
print(result)