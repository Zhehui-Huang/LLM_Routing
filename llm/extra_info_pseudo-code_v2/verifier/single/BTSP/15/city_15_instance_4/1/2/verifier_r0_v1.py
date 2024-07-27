import math

# Given solution details
tour = [0, 1, 5, 9, 2, 0]
total_travel_cost = 100.94
max_distance_between_cities = 47.07

# City coordinates (id: (x, y))
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 5: (54, 46), 9: (70, 44)
}

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_requirements(tour, total_travel_cost, max_distance):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit each city exactly once, plus the return to the depot
    if len(set(tour)) != len(tour) - 1:
        return "FAIL"

    # Requirement 5: Tour should start and end at depot city 0
    if not (tour[0] == tour[-1] == 0):
        return "FAIL"

    # Calculate actual travel cost and distances
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        distance = calculate_euclidean_distance(*cities[city1], *cities[city2])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Requirement 6: Verify calculated and provided total travel costs
    if not math.isclose(calculated_total_cost, total_travel_cost, abs_tol=0.01):
        return "FAIL"

    # Requirement 7: Verify calculated and provided max distance
    if not math.isclose(calculated_max_distance, max_distance, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

result = verify_requirements(tour, total_travel_cost, max_distance_between_cities)
print(result)