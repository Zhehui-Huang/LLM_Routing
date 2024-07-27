import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour_and_cost(coords, tour, reported_cost):
    n = len(coords)
    visited = [False] * n
    total_cost = 0.0
    for i in range(1, len(tour)):
        city1, city2 = tour[i - 1], tour[i]
        if not (0 <= city1 < n and 0 <= city2 < n):
            return False
        total_cost += euclidean_distance(coords[city1], coords[city2])
        if city1 != 0 and city2 != 0:
            visited[city1] = True
        
    # Check if tour begins and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if all cities are visited exactly once excluding the depot
    if not all(visited[1:]):
        return False
    
    # Check proximity of computed cost to the reported cost (to handle floating point imprecision)
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-3):
        return False
    
    return True

# Coordinates from the problem statement
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Provided solution
tour = [0, 14, 16, 11, 7, 10, 3, 4, 1, 19, 17, 5, 6, 8, 2, 9, 15, 13, 18, 12, 0, 0]
reported_cost = 692.58

# Validation
if verify_tour_and_cost(coords, tour, reported_cost):
    print("CORRECT")
else:
    print("FAIL")