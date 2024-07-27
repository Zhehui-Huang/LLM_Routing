import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution():
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

    city_groups = [
        [5, 6, 7, 11, 17],
        [1, 4, 8, 13, 16],
        [2, 10, 15, 18, 19],
        [3, 9, 12, 14]
    ]
    
    # Given solution
    solution_tour = [0, 6, 0, 0]  # This appears as the final output tour
    solution_cost = 46.51881339845203

    # Check Requirment 1: Start and end at the depot
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"

    # Build unique set of visited groups
    visited_groups = set()
    for city in solution_tour:
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(i)
    
    # Check Requirement 2: One city per group
    if len(visited_groups) != 4:
        return "FAIL"
    
    # Calculate the actual tour cost
    actual_cost = 0
    for i in range(len(solution_tour) - 1):
        actual_cost += euclidean_distance(cities[solution_tour[i]], cities[solution_tour[i + 1]])
    
    # Check Requirement 3: Minimized travel distance
    if not math.isclose(actual_cost, solution_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Run test
output = check_solution()
print(output)