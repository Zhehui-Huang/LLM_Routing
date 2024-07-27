import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, reported_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour does not start and end at depot city
    
    if len(tour) != len(set(tour)):
        return "FAIL"  # Tour contains duplicate cities
    
    unique_cities_visited = set(tour) - {0}
    if len(unique_cities_visited) != len(cities) - 1:
        return "FAIL"  # Not all cities are visited exactly once
    
    # Calculate the total tour cost and compare with the reported cost
    total_cost = 0
    previous_city = tour[0]
    for city in tour[1:]:
        total_cost += calculate_euclidean_distance(cities[previous_city], cities[city])
        previous_city = city
    
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"  # Reported travel cost does not match calculated cost
    
    return "CORRECT"

# Cities are defined as {index: (x, y)}
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

# Solution particulars
tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
reported_cost = 295.9919678938414

# Compute the verification result
verification_result = verify_solution(tour, reported_cost, cities)
print(verification_result)