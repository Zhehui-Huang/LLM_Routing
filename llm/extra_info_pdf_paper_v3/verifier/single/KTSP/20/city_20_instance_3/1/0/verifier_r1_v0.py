import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, reported_cost):
    # Check if tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 13 cities are visited (including depot, hence 14 positions in tour)
    if len(tour) != 14:
        return "FAIL"

    # Check for unique cities in the tour (except the depot city which appears twice)
    if len(set(tour)) != 13:
        return "FAIL"

    # Calculate the actual travel cost of the tour
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Check if the actual calculated cost matches the reported cost
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Coordinates of the cities
cities = [
    (30, 56),  # City 0 - Depot
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72)   # City 19
]

tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 0]
total_cost = 273.7443523737762

# Call the verification function
result = verify_solution(cities, tour, total_cost)
print(result)