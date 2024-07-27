import math

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_solution():
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
    city_groups = {
        0: [7, 10, 11, 12],
        1: [3, 8, 13, 16],
        2: [2, 4, 15, 18],
        3: [1, 9, 14, 19],
        4: [5, 6, 17]
    }
    solution_tour = [0, 11, 16, 18, 19, 6, 0]
    solution_cost = 162.38
    
    if len(cities) != 20:
        return "FAIL"
    
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    visited_from_group = set()
    for city in solution_tour[1:-1]:
        for group_id, group_cities in city_groups.items():
            if city in group_cities:
                if group_id in visited_from_group:
                    return "FAIL"
                visited_from_group.add(group_id)
                break
    if len(visited_from_group) != 5:
        return "FAIL"
    
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        calculated_cost += euclidean_distance(cities[solution_tour[i]], cities[solution_tour[i + 1]])
    if not math.isclose(calculated_cost, solution_cost, abs_tol=1):
        return "FAIL"
    
    return "CORRECT"

# Running the test
print(test_solution())