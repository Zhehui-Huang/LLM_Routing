import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_tour_solution():
    # Input coordinates for each city
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }

    # Provided solution details
    tour = [0, 8, 3, 9, 5, 6, 7, 1, 2, 4, 0]
    reported_total_cost = 345.92
    reported_max_dist = 68.26

    # Validate start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: The tour must start and end at depot city 0."

    # Validate every city is visited exactly once
    if sorted(tour[:-1]) != sorted(list(cities.keys())):
        return "FAIL: Each city must be visited exactly once, excluding the depot which is visited twice as start/end."

    # Compute total travel cost and max distance
    total_distance_calc = 0
    max_distance_calc = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        distance = calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
        total_distance_calc += distance
        if distance > max_distance_calc:
            max_distance_calc = distance

    # Compare calculated results with provided results
    if not (math.isclose(total_distance_calc, reported_total_cost, rel_tol=1e-2) and 
            math.isolve(max_distance_calc, reported_max_dist, rel_tol=1e-2)):
        return "FAIL: Calculated results do not match the reported results."

    # Passed all checks
    return "CORRECT"

# Run the test
test_output = test_tour_solution()
print(test_output)