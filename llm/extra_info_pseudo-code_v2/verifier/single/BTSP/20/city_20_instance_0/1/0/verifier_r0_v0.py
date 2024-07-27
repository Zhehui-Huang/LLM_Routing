import math

# Coordinates of cities (city index corresponds to position in the list)
coordinates = [
    (8, 11),   # city 0
    (40, 6),   # city 1
    (95, 33),  # city 2
    (80, 60),  # city 3
    (25, 18),  # city 4
    (67, 23),  # city 5
    (97, 32),  # city 6
    (25, 71),  # city 7
    (61, 16),  # city 8
    (27, 91),  # city 9
    (91, 46),  # city 10
    (40, 87),  # city 11
    (20, 97),  # city 12
    (61, 25),  # city 13
    (5, 59),   # city 14
    (62, 88),  # city 15
    (13, 43),  # city 16
    (61, 28),  # city 17
    (60, 63),  # city 18
    (93, 15)   # city 19
]

# Given tour solution
solution_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
solution_total_cost = 349.20
solution_max_distance = 32.39

def euclidean_distance(a, b):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def check_requirements(tour, total_cost, max_distance):
    # Check all cities are visited exactly once and tour starts/ends at the depot city
    if len(tour) != len(set(tour)) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate actual total travel cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist

    # Check total travel cost and max distance with acceptable rounding errors
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-2) or \
       not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Run the test
test_result = check_requirements(solution_tour, solution_total_cost, solution_max, distance)
print(test_result)