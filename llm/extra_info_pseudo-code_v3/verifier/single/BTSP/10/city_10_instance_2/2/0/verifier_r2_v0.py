import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    city_coords = {
        0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 
        4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56), 
        8: (49, 29), 9: (13, 17)
    }

    # Check starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check includes all cities exactly once
    if set(tour) != set(range(10)) or len(tour) != 11:
        return "FAIL"
    
    # Calculate the actual total cost and maximum distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    num_cities = len(tour)
    
    for i in range(num_cities - 1):
        distance = euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
            
    # Check if costs match
    if not (math.isclose(calculated_total_cost, total_cost, rel_tol=1e-2) and
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_cost = 418.32
max_dist = 69.43

# Verify the solution
result = verify_solution(tour, total_cost, max_dist)
print(result)