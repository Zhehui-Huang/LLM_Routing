import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, city_groups, cities, expected_cost):
    # Check Requirement 1: Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Visit exactly one city from each group
    visited_cities = set(tour) - {0}
    group_check = all(len(set(group).intersection(visited_cities)) == 1 for group in city_groups)
    if not group_check:
        return "FAIL"
    
    # Check Requirement 3: Verify cost
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(total_cost, expected_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Define cities and groups from environment information
cities = {
    0: (3, 26), 
    1: (85, 72), 
    2: (67, 0),
    3: (50, 99), 
    4: (61, 89), 
    5: (91, 56), 
    6: (2, 65), 
    7: (38, 68), 
    8: (3, 92), 
    9: (59, 8), 
    10: (30, 88), 
    11: (30, 53), 
    12: (11, 14), 
    13: (52, 49), 
    14: (18, 49), 
    15: (64, 41), 
    16: (28, 49), 
    17: (91, 94), 
    18: (51, 58), 
    19: (30, 48)
}

city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Provided tour and expected cost
tour = [0, 6, 0, 12, 0, 14, 0, 16, 0, 18, 0]
expected_cost = 345.1069597079202

# Execute the test
result = verify_solution(tour, city_groups, cities, expected_cost)
print(result)