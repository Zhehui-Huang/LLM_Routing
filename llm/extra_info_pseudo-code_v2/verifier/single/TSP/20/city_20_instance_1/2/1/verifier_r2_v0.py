import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cost):
    # Define the cities based on the information in the problem description
    cities = [
        (14, 77),  # Depot 0
        (34, 20),  # City 1
        (19, 38),  # City 2
        (14, 91),  # City 3
        (68, 98),  # City 4
        (45, 84),  # City 5
        (4, 56),   # City 6
        (54, 82),  # City 7
        (37, 28),  # City 8
        (27, 45),  # City 9
        (90, 85),  # City 10
        (98, 76),  # City 11
        (6, 19),   # City 12
        (26, 29),  # City 13
        (21, 79),  # City 14
        (49, 23),  # City 15
        (78, 76),  # City 16
        (68, 45),  # City 17
        (50, 28),  # City 18
        (69, 9)    # City 19
    ]

    # Requirement 1: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit each city exactly once
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"

    # Requirement 3: All pairs traveled between are cities
    # Assuming intrinsic check that all tour indices are valid indices of cities

    # Calculate the actual cost from the given tour
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Round the cost to two decimal places for comparison
    actual_cost = round(actual_cost, 2)

    # Requirement 6: Check if provided cost matches the calculated cost
    if actual_cost != cost:
        return "FAIL"

    # If all checks pass, the solution is considered correct.
    return "CORRECT"

# Suppose the given solution's tour and cost
provided_tour = [0, 6, 9, 2, 12, 13, 1, 8, 18, 15, 19, 17, 11, 10, 16, 4, 7, 5, 14, 3, 0]
provided_cost = 381.11

# Verify the tour based on the requirements
result = verify_tour(provided_tour, provided_cost)
print(result)