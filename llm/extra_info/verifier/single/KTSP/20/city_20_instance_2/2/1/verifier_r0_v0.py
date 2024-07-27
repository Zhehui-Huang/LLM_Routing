import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_total_cost(proposed_tour, proposed_cost, cities):
    if len(proposed_tour) != 11:
        return "FAIL"  # Tour must include exactly 10 cities plus the return to the depot

    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"  # Tour must start and end at depot city 0

    unique_cities = set(proposed_tour)
    if len(unique_cities) != 11:
        return "FAIL"  # There must be 10 different cities visited exactly once, including the depot

    # Calculating the total cost from the tour
    total_cost = 0
    for i in range(len(proposed_tour) - 1):
        city1 = proposed_tour[i]
        city2 = proposed_tour[i + 1]
        total_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])

    # Check the total travel cost correctness
    if not math.isclose(total_cost, proposed_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Coordinates of the cities
cities = {
    0: (3, 26),
    6: (2, 65),
    8: (3, 92),
    10: (30, 88),
    11: (30, 53),
    13: (52, 49),
    14: (18, 49),
    16: (28, 49),
    18: (51, 58),
    19: (30, 48)
}

# Proposed tour and cost
proposed_tour = [0, 6, 8, 10, 11, 13, 14, 16, 18, 19, 0]
proposed_cost = 277.47

# Verification
result = verify_tour_and_total_cost(proposed_tour, proposed_cost, cities)
print(result)