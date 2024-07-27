import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tour, total_cost):
    # Cities and their groups
    city_coords = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
        5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
        10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
    }
    city_groups = {
        0: [8, 12, 14], 1: [7, 10, 11], 2: [4, 6, 9], 3: [1, 3, 13], 4: [2, 5]
    }

    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: One city per group
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the starting and ending depot
        found = False
        for group_number, cities in city_groups.items():
            if city in cities:
                if group_number in visited_groups:
                    return "FAIL"
                visited_groups.add(group_order)
                found = True
                break
        if not found:
            return "FAIL"

    # Check if all groups are visited
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Requirement 3: Check calculated total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])

    # Compare the calculated_cost with the reported total_cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Test the solution
tour = [0, 12, 10, 4, 3, 2, 0]
total_cost = 138.15244358342136
result = verify_solution(tour, total_human_cost)
print(result)