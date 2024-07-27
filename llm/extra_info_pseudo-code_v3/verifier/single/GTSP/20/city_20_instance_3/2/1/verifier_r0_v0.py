import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost, cities, city_groups):
    # Requirement 1: Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if one city from each group is visited exactly once
    group_membership = {i: False for i in range(len(city_groups))}
    for city in tour[1:-1]:  # exclude start/end depot city for checking groups
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_membership[group_index] == True:
                    return "FAIL"
                group_membership[group_index] = True
                break
            
    if not all(group_membership.values()):
        return "FAIL"
    
    # Calculate the total travel cost from the cities coordinates
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += euclidean_distance(cities[city1], cities[city2])
    
    # Requirement 4 & 5: Check if the calculated cost matches the provided total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Data
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Given solution details
tour = [0, 4, 7, 12, 15, 3, 18, 0]
total_cost = 227.4

# Test the solution
result = verify_solution(tour, total_cost, cities, city_groups)
print(result)