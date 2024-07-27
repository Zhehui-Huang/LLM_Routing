import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(tour, coordinates, groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at the depot city.

    visited_groups = set()
    for i in range(1, len(tour)-1):
        city_index = tour[i]
        for group_index, group_cities in enumerate(groups):
            if city_index in group_cities:
                if group_index in visited_groups:
                    return "FAIL"  # A group is visited more than once.
                visited_groups.add(group_index)

    if len(visited_groups) != len(groups):
        return "FAIL"  # Not all groups are visited.

    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(coordinates[city1], coordinates[city2])

    expected_cost = 169.94095984675323
    if not math.isclose(calculated_cost, expected_cost, abs_tol=1e-5):
        return "FAIL"  # Cost doesn't match the expected optimal cost.

    return "CORRECT"

# Cities' coordinates
coordinates = [
    (53, 68),  # City 0 - depot
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# City groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Tour solution
tour = [0, 8, 3, 5, 9, 0]

result = validate_tour(tour, coordinates, groups)
print(result)  # Expected output: "CORRECT"