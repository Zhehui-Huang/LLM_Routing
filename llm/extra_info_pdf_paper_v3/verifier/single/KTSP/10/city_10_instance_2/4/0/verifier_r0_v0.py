import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, cost, cities_coordinates):
    # Verify the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify the tour visits exactly 6 cities
    if len(tour) != 7:  # Includes returning to the depot
        return "FAIL"

    # Verify no city other than depot is visited more than once
    if len(set(tour[1:-1])) != len(tour[1:-1]):
        return "FAIL"

    # Calculate the travel cost from the tour
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = cities_coordinates[tour[i]]
        city_to = cities_coordinates[tour[i + 1]]
        total_calculated_cost += euclidean_distance(city_from, city_to)

    # Check if calculated cost is approximately equal to provided cost
    if not math.isclose(total_calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Define the coordinates of the cities
cities_coordinates = {
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

# Given solution
tour = [0, 8, 5, 2, 1, 9, 0]
total_travel_cost = 183.85354044487238

# Verify the solution
result = verify_solution(tour, total_travel_cost, cities_coordinates)
print(result)