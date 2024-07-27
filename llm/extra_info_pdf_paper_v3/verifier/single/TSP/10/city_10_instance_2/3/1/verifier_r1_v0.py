import numpy as np

def calculate_euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_tsp_solution():
    # Coordinates of cities including the depot
    coordinates = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }

    # Provided tour and total travel cost
    tour = [np.int64(8), 0, 0]
    provided_total_cost = 48.54894437575342

    # Check if there are 10 cities
    if len(coordinates) != 10:
        return "FAIL"

    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check that all cities, except the depot city, are visited exactly once
    unique_cities = set(tour)
    if unique_cities != set(range(10)) or tour.count(0) != 2:
        return "FAIL"

    # Calculate the total travel cost from the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])

    # Compare the calculated total cost with the provided total cost
    if not np.isclose(total_cost, provided_total_cost):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Output the test result
print(test_tsp_solution())