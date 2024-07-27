import math

# Provided tour and total travel cost
tour = [0, 4, 11, 13, 5, 0]
provided_total_travel_cost = 148.86963273650017

# City coordinates
coordinates = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# City groups
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}


def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)


def verify_tour(tour, groups, provided_total_travel_cost):
    """ Verify the correctness of the tour based on the provided constraints. """
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # excluding first and last city (depot city 0)
        for group_id, cities in groups.items():
            if city in cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.add(group_id)
    if len(visited_groups) != len(groups):
        return "FAIL"

    # Calculate the tour total cost and compare it
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    if not math.isclose(total_cost, provided_total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Unit test execution
result = verify_tour(tour, groups, provided_total_travel_cost)
print(result)