import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost):
    # Define cities coordinates
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
    
    # Define groups
    groups = [
        [7, 10, 11, 12],
        [3, 8, 13, 16],
        [2, 4, 15, 18],
        [1, 9, 14, 19],
        [5, 6, 17]
    ]
    
    # Requirement 1: Check start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check exactly one city from each group
    visited_groups = [0] * len(groups)
    for city_index in tour[1:-1]:  # Exclude the starting and ending depot
        group_found = False
        for group_index, group in enumerate(groups):
            if city_index in group:
                visited_groups[group_index] += 1
                group_found = True
                break
        if not group_found or visited_groups[group_index] > 1:
            return "FAIL"
    
    if any(group_count != 1 for group_count in visited_groups):
        return "FAIL"
    
    # Requirement 3: Check the total distance
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        calculated_total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-9):  # Accurate comparison for floating point
        return "FAIL"
    
    return "CORRECT"

# Given solution check
tour = [0, 11, 16, 18, 19, 6, 0]
total_cost = 162.3829840233368
print(test_solution(tour, total_cost))