import math

def calculate_distance(city1, city2):
    """ Helper function to calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost, max_distance):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
        (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
        (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
        (64, 72), (14, 89)
    ]

    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit each city exactly once
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL"
    if len(tour) != 21:  # 20 cities + 1 return to depot
        return "FAIL"

    # Requirement 3: Validate distances
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)

    # Check if the given cost and max distance match
    if not math.isclose(calculated_total_cost, cost, rel_tol=1e-2):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Example solution
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
total_travel_cost = 410.04
maximum_distance_between_cities = 89.01

# Validate the solution
result = verify_solution(tour, total_travel_cost, maximum_distance_between_cities)
print(result)