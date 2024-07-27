import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, reported_cost):
    # Coordinates for each city
    coordinates = [
        (8, 11),  # City 0
        (40, 6),  # City 1
        (95, 33), # City 2
        (80, 60), # City 3
        (25, 18), # City 4
        (67, 23), # City 5
        (97, 32), # City 6
        (25, 71), # City 7
        (61, 16), # City 8
        (27, 91), # City 9
        (91, 46), # City 10
        (40, 87), # City 11
        (20, 97), # City 12
        (61, 25), # City 13
        (5, 59),  # City 14
        (62, 88), # City 15
        (13, 43), # City 16
        (61, 28), # City 17
        (60, 63), # City 18
        (93, 15)  # City 19
    ]

    # Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 4 cities are visited
    if len(tour) != 5:  # including the depot city twice
        return "FAIL"

    # Calculate the travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])

    # Check if calculated cost matches the reported cost
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Provided solution details
tour = [0, 1, 9, 4, 0]
reported_cost = 110.09

# Validate the solution
result = verify_solution(tour, reported_cost)
print(result)