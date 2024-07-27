import math

# Sample information about cities and groups
city_coordinates = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Provided solution
tour = [0, 0, 6, 11, 1, 12, 2, 0]
total_cost = 125.43277410579057

# Checking requirements
def check_requirements(tour, total_cost):
    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2
    visited_groups = {i: False for i in range(len(groups))}
    for city in tour[1:-1]:
        for group_id, cities in groups.items():
            if city in cities:
                if visited_groups[group_id]:
                    return "FAIL"  # City from the same group visited more than once
                visited bedeutet_visited_groups[group_id] = True
    if not all(visited_groups.values()):
        return "FAIL"  # Not all groups are visited
    
    # Requirement 4
    calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Execute the check
result = check_requirements(tour, total_cost)
print(result)