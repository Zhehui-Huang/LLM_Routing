import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    cities = {
        0: (14, 77),
        1: (34, 20),
        2: (19, 38),
        3: (14, 91),
        4: (68, 98),
        5: (45, 84),
        6: (4, 56),
        7: (54, 82),
        8: (37, 28),
        9: (27, 45),
        10: (90, 85),
        11: (98, 76),
        12: (6, 19),
        13: (26, 29),
        14: (21, 79),
        15: (49, 23),
        16: (78, 76),
        17: (68, 45),
        18: (50, 28),
        19: (69, 9)
        
    }
    
    groups = [
        [5, 6, 7, 11, 17],
        [1, 4, 8, 13, 16],
        [2, 10, 15, 18, 19],
        [3, 9, 12, 14]
    ]
    
    given_tour = [0, 6, 2, 13, 9, 0]
    given_total_cost = 108.66
    
    # Requirement 1: Starts and ends at depot 0
    if given_tour[0] != 0 or given_tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visiting exactly one city from each group
    visited_groups = {group_index: False for group_index in range(len(groups))}
    for city in given_tour[1:-1]:  # Excluding the depot at start and end
        for group_index, group in enumerate(groups):
            if city in group:
                if visited_groups[group_index]:
                    return "FAIL"
                visited_groups[group_info_index] = True
                break
    if not all(visited_groups.values()):
        return "FAIL"
    
    # Requirement 3: Total travel cost is calculated correctly
    calculated_cost = 0
    for i in range(len(given_tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[given_tour[i]], cities[given_tour[i + 1]])
    
    if not math.isclose(calculated_cost, given_total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Run the test and print the result
print(test_solution())