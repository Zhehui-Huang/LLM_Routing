import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    # Check requirement: The robot must start and end its tour at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement: The robot must visit exactly 5 cities, including the depot city.
    if len(tour) != 6:  # Includes 5 cities + returning to the depot
        return "FAIL"

    # Check requirement: The travel cost is calculated as the Euclidean distance between the cities.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(*city_coordinates[city1], *city_coordinates[city2])

    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-9):
        return "FAIL"

    # Check requirement: The output must be in the form of a list of city indices and the total travel cost.
    if not isinstance(tour, list) or not isinstance(total_cost, float):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# City coordinates (indexed from 0 to 9)
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Solution to check
solution_tour = [0, 9, 5, 3, 8, 0]
solution_total_cost = 169.9409598467532

# Run the verification
result = verify_solution(solution_tour, solution_total_cost, cities)
print(result)