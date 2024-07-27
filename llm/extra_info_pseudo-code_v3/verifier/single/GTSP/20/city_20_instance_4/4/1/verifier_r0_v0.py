import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, reported_cost):
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }
    groups = [
        [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
        [2, 4, 14], [10, 17], [7, 15]
    ]

    # Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check visit exactly one city from each group
    visited_groups = {idx: False for idx in range(len(groups))}
    for city in tour[1:-1]:  # Exclude the depot at the start and the end
        for group_idx, group in enumerate(groups):
            if city in group:
                if visited_groups[group_idx]:
                    return "FAIL"
                visited_groups[group_idx] = True
    if not all(visited_groups.values()):
        return "FAIL"

    # Calculate and check the tour cost
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, reported_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Solution provided
tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
reported_cost = 266.72

# Test the solution
result = test_solution(tour, reported_cost)
print(result)