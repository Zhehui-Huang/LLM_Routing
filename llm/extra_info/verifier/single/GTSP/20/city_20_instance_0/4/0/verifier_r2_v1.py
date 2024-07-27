import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_travel_cost):
    # Cities coordinates
    cities = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
        5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
        10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
        15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }
    
    # City groups
    groups = [
        {1, 3, 5, 11, 13, 14, 19},
        {2, 6, 7, 8, 12, 15},
        {4, 9, 10, 16, 17, 18}
    ]

    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    visited_groups = [False] * 3
    for i in tour[1:-1]:
        for idx, group in enumerate(groups):
            if i in group:
                if visited_groups[idx]:
                    return "FAIL"
                visited_groups[idx] = True
                break
    if not all(visited_groups):
        return "FAIL"
    
    # [Requirement 3 & 5]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    # [Requirement 4]
    if len(tour) != 5:
        return "FAIL"
    
    return "CORRECT"

# Solution provided
tour = [0, 1, 8, 4, 0]
total_travel_cost = 110.09

# Run the unit test
print(test_solution(tour, total_travelood_cost))