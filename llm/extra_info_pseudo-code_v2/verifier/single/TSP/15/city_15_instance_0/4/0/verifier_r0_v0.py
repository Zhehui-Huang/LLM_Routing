import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(tour, total_cost):
    # Coordinates of the cities
    coordinates = [
        (9, 93),  # Depot city 0
        (8, 51),  # City 1
        (74, 99), # City 2
        (78, 50), # City 3
        (21, 23), # City 4
        (88, 59), # City 5
        (79, 77), # City 6
        (63, 23), # City 7
        (19, 76), # City 8
        (21, 38), # City 9
        (19, 65), # City 10
        (11, 40), # City 11
        (3, 21),  # City 12
        (60, 55), # City 13
        (4, 39)   # City 14
    ]

    # [Requirement 5]: Tour must start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 6]: Total correct number of cities
    if len(tour) != 16:
        return "FAIL"

    # [Requirement 2]: Each city must be visited exactly once (except depot twice, starting and ending)
    unique_cities = set(tour)
    if len(unique_cities) != 15:
        return "FAIL"

    # [Requirement 3]: Check the total travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Input from the problem, expected results
tour_input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
total_cost_input = 748.0763256382368

# Check the test case
print(verify_solution(tour_input, total_cost_input))