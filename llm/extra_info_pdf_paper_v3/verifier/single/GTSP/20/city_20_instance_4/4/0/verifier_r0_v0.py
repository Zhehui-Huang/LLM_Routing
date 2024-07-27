import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_total_distance(tour, coordinates):
    distance = 0
    for i in range(len(tour) - 1):
        distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return round(distance, 12)  # rounding to ensure floating point precision issue is minimized

def verify_tour(tour, total_cost, groups, coordinates):
    # Verify starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return False, 'Tour does not start and end at depot city 0.'
    
    # Verify each group is represented exactly once
    visited_groups = set()
    for city in tour[1:-1]:
        for group_index, group_cities in enumerate(groups):
            if city in group_cities:
                if group_index in visited_groups:
                    return False, 'More than one city from a single group visited.'
                else:
                    visited_groups.add(group_index)
                    break
    if len(visited_groups) != len(groups):
        return False, 'Not all groups were visited.'

    # Verify the reported distance is correct
    calculated_cost = calculate_total_distance(tour, coordinates)
    if calculated_cost != total_cost:
        return False, f'Cost mismatches, expected: {calculated_cost}, got: {total_cost}.'

    return True, 'All checks passed.'

# Data setup
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

# Test Tour and cost
tour_provided = [0, 5, 18, 13, 1, 14, 10, 15, 0]
total_cost_provided = 266.71610174713

# Verify solution
is_correct, message = verify_tour(tour_provided, total_cost_provided, groups, coordinates)
if is_correct:
    print("CORRECT")
else:
    print("FAIL:", message)