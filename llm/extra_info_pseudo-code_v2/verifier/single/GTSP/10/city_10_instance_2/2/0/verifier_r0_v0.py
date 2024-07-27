import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    cities = {
        0: (90, 3),
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
    city_groups = [
        [3, 6],
        [5, 8],
        [4, 9],
        [1, 7],
        [2]
    ]
    solution_tour = [0, 3, 4, 5, 2, 1, 0]
    solution_cost = 276.3

    # Check if the tour starts and ends at city 0
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"

    # Calculate the total travel cost from the tour
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        calculated_cost += calculate_distance(cities[solution_tour[i]], cities[solution_tour[i+1]])

    # Check if the calculated cost is approximately equal to the given solution cost
    if not math.isclose(calculated_cost, solution_cost, rel_tol=1e-2):
        return "FAIL"

    # Check if the tour visits exactly one city from each group
    visited_groups = {i: False for i in range(len(city_groups))}
    for city in solution_tour:
        for group_index, group in enumerate(city_groups):
            if city in group:
                if visited_groups[group_index]:
                    return "FAIL"  # This group was visited more than once
                visited_groups[group_index] = True

    # Ensure all groups were visited
    if not all(visited_groups.values()):
        return "FAIL"

    return "CORRECT"

# Run the test
test_result = test_solution()
print(test_result)