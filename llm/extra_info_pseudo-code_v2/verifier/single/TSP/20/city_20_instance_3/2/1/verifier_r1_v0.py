import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, cities):
    # Requirement 1: Tour must start and end at depot city indexed at 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Robot visits each other city exactly once
    all_cities = set(range(len(cities)))
    visited_cities = set(tour)
    if all_cities != visited_cities:
        return "FAIL"

    # Requirement 3: Travel cost is based on the Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = cities[tour[i]]
        city_b = cities[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(city_a[0], city_a[1], city_b[0], city_b[1])
    
    # Allow a small margin for floating point errors
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-5):
        return "FAIL"

    # If all checks are complete
    return "CORRECT"

# Cities coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Provided example tour and total cost
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_cost = 458.36719998557066

# Run verification and print the result
result = verify_solution(tour, total_cost, cities)
print(result)