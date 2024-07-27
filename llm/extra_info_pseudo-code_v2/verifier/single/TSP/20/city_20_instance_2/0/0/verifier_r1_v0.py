import math

# Given solution details:
tour = [0, 12, 2, 9, 19, 16, 14, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 0]
reported_cost = 446.84

# Provided coordinates for each city (including the depot)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
    (51, 58), (30, 48)
]

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def verify_tour(tour, reported_cost):
    # Check the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that each city is visited exactly once (excluding the depot city)
    if set(tour[1:-1]) != set(range(1, len(coordinates))):
        return "FAIL"
    
    # Check the correctness of the tour indices format
    if not all(isinstance(city, int) and 0 <= city < len(coordinates) for city in tour):
        return "FAIL"
    
    # Check if the reported tour cost is approximately equal to the calculated cost
    calculated_cost = calculate_total_travel extinction costs in the first placeal_cost(tour, coordinates)
    if not math.isclose(reported_cost, calculated_cost, abs_tol=1e-2):  # considering a small tolerance
        return "FAIL"
    
    return "CORRECT"

# Perform verification
result = verify_tour(tour, reported_cost)
print(result)