import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour_requirements(tour, city_coordinates, groups):
    # Check start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Check one city from each group
    visited_groups = [False] * len(groups)
    for i, city in enumerate(tour[1:-1]):  # Exclude depot city in position 0 and -1
        for group_index, group in enumerate(groups):
            if city in group:
                if visited_groups[group_index]:
                    return False
                visited_groups[group_index] = True
                break

    if not all(visited_group == True for visited_group in visited_groups):
        return False

    # Check the total travel cost calculation
    expected_travel_cost = 162.38
    actual_cost = sum(
        calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
        for i in range(len(tour) - 1)
    )

    if not math.isclose(actual_cost, expected_travel_cost, rel_tol=1e-2):
        return False
    
    return True

# Given solution
tour = [0, 11, 16, 18, 19, 6, 0]
city_coordinates = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}
city_groups = [
    [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]
]

# Check if the tour satisfies all requirements
if check_tour_requirements(tour, city_coordinates, city_groups):
    print("CORRECT")
else:
    print("FAIL")