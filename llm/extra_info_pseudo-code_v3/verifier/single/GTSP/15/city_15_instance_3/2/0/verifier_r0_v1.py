import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_tour(tour, cost):
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
    groups = [
        [1, 6, 14],
        [5, 12, 13],
        [7, 10],
        [4, 11],
        [2, 8],
        [3, 9]
    ]
    
    # If tour is None
    if tour is None:
        return "FAIL"

    # Requirement 1: The robot visits exactly one city from each group of cities
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # Exclude depot city from checking
        for index, group in enumerate(groups):
            if city in group:
                if visited_gefrom math import sqrtroups[index]:
                    return "FAIL"
                visited_groups[index] = True

    if not all(visited_groups):
        return "FAIL"
    
    # Requirement 2: The tour must start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3: Travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i+1]
        calculated_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])
    
    if not math.isclose(calculated_cost, cost, abs_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Example of the output to test
output_tour = [0, 14, 13, 10, 11, 8, 3, 0]
output_cost = 166.75801920718544
result = test_tour(output_tour, output_cost)

print(result)  # Should print either "CORRECT" or "FAIL"