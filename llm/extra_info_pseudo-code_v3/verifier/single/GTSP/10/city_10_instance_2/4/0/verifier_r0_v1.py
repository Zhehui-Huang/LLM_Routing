import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution():
    cities = {
        0: (90, 3),   # depot
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }
    groups = [
        [3, 6],
        [5, 8],
        [4, 9],
        [1, 7],
        [2]
    ]
    solution_tour = [0, 3, 5, 9, 1, 2, 0]
    reported_cost = 281.60273931778477

    # Check if tour starts and ends at depot (city 0)
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"

    # Check if tour visits exactly one city from each group
    found_groups = [0] * len(groups)
    for city in solution_tour[1:-1]:  # exclude the depot city (start and end)
        for i, group in enumerate(groups):
            if city in group:
                found_groups[i] += 1
    if any(count != 1 for count in found_groups):
        return "FAIL"

    # Calculate and validate the travel cost
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        calculated_cost += euclidean_distance(cities[solution_tour[i]], cities[solution_tour[i+1]])

    # Check if the reported total travel cost matches the calculated travel cost
    if abs(calculated_cost - reported_cost) > 0.001:
        return "FAIL"

    return "CORRECT"

# Execute the verification
result = verify_solution()
print(result)