import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, cost):
    # Define the city coordinates
    cities = {
        0: (29, 51),
        1: (49, 20),
        2: (79, 69),
        3: (17, 20),
        4: (18, 61),
        5: (40, 57),
        6: (57, 30),
        7: (36, 12),
        8: (93, 43),
        9: (17, 36),
        10: (4, 60),
        11: (78, 82),
        12: (83, 96),
        13: (60, 50),
        14: (98, 1)
    }
    
    # Groups of cities
    groups = [
        [1, 2, 5, 6],
        [8, 9, 10, 13],
        [3, 4, 7],
        [11, 12, 14]
    ]
    
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly one city from each group
    visited_groups = [0] * len(groups)
    for city_index in tour[1:-1]:  # exclude depots at the start and end
        for group_index, group in enumerate(groups):
            if city_index in group:
                visited_groups[group_index] += 1
                if visited_groups[group_index] > 1:
                    return "FAIL"
    if any(count != 1 for count in visited_groups):
        return "FAIL"
    
    # Requirement 3: Check the travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        computed_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])
    
    if abs(computed_cost - cost) > 1e-9:
        return "FAIL"
    
    return "CORRECT"

# Given solution to verify using the provided tour and cost
result = verify_tour([0, 5, 10, 4, 11, 0], 184.24203302868492)
print(result)  # Output "CORRECT" if the given solution is valid according to the requirements