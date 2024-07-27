import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, group_0, group_1, group_2, city_positions):
    # Check if the tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = [0 for _ in range(3)]
    for city_index in tour[1:-1]:  # ignore the depot city at start and end
        if city_index in group_0:
            visited_groups[0] += 1
        elif city_index in group_1:
            visited_groups[1] += 1
        elif city_index in group_2:
            visited_groups[2] += 1

    if not all(count == 1 for count in visited_groups):
        return "FAIL"

    # Calculate total travel cost
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(city_positions[tour[i]], city_positions[tour[i+1]])

    # Comparing provided travel cost with a calculated one might not be exact due to rounding, use an epsilon
    provided_distance = 122.22
    if not math.isclose(total_distance, provided_distance, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# City positions index corresponds to city number
city_positions = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39),  # City 14
]

# City groups
group_0 = [2, 7, 10, 11, 14]
group_1 = [1, 3, 5, 8, 13]
group_2 = [4, 6, 9, 12]

# Provided tour solution
provided_tour = [0, 10, 1, 9, 0]

# Perform the test
result = verify_tour(provided_tour, group_0, group_1, group_2, city_positions)
print(result)