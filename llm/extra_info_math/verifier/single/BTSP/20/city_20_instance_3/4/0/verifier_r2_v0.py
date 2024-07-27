import math

# Given cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Solution tour from the MILP solver
tour = [0, 1, 3, 5, 2, 13, 6, 15, 17, 16, 9, 11, 10, 4, 14, 7, 8, 12, 18, 19, 0]
max_distance_in_tour = 41.0
total_travel_cost = 532.0846683883167

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def verify_tour(tour, cities, max_distance_in_tour, total_travel_cost):
    # Check if the tour starts and ends at the depot, and is cyclic
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once, excluding the depot return
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"
    
    # Calculate and check travel costs and distances
    computed_total_cost = 0
    computed_max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        computed_total_cost += dist
        if dist > computed_max_distance:
            computed_max_distance = dist
    
    if abs(computed_total_cost - total_travel_cost) > 1e-4:
        return "FAIL"
    
    if abs(computed_max_distance - max_distance_in_tour) > 1e-4:
        return "FAIL"
    
    # Verification of sub-tour elimination is complex usually done during model formulation
    # Due to problem reduction, assume this is handled via constraints and properly configured IP model

    return "CORRECT"

# Execute the testing function
result = verify_tour(tour, cities, max_distance_in_tour, total_travel_cost)
print(result)