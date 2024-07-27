def calculate_euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def verify_requirements(tour, travel_cost):
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
    for city in tour[1:-1]:  # Skip the depot city at start and end
        for group_index, group in enumerate(groups):
            if city in group:
                visited_groups.add(group_index)
                break

    if len(visited_groups) != len(groups):
        return "FAIL"

    # [Requirement 3] Verify the total Euclidean distance
    computed_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        computed_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])

    if not (abs(computed_cost - travel_cost) < 0.01):  # Considering a small floating-point tolerance
        return "FAIL"

    return "CORRECT"

# Provided solution from the MILP solver
tour = [0, 6, 0]
travel_cost = 10.77

# Run the verification
result = verify_requirements(tour, travel_network)
print(result)  # This should print "CORRECT" if everything is as expected, else "FAIL"