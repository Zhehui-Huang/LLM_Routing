import math

# Define cities and groups
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

groups = {
    0: [3, 8],
    1: [4, 13],
    2: [1, 2],
    3: [6, 14],
    4: [5, 9],
    5: [7, 12],
    6: [10, 11]
}

tour = [0, 13, 14, 8, 11, 12, 5, 1, 0]
computed_cost = 156.55750207016007

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[b][0] - cities[a][0]) ** 2 + (cities[b][1] - cities[a][1]) ** 2)

# Check if the tour starts and ends at the depot city
def check_depot_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if exactly one city from each group is visited
def check_one_city_per_group(tour, groups):
    visited = set(tour[1:-1])
    unique_groups = [set(g) & visited for g in groups.values()]
    return all(len(g) == 1 for g in unique_groups) and len(unique_groups) == len(groups)

# Check for subtours and compute total travel cost
def check_no_subtours_and_total_cost(tour, expected_cost):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    costs_match = abs(total_cost - expected_cost) < 0.001
    tour_unique_check = len(tour) == len(set(tour)) + 1  # +1 to account for the repeated depot
    return costs_match and tour_unique_check

# Validate the solution
def validate_solution(tour, groups, expected_cost):
    requirements = [
        check_depot_start_end(tour),
        check_one_city_per_group(tour, groups),
        check_no_subtours_and_total_cost(tour, expected_cost)
    ]
    return "CORRECT" if all(requirements) else "FAIL"

# Run validation
result = validate_solution(tour, groups, computed_cost)
print(result)