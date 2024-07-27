import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, reported_cost, cities):
    if len(tour) != 8:  # Tour should visit exactly 7 cities + 1 repetition of depot city
        return "FAIL"

    if tour[0] != 0 or tour[-1] != 0:  # Start and end at depot city 0
        return "FAIL"

    unique_cities = set(tour)
    if len(unique_cities) != 8:  # Including depot revisited i.e., exactly 7 unique cities visited
        return "FAIL"

    # Calculate the actual travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        city_a_index = tour[i]
        city_b_index = tour[i + 1]
        city_a = cities[city_a_index]
        city_b = cities[city_b_index]
        actual_cost += calculate_euclidean_distance(city_a[0], city_a[1], city_b[0], city_b[1])

    # Check if the calculated distance matches the reported distance within a small tolerance
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates (with index representing city number)
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Provided solution
tour = [0, 3, 14, 17, 9, 6, 0]
reported_cost = 175.66

# Conducting the tests
result = verify_solution(tour, reported_cost, cities)
print(result)