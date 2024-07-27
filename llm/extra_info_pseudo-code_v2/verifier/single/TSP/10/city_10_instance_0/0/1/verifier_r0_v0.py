import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_cost(tour, total_travel_cost, cities):
    # Check Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"

    # Check Requirement 3
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"

    # We cannot directly verify Requirement 4 as it requires running and comparing with the Lin-Kernighan algorithm.
    
    # Check Requirement 5
    if not isinstance(tour, list) or not isinstance(total_travel_cost, float):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Provided tour and cost
tour = [0, 5, 9, 4, 8, 3, 2, 1, 6, 7, 0]
total_travel_cost = 271.4716218753353

# Run the verification
result = verify_tour_and_cost(tour, total_travel, cities)
print(result)