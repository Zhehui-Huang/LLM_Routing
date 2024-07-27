import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # Define city coordinates
    cities = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
        5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
        10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
    }

    # Define city groups
    groups = [
        [8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]
    ]

    # [Requirement 1] Check if exactly one city from each group is visited
    visited_groups = [False] * len(groups)
    for city in tour:
        for group_index, group in enumerate(groups):
            if city in group:
                if visited_group[group_index]:  # corrected variable name
                    return "FAIL"
                visited_groups[group_index] = True

    if not all(visited_groups):
        return "FAIL"

    # [Requirement 2] Check if the total travel cost is correctly calculated
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    # [Requirement 3] Check if tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    return "CORRECT"

# Provided solution details
solution_tour = [0, 6, 11, 0]
solution_cost = 26.73541702731773

# Verify solution
result = verify_solution(solution_tour, solution_cost)
print(result)