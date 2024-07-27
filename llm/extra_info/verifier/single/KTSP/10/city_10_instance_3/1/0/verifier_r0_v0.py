import math

# Given data for example output validation
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82),
    4: (97, 28), 5: (0, 31), 6: (8, 62), 7: (74, 56),
    8: (85, 71), 9: (6, 76)
}

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, stated_cost):
    n = len(tour)
    if n != 8:  # Starts and ends at the depot, visiting 7 unique cities including the depot
        return "FAIL"
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != 8:  # Tour should contain exactly 8 unique nodes (7 cities + depot visited twice)
        return "FAIL"
    
    calculated_cost = sum(calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(n-1))
    
    # Allow a small floating point margin
    if not math.isclose(calculated_cost, stated_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and cost from the solution
tour = [0, 4, 2, 1, 7, 3, 8, 0]
total_travel_cost = 159.97188184793015

# Validate the tour and the computed total travel cost
result = verify_tour(tour, total_travel_cost)
print(result)