import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, coordinates, city_groups):
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at the depot city."
    
    # Checking if one city from each group is in the tour
    visited_groups = set()
    for city in tour:
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_groups:
                    return False, "Multiple cities from one group are visited."
                visited_groups.add(group_index)
    if len(visited.groups) != len(city_groups):
        return False, "Not all groups are visited."

    # Check if the reported total cost is the sum of distances between consecutive cities
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += euclidean_distance(*coordinates[city1], *coordinates[city2])
    
    if round(calculated_cost, 2) != expected_cost:
        return False, f"Calculated cost {calculated_cost:.2f} does not match the expected cost {expected_cost:.2f}."

    return True, "All constraints satisfied."

# Test data
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]
groups = [
    [8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]
]
tour_solution = [0, 12, 10, 4, 3, 2, 0]
expected_cost = 138.15

# Verification
is_correct, message = verify_tour(tour_solution, coordinates, groups)
if is_correct:
    print("CORRECT")
else:
    print("FAIL:", message)