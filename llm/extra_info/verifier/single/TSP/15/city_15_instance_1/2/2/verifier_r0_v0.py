import math

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Provided Tour
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
provided_total_cost = 443

def calculate_euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour():
    # Ensure start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once
    visited_cities = set(tour)
    if visited_cities != set(cities.keys()):
        return "FAIL"

    # Calculate the actual total travel cost
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        calculated_total_cost += calculate_euclidean_distance(tour[i], tour[i+1])

    # Compare provided total cost with calculated cost
    if int(calculated_total_cost) != provided_total cost:
        return "FAIL"

    return "CORRECT"

# Run the test
test_result = verify_tour()
print(test_result)