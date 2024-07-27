import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour_and_cost(cities, groups, tour, expected_cost):
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour visits exactly one city from each group
    visited_groups = []
    for city in tour[1:-1]:  # exclude the depot city at the beginning and the end
        for group_index, group in enumerate(groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.append(group_index)
                break

    if len(visited_groups) != len(groups):
        return "FAIL"

    # Calculate the total travel cost and compare with the expected cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(total_calculated_cost, expected_cost, rel_tol=0.01):  # set a small tolerance for float comparison
        return "FAIL"

    return "CORRECT"

# Define city coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 83), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8),  (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Define groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Given solution tour and cost
tour = [0, 16, 19, 18, 11, 6, 0]
given_cost = 150.52899415429272

# Run the verification
result = verify_tail_and_cost(cities, groups, tour, given_cost)
print(result)