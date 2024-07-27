import math

# Given data
cities = {
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
groups = {
    0: [1, 6, 14],
    1: [5, 12, 13],
    2: [7, 10],
    3: [4, 11],
    4: [2, 8],
    5: [3, 9]
}

# Proposed solution to test
tour = [0, 14, 5, 10, 11, 8, 9, 0]
calculated_cost = 166.75801920718544

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_tour(tour, groups, calculated_cost):
    # Check the starting and ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city chosen is from a distinct group
    group_validation = set()
    for key, group in groups.items():
        if not any(city in tour for city in group):
            return "FAIL"
        for city in group:
            if city in tour:
                if key in group_validation:
                    return "FAIL"
                group_play = {g_key: g_value for g_key, g_value in groups.items() if city in g_value}
                if any(key != k for k in group_play.keys()):
                    return "FAIL"
                group_validation.add(key)
    
    # Calculating the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    
    # Check if the total cost is matched
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Perform the test
result = check_tour(tour, groups, calculated_cost)
print(result)