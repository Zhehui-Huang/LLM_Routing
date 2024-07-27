import math

cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def verify_solution(tour, total_cost, max_distance):
    # Verify tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify each city is visited once
    if set(tour) != set(range(len(cities))):
        return "FAIL"
    
    # Calculate total travel cost and max distance
    calculated_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        source_city = tour[i]
        destination_city = tour[i + 1]
        distance = euclidean_distance(cities[source_city], cities[destination_city])
        calculated_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)
    
    # Verify costs and distances
    if not (math.isclose(calculated_cost, total_cost, rel_tol=1e-5) and 
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5)):
        return "FAIL"
    
    return "CORRECT"

# Test data from the solution
given_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
given_total_cost = 458.37
given_max_distance = 68.15

# Running the verification
result = verify_solution(given_tour, given_total_cost, given_max_distance)
print(result)