def calculate_euclidean_distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points.
    """
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def verify_requirements(tour, travel_cost):
    """
    Verify the solution against the given requirements.
    """
    # Coordinates for the cities
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }

    groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

    # [Requirement 1] Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the start/end city in validation
        found = False
        for group_index, group in enumerate(groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups.add(group_index)
                found = True
                break
        if not found:
            return "FAIL"
    
    if len(visited_groups) != len(groups):
        return "FAIL"

    # [Requirement 3] Verify the total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        computed_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    if not (abs(computed_cost - travel_cost) < 0.001):  # Allowing small precision difference
        return "FAIL"

    return "CORRECT"

# Example test case
tour = [0, 8, 10, 4, 3, 2, 0]
travel_cost = 53.036

# Run the verification
result = verify_requirements(tour, travel_cost)
print(result)  # Should print "CORRECT" if the solution meets requirements, otherwise "FAIL"