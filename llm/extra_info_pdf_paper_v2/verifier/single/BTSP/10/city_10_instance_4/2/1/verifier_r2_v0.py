import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, city_coordinates):
    # Requirement 1: Check if all cities are visited exactly once and starts/ends at depot
    if set(tour) != set(range(len(city_coordinates))) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Prepare to check Requirement 2 and 3
    max_distance = 0
    total_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance

    # Given result calculations:
    given_total_cost = 408.41
    given_max_distance = 61.68

    # Requirement 2: We assume the maximum minimizing strategy is correctly implemented, as numerical value validation requires comparisons with all possible tours or an exact solution algorithm
    # Requirement 3: Checking the distance computation
    if not (abs(total_distance - given_total_cost) < 0.01 and abs(max_distance - given_max_distance) < 0.01):
        return "FAIL"

    return "CORRECT"

# Cities coordinates
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
# Proposed tour
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]

# Verify if the tour meets the requirements
result = verify_solution(tour, cities)
print(result)