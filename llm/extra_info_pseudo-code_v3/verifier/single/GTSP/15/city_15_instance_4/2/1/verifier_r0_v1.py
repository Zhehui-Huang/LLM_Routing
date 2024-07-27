import math

def calculate_distance(c1, c2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def test_solution():
    cities = {
        0: (35, 40),
        1: (39, 41),
        2: (81, 30),
        3: (5, 50),
        4: (72, 90),
        5: (54, 46),
        6: (8, 70),
        7: (97, 62),
        8: (14, 41),
        9: (70, 44),
        10: (27, 47),
        11: (41, 74),
        12: (53, 80),
        13: (21, 21),
        14: (12, 39)
    }
    
    groups = {
        0: [3, 8],
        1: [4, 13],
        2: [1, 2],
        3: [6, 14],
        4: [5, 9],
        5: [7, 12],
        6: [10, 11]
    }

    tour_solution = [0, 8, 13, 1, 14, 5, 12, 11, 0]
    reported_cost = 220.73043826129523

    # Check if the robot starts and ends at the depot city
    if tour_solution[0] != 0 or tour_to_solution[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_from_groups = set()
    for city in tour_solution[1:-1]:
        found = False
        for group_id, cities in groups.items():
            if city in cities:
                if group_id in visited_from_groups:
                    return "FAIL"  # More than one city from the same group visited
                visited_from_groups.add(group_id)
                found = True
        if not found:
            return "FAIL"  # City does not belong to any group

    if len(visited_from_groups) != len(groups):
        return "FAIL"  # Not all groups are visited exactly once

    # Calculate the total travel cost
    calculated_cost = 0
    for i in range(len(tour_solution) - 1):
        calculated_cost += calculate_distance(cities[tour_solution[i]], cities[tour_solution[i + 1]])

    # Check if the calculated cost is close to the reported cost
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the test
result = test_solution()
print(result)