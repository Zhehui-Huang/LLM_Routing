import math

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Provided solution information
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
total_travel_cost = 408.41
max_distance = 61.68

def calculate_euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two city coordinates."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost, max_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    if set(tour) != set(cities.keys()) or tour.count(0) != 2:
        return "FAIL"

    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        distance = calculate_euclidean_distance(tour[i - 1], tour[i])
        calculated_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)

    if not math.isclose(total_travel_cost, calculated_cost, abs_tol=1):
        return "FAIL"
    if not math.isclose(max_distance, calculated_max_distance, abs_tol=1):
        return "FAIL"

    return "CORRECT"

# Running the verification
result = verify_solution(tour, total_travel_cost, max_distance)
print(result)