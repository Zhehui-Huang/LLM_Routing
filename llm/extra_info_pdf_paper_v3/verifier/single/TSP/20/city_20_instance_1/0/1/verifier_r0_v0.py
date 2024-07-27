import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, cost):
    cities = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
        (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
        (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
        (50, 28), (69, 9)
    ]
    
    # Check Requirement 1: Start and End at Depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Visit each city exactly once
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL"
    
    # Check Requirement 3: Compute and verify the travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        computed_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(computed_cost, cost, rel_tol=1e-4):
        return "FAIL"
    
    # Check Requirement 5: Output includes correct tour and cost
    # As cost and tour check is already performed above, we assume output format is correct if passed
    
    return "CORRECT"


tour = [0, 3, 14, 5, 7, 4, 10, 11, 16, 17, 19, 15, 18, 8, 1, 13, 12, 2, 9, 6, 0]
total_cost = 376.93470962470616

# Add check if all cities are visited exactly once except depot (covered implicitly in sorted list check)
if len(tour) != 21 or len(set(tour)) != 20 and len(tour) != len(set(tour)):
    print("FAIL")
else:
    result = verify_tour(tour, total_cost)
    print(result)