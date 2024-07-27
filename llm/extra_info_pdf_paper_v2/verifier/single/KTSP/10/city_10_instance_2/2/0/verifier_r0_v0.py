import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(city_coordinates, tour, reported_cost):
    # Verify return to start: The robot must start and end its tour at the depot city (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify exact number of cities including the depot city: The tour must include exactly 6 cities.
    if len(tour) != 7:  # 6 cities plus the return to the start city
        return "FAIL"

    # Calculate the total travel cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        total_calculated_cost += calculate_euclidean_distance(
            city_coordinates[city_a][0], city_coordinates[city_a][1],
            city_coordinates[city_b][0], city_coordinates[city_b][1])

    # Compare calculated cost with the reported cost
    if abs(total_calculated_cost - reported_cost) > 1e-5:
        return "FAIL"

    # Additional checks (if tour contains any city more than once besides the depot city)
    visited_cities = set(tour[1:-1])  # exclude the first and last element (depot city)
    if len(tour[1:-1]) != len(visited_cities):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# City coordinates given in the problem
city_coordinates = {
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

# Tour and reported total cost from the solution provided
tour = [0, 8, 5, 2, 1, 9, 0]
reported_cost = 183

# Running the verification
result = verify_tour(city_coordinates, tour, reported_cost)
print(result)  # Output: "CORRECT" or "FAIL"