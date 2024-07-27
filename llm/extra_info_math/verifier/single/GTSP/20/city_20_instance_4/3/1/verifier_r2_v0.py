import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, expected_cost):
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }
    groups = {
        0: [5, 6, 16], 1: [8, 18, 19], 2: [11, 12, 13], 3: [1, 3, 9],
        4: [2, 4, 14], 5: [10, 17], 6: [7, 15]
    }
    
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    visited_groups = set()
    for city in tour:
        for group_id, group_cities in groups.items():
            if city in group_cities:
                visited_groups.add(group_id)
                break
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # [Requirement 3]
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    if abs(total_cost - expected_cost) > 0.01:  # Accounting for floating-point precision issues
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 8, 17, 9, 12, 6, 4, 15, 0]
total_travel_cost = 187.16

# Verify the solution
result = verify_solution(tour, total_travel_cost)
print(result)