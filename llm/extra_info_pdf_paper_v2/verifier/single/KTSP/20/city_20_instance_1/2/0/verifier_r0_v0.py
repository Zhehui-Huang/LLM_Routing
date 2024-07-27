import math

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Given solution
tour = [0, 6, 2, 13, 8, 9, 14, 0]
computed_cost = 130.6658168109853

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, computed_cost):
    # Check the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check exactly 7 cities are visited including depot city
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Calculate the travel cost and compare with computed cost
    total_cost = 0
    for i in range(len(tour)-1):
        city1 = tour[i]
        city2 = tour[i+1]
        total_cost += calculate_euclidean_distance(cities[city1], cities[city2])
    if not math.isclose(total_cost, computed_cost, rel_tol=1e-9):
        return "FAIL"
    
    # The tour should be exactly as specified and the cost should match exactly
    return "CORRECT"

# Perform the unit test based on the provided solution tour and its computed cost
result = verify_tour(tour, computed_cost)
print(result)