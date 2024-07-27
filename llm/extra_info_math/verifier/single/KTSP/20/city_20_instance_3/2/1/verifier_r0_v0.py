import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost):
    # Cities coordinates
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
        (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
        (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
        (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2
    if len(tour) != 14 or len(set(tour)) != 14:  # 13 cities plus the home city visited twice
        return "FAIL"
    
    # Requirement 3
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 0]
total_cost = 273.7443523737762

# Verify the provided solution
result = verify_solution(tour, total_cost)
print(result)