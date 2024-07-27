import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities, groups):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Check if one city from each group is visited
    visited_groups = set()
    for city_index in tour[1:-1]:  # exclude the depot city from check
        for group_index, group in enumerate(groups):
            if city_index in group:
                visited_groups.add(group_index)
    if visited_groups != set(range(len(groups))):
        return False

    # Check if the calculated travel cost is correct
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-2):
        return False

    return True

# Data for the problem
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}
groups = [
    [1, 2, 6],  # Group 0
    [3, 7, 8],  # Group 1
    [4, 5, 9]   # Group 2
]

# Provided solution
tour = [0, 6, 7, 5, 0]
total_cost = 74.95

# Verify the solution
is_correct = verify_solution(tour, total_cost, cities, groups)
print("CORRECT" if is_correct else "FAIL")