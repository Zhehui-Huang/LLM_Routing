import math

# Define the test tour and cost provided
test_tour = [0, 6, 11, 14, 1, 8, 12, 4, 3, 5, 10, 9, 13, 7, 2, 0]
test_total_cost = 311.88

# Define the city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_requirements(tour, total_cost):
    # [Requirement 1] & [Requirement 3]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or any(city not in tour for city in cities):
        return "FAIL"

    # [Requirement 6]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the travel cost
    calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    # [Requirement 7]
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    # [Requirement 4] is considered in calculating distances and [Requirement 5]
    # Would require solving or comparing to an optimal or known solution

    return "CORRECT"

# Check the given solution with our constraints
result = check_requirements(test_tour, test_total_cost)
print(result)