import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost, max_distance_between_cities):
    # Define Cities' coordinates
    cities = [
        (50, 42),  # Depot City 0 - index 0
        (41, 1),   # City 1 - index 1
        (18, 46),  # City 2 - index 2
        (40, 98),  # City 3 - index 3
        (51, 69),  # City 4 - index 4
        (47, 39),  # City 5 - index 5
        (62, 26),  # City 6 - index 6
        (79, 31),  # City 7 - index 7
        (61, 90),  # City 8 - index 8
        (42, 49)   # City 9 - index 9
    ]

    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if tour has all cities and starts and ends at the depot
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"

    # Calculate the actual total travel cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        dist = euclidean_distance(*cities[city1], *cities[city2])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist

    # Check given travel cost and max distance against calculated values
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance_between_cities, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Data from the solution
tour = [0, 1, 5, 2, 9, 8, 3, 4, 6, 7, 0]
total_travel_cost = 326.26
max_distance_between_consecutive_cities = 45.19

# Verification
result = verify_solution(tour, total_travel_cost, max_distance_between_consecutive_cities)
print(result)