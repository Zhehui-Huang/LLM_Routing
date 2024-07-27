import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, cost, cities):
    # Check requirement 1 and 4: Start and End at Depot City 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement 2: Visit all cities exactly once, except depot
    unique_cities = set(tour)
    if len(tour) != len(unique_cities) or len(unique_cities) != len(cities):
        return "FAIL"
    
    # Check requirement 3 and 5: Calculate total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Using a tolerance for floating point comparison
    if not math.isclose(cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided cities
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# Solution provided
tour = [6, 1, 7, 9, 2, 5, 0, 4, 8, 3, 0]
total_cost = 244.74754583280696

# Verify the solution
result = verify_solution(tour, total_cost, cities)
print(result)