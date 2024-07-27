import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_tour_and_cost(tour, reported_cost):
    # City coordinates as provided in problem
    city_coordinates = [
        (9, 93),   # Depot city 0
        (8, 51),   # City 1
        (74, 99),  # City 2
        (78, 50),  # City 3
        (21, 23),  # City 4
        (88, 59),  # City 5
        (79, 77),  # City 6
        (63, 23),  # City 7
        (19, 76),  # City 8
        (21, 38),  # City 9
        (19, 65),  # City 10
        (11, 40),  # City 11
        (3, 21),   # City 12
        (60, 55),  # City 13
        (4, 39)    # City 14
    ]

    # Check tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities visited exactly once excluding depot city
    visited = set(tour)
    if visited != set(range(len(city_coordinates))):
        return "FAIL"

    # Calculate the total travel cost from the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i+1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Check if the calculated cost matches the reported cost
    if not math.isclose(total_cost, reported_cost, abs_tol=1e-3):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
reported_cost = 373.97393412233544

# Test the tour
result = test_tour_and_cost(tour, reported_cost)
print(result)