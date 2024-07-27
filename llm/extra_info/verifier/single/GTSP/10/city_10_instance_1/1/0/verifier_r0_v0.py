import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def test_solution(tour, expected_cost):
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    groups = [
        [5, 6, 7],
        [2, 3],
        [1, 9],
        [4, 8]
    ]

    # Requirement 1: The robot must start and end the journey at depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: The robot must visit exactly one city from each of the four groups.
    visited_groups = [0 for _ in groups]
    for city in tour[1:-1]:  # Exclude the starting and ending depot city
        for group_index, group in enumerate(groups):
            if city in group:
                visited_groups[group_index] += 1
    
    if not all(v == 1 for v in visited_groups):
        return "FAIL"

    # Requirement 3: Travel cost is calculated using the Euclidean distance formula.
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Example test case given in the problem
tour = [0, 5, 2, 9, 8, 0]
expected_cost = 183.99
result = test_solution(tour, expected_cost)
print(result)