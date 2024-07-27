import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, cities):
    # Requirement 1: The robot must start and end its tour at the depot city, which is city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit a total of 4 cities including the depot city
    if len(tour) != 5:
        return "FAIL"
    
    # Requirement 3: The goal is to determine the shortest round-trip tour using Euclidean distance
    total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if abs(total_distance - 110.09) > 1e-2:
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    8: (61, 16),
    4: (25, 18)
}

# Proposed tour and calculated travel cost
tour = [0, 1, 8, 4, 0]
calculated_travel_cost = 110.09

# Validate the solution
result = verify_solution(tour, cities)
print(result)