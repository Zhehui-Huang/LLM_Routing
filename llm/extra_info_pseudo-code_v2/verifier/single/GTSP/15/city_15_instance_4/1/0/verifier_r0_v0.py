import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, total_cost_calculated, coordinates, groups):
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour visits one city from each group
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # exclude the depot city at start and end
        found_group = False
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # A group is visited more than once
                visited_groups[i] = True
                found_group = True
                break
        if not found_group:
            return "FAIL"  # City does not belong to any group
    
    if not all(visited_groups):
        return "FAIL"  # Not all groups were visited

    # Check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost_calculated, rel_tol=1e-5):
        return "FAIL"  # The reported cost does not match the calculated cost

    return "CORRECT"

# City coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Defined city groups
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9],
    [7, 12], [10, 11]
]

# Given solution
tour = [0, 1, 5, 7, 4, 6, 3, 10, 0]
total_cost_calculated = 223.46

# Verify the solution
result = verify_solution(tour, total_cost_calculated, coordinates, city_groups)
print(result)