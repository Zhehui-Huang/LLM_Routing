import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

robot_tours = [
    ([8, 0, 0], 32.449961479175904),
    ([0, 1, 9], 40.81826802512232),
    ([10, 2, 0], 31.65394185436329),
    ([0, 11, 3], 53.47823348300177),
    ([12, 4, 0], 35.02271554554524),
    ([13, 5, 0], 39.2422871826339),
    ([0, 6, 14], 33.30188620426159),
    ([15, 0, 7], 51.85558332589784)
]

def verify_tours(robot_tours, cities_coordinates):
    all_visited_cities = set()
    total_calculated_cost = 0.0
    depots = [0]

    for tour, reported_cost in robot_tours:
        # Check starting from depot 0 (Requirement 2)
        if tour[0] != depots[0]:
            return "FAIL"

        # Check if all cities are visited at least once (Requirement 1)
        all_visited_cities.update(tour)

        # Calculate the actual cost (Requirement 3 and 5)
        actual_cost = 0.0
        for i in range(len(tour) - 1):
            actual_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
        if not math.isclose(actual_cost, reported_cost, rel_tol=1e-5):
            return "FAIL"

        total_calculated_cost += actual_cost

    # Check all cities are visited exactly once (Requirement 1)
    if all_visited_cities != set(cities_coordinates.keys()):
        return "FAIL"

    # Check total cost consistency (Requirement 3 and 5)
    reported_total_cost = sum(cost for _, cost in robot_tours)
    if not math.isclose(total_calculated_cost, reported_total_cost, rel_tol=1e-5):
        return "FAIL"
      
    return "CORRECT"

# Execute test
test_result = verify_tours(robot_tours, cities_coordinates)
print(test_result)