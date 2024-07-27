import math

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Provided solution
tour = [0, 4, 8, 3, 5, 0]
reported_cost = 110.38072506104011

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, reported_cost):
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visits exactly 5 cities, including the depot
    if len(set(tour)) - 1 != 4:  # subtracting the repeated depot city
        return "FAIL"
    
    # Requirement 3: Check the calculated total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run verification on the provided tour and reported total cost
result = verify_tour(tour, reported_cost)
print(result)