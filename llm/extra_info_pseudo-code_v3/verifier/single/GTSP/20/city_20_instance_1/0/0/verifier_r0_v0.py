import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost):
    # City coordinates
    coordinates = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
        (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
        (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    # City groups
    groups = [
        [5, 6, 7, 11, 17],
        [1, 4, 8, 13, 16],
        [2, 10, 15, 18, 19],
        [3, 9, 12, 14]
    ]

    # Verify tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify only one city from each group is visited
    visited_groups = [0 for _ in range(len(groups))]
    for city in tour[1:-1]:  # Exclude the depot city at beginning and end
        for group_index, group in enumerate(groups):
            if city in group:
                visited_more_than_once = visited_groups[group_index] >= 1
                visited_groups[group_index] += 1
                if visited_more_than_once:
                    return "FAIL"

    if not all(x == 1 for x in visited_groups):
        return "FAIL"

    # Verify correct calculation of the total travel cost
    calculated_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    if abs(calculated_cost - cost) > 0.001:  # Allowing a small error due to floating point arithmetic
        return "FAIL"

    return "CORRECT"

# Tour and cost from the provided solution
tour = [0, 6, 13, 2, 9, 0]
cost = 114.65928837582914

# Check if the provided solution meets the requirements
print(verify_solution(tour, cost))