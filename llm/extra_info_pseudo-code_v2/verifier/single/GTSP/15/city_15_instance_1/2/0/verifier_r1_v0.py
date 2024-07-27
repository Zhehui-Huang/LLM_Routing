import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, cost):
    city_coordinates = [
        (29, 51),  # Depot city 0
        (49, 20),  # City 1
        (79, 69),  # City 2
        (17, 20),  # City 3
        (18, 61),  # City 4
        (40, 57),  # City 5
        (57, 30),  # City 6
        (36, 12),  # City 7
        (93, 43),  # City 8
        (17, 36),  # City 9
        (4, 60),   # City 10
        (78, 82),  # City 11
        (83, 96),  # City 12
        (60, 50),  # City 13
        (98, 1)    # City 14
    ]

    city_groups = [
        [1, 2, 5, 6],
        [8, 9, 10, 13],
        [3, 4, 7],
        [11, 12, 14]
    ]

    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check unique visit of each group
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # Exclude depot in the beginning and end
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1
                if visited_groups[i] > 1:
                    return "FAIL"
    
    if not all(visited_groups):
        return "FAIL"

    # Check cost computation
    computed_cost = 0.0
    for i in range(len(tour)-1):
        computed_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    if not math.isclose(computed_cost, cost, rel_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Example Tour and Cost from solution
tour = [0, 5, 10, 4, 11, 0]
cost = 184.24203302868492

result = verify_solution(tour, cost)
print(result)