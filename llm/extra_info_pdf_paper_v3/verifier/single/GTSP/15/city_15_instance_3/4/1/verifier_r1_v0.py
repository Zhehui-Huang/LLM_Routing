import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_travel_cost):
    # City coordinates
    cities = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }

    # Groups of cities
    groups = [[1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]]
    
    # Check Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2
    visited_groups = 0
    unique_cities = set(tour)
    if len(tour) - 2 != len(groups):
        return "FAIL"
    
    for group in groups:
        if not any(city in group for city in tour[1:-1]):
            return "FAIL"
        visited_groups += 1
    
    if visited_groups != len(groups):
        return "FAIL"
    
    # Check Requirement 3 & 4
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 5 is implicitly verified by the function inputs.
    
    return "CORRECT"

# Provided example solution to be verified
sample_tour = [0, 14, 5, 9, 8, 10, 4, 0]
sample_total_travel_cost = 138.22028342379204

# Verifying the sample solution
result = verify_tour(sample_tour, sample_total_travel_cost)
print(result)