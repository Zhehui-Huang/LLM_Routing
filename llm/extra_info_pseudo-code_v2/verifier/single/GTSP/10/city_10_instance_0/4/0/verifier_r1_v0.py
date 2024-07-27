from math import sqrt

def calculate_euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour_and_cost(tour, reported_cost, cities, groups):
    # Check start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check the tour visits exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the depot city at start and end
        for group_idx, group in enumerate(groups):
            if city in group:
                if group_idx in visited_even or any([city not in groups[i] for i in visited_groups]):
                    return "FAIL"
                visited_groups.add(group_idx)

    if len(visited_groups) != len(groups):
        return "FAIL"

    # Check the travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city_index1 = tour[i]
        city_index2 = tour[i + 1]
        total_cost += calculate_euclidean_distance(cities[city_index1][0], cities[city_index1][1],
                                                   cities[city_index2][0], cities[city_index2][1])

    if not (abs(total_cost - reported_cost) < 1e-2):  # allow some float precision tolerance
        return "FAIL"

    return "CORRECT"

# City coordinates (index: (x, y))
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

# City groups
groups = [
    [1, 2, 6],  # Group 0
    [3, 7, 8],  # Group 1
    [4, 5, 9]   # Group 2
]

# Given tour solution and its total travel cost
tour_solution = [0, 5, 6, 7, 0]
reported_cost = 72.83

# Validate the solution
result = verify_tour_and_cost(tour_solution, reported_cost, cities, groups)
print(result)