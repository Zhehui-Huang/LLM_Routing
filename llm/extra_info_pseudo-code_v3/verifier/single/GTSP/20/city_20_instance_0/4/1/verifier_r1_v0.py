import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # City coordinates
    cities = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
        5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
        10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
        15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }

    # Groups of cities
    groups = [
        {1, 3, 5, 11, 13, 14, 19},
        {2, 6, 7, 8, 12, 15},
        {4, 9, 10, 16, 17, 18}
    ]

    # Requirement 1: Starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit one city from each group
    visited_groups = [set() for _ in groups]
    for idx, group in enumerate(groups):
        for city in tour:
            if city in group:
                visited_groups[idx].add(city)
    
    if any(len(g) != 1 for g in visited_groups):
        return "FAIL"

    # Requirement 3: Check travel cost calculation
    calc_cost = 0
    for i in range(len(tour) - 1):
        calc_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    calc_cost = round(calc_cost, 2)
    if calc_cost != total_cost:
        return "FAIL"

    # Requirements 4 and 5 are met if the other checks pass
    return "CORRECT"

# Solution provided
solution_tour = [0, 1, 8, 4, 0]
solution_cost = 110.09

# Verify the solution
result = verify_solution(solution_tour, solution_cost)
print(result)