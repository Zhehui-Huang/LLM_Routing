import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, city_coordinates, city_groups):
    # Check the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify each group is represented exactly once
    visited = set(tour) - {0}  # excluding depot
    for group in city_groups:
        if not (visited & set(group)):
            return "FAIL"
        
    # Check distances
    total_distance = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour)-1))
    if total_distance != 0:
        return "FAIL"
    
    return "CORRECT"

# City coordinates for the problem, indexed by city number
city_coordinates = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# City groups, indexed by group number
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Solution to verify
tour = [0, 2, 12, 0]
total_travel_cost = 0

# Verification
result = verify_solution(tour, city_coordinates, city_groups)
print(result)