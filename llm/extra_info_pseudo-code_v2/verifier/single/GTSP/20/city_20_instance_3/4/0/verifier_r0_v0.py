import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # Requirement 1: Tour starts and ends at the depot city (city index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visits exactly one city from each of the 6 distinct groups
    visited_groups = {group_index: set() for group_index in range(len(city_groups))}
    for city_index in tour[1:-1]:  # Exclude the first and last city (depot)
        for group_index, cities in enumerate(city[0] for city in city_groups):
            if city_index in cities:
                if city_index in visited_groups[group_index]:
                    return "FAIL"  # City repeated in the same group
                visited_groups[group_index].add(city_index)
    
    if not all(len(visited_groups[group_index]) == 1 for group_index in range(len(city_groups))):
        return "FAIL"  # Some group was not visited exactly once

    # Requirement 3: Travel cost calculated using Euclidean distance
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(total_cost, computed_cost, rel_tol=1e-5):
        return "FAIL"  # Computed travel cost does not match the provided cost

    # Requirement 4 & 5: Correct tour structure and total travel cost
    return "CORRECT"

city_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

tour = [0, 11, 16, 15, 6, 13, 19, 0]
total_cost = 219.43829363969311

result = verify_solution(tour, total_cost, city_coordinates, city_groups)
print(result)