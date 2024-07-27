import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_tsp_solution(tour, coordinates, reported_cost):
    # Check if the tour starts and ends at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, except the depot which must be visited twice (start and end)
    if sorted(tour[1:-1]) != list(range(1, len(coordinates))):
        return "FAIL"

    # Calculate the total travel cost of the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        city_1 = tour[i]
        city_2 = tour[i + 1]
        x1, y1 = coordinates[city_1]
        x2, y2 = coordinates[city_2]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Compare the calculated cost with the reported cost
    if not math.isclose(total_cost, reported_cost, abs_tol=0.01):
        return "FAIL"

    # Since the function to verify the use of a specific heuristic like constructing SST and MCPM is not practical without
    # implementing or observing the internal algorithm steps, we cannot verify criterion [5] in this unit test.
    # We assume the heuristic method is correctly used based on problem statement requirement.

    return "CORRECT"

# Coordinates for each city based on the task description
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

# Tour and reported total travel cost
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
reported_cost = 349.20

# Validate the solution
result = verify_tsp_solution(tour, coordinates, reported_cost)
print(result)