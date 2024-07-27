import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_and_cost(tour, total_cost):
    # Define cities coordinates
    cities = [
        (3, 26),   # Depot city 0
        (85, 72),  # City 1
        (67, 0),   # City 2
        (50, 99),  # City 3
        (61, 89),  # City 4
        (91, 56),  # City 5
        (2, 65),   # City 6
        (38, 68),  # City 7
        (3, 92),   # City 8
        (59, 8),   # City 9
        (30, 88),  # City 10
        (30, 53),  # City 11
        (11, 14),  # City 12
        (52, 49),  # City 13
        (18, 49),  # City 14
        (64, 41),  # City 15
        (28, 49),  # City 16
        (91, 94),  # City 17
        (51, 58),  # City 18
        (30, 48)   # City 19
    ]

    # Validate the constraints listed
    groups = [
        [7, 10, 11, 12],
        [3, 8, 13, 16],
        [2, 4, 15, 18],
        [1, 9, 14, 19],
        [5, 6, 17]
    ]

    # Checking that the route starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking group constraints
    visited = set(tour[1:-1])  # Excluding the depot city
    for group in groups:
        if not (len(visited.intersection(set(group))) == 1):
            return "FAIL"

    # Checking that one and only one city is visited from each group
    counted = sum([city in visited for city in sum(groups, [])])
    if counted != 5:
        return "FAIL"

    # Compute the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Comparing calculated total cost to the given cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided Solution:
tour = [0, 11, 16, 18, 19, 6, 0]
total_cost = 162.38

# Running the verification
print(verify_tour_and_cost(tour, total_cost))