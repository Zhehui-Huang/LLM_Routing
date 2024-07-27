import math

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

# Provided solution
tour = [0, 5, 9, 4, 8, 3, 2, 1, 6, 7, 0]
reported_cost = 271.4716218753353

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def verify_tour(tour, reported_cost):
    # Requirement 1: Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited once, except depot
    unique_cities = set(tour)
    if len(tour) - 1 != len(unique_cities):
        return "FAIL"
    if len(unique_cities) != len(cities):
        return "FAIL"
    
    # Requirement 4: No subtours and each city only once, validated by unique cities check
    
    # Requirement 3: Travel costs calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(tour[i], tour[i+1])

    if not math.isclose(calculated, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Output the verification result
result = verify_tour(tour, reported_cost)
print(result)