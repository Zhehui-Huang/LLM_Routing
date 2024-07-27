import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_cost, max_distance):
    # City coordinates
    coordinates = [
        (79, 15),  # city 0 - depot
        (79, 55),  # city 1
        (4, 80),   # city 2
        (65, 26),  # city 3
        (92, 9),   # city 4
        (83, 61),  # city 5
        (22, 21),  # city 6
        (97, 70),  # city 7
        (20, 99),  # city 8
        (66, 62)   # city 9
    ]

    # Check start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once
    if sorted(tour) != sorted(list(range(len(coordinates)))):
        return "FAIL"

    # Calculate the travel cost and check the maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    number_of_cities = len(tour)

    for i in range(number_of_cities - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])
        calculated_total_cost += distance
        if distance > calculated_max_home_distance:
            calculated_max_home_distance = distance

    # Check total travel cost and max distance
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=1e-2):
        return "FAIL"
    if not math.isclose(calculated_max_home_distance, max_distance, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given solution information
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
total_travel_cost = 408.41
maximum_distance = 61.68

# Validate the solution
solution_status = verify_solution(tour, total_travel_cost, maximum_distance)
print(solution_status)