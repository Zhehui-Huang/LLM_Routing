import math

def calculate_euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_requirements(tour, expected_cost):
    # Coordinates of each city
    coordinates = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    # City groups
    city_groups = [[5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]]

    # [Requirement 1]: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]: Visit exactly one city from each group
    visited_groups = [False] * len(city_groups)
    for city in tour[1:-1]:
        for idx, group in enumerate(city_groups):
            if city in group:
                if visited_groups[idx]:
                    return "FAIL"
                visited_groups[idx] = True
                break

    if not all(visited_groups):
        return "FAIL"
    
    # [Requirement 3]: Check the total travel cost using the Euclidean distance
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    if not math.isclose(actual_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Test input
tour = [0, 8, 17, 13, 9, 6, 4, 15, 0]
expected_cost = 208.32

# Output the test result
print(verify_requirements(tour, expected_cost))