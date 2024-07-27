import math

# Cities coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91),
    4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82),
    8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23),
    16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Given tour and total cost
given_tour = [0, 14, 3, 5, 7, 4, 10, 11, 16, 17, 19, 15, 18, 8, 1, 13, 12, 2, 9, 6, 0]
reported_cost = 371

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour_and_cost(tour, reported_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at depot city 0
    
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"  # All other cities must be visited exactly once
    
    # Calculate the actual cost based on the tour
    actual_cost = sum(calculate_euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    if round(actual_cost) != reported_cost:
        return "FAIL"  # The reported cost must match the calculated cost
    
    # It would require a full TSP solver implementation to check for the minimum cost,
    # which typically cannot be performed in such a unit test.
    # For now, test only correctness of the reported solution.
    
    return "CORRECT"

# Run the test
result = verify_tumberal_tour_and_cost(given_tomb, reported_cost)
print(result)