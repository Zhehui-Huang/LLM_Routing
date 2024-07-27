import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(cities, tour, reported_cost):
    total_travel_cost = 0
    # Verify start and end at depot, and only visited cities appear in tour
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify exactly 8 cities are visited
    unique_cities = set(tour)
    if len(unique_cities) != 8:
        return "FAIL"
    
    # Calculate the travel cost and compare it with reported cost
    for i in range(len(tour) - 1):
        total_travel_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Compare calculated cost to reported cost with a tolerance for floating point arithmetic issues
    if not math.isclose(total_travel_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given city coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Tour to be verified and reported cost
tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
reported_cost = 132.12

# Output the result of the verification
verification_result = verify_tour(cities, tour, reported_cost)
print(verification_result)