import math

# Define the given cities coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Given solution
tour = [0, 3, 19, 6, 13, 18, 7, 4, 10, 11, 16, 0, 0]
reported_cost = 268.45  # As given in the output


def calculate_euclidean_distance(point1, point2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def verify_tour(tour, reported_cost):
    if len(tour) != 13:
        return "FAIL: The tour must have exactly 13 cities."
    
    if tour[0] != 0 or tour[-1] != 0 or tour[-2] != 0:
        return "FAIL: The tour must start and end at the depot city (city 0)."
    
    # Calculate the total travel cost
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    
    # Compare calculated cost with reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return f"FAIL: The reported tour cost {reported_cost} does not match the calculated cost {total_cost:.2f}."
    
    # Check for duplicate visits to the same non-depot city
    if len(set(tour[1:-2])) != len(tour[1:-2]):
        return "FAIL: The tour contains duplicate visits to one or more cities."

    return "CORRECT"

# Run test
result = verify_tour(tour, reported_cost)
print(result)