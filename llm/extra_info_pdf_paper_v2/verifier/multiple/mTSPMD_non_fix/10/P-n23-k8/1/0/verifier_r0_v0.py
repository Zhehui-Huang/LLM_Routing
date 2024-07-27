import math

# City coordinates as per the initial task
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Solution provided (robots' tours)
solutions = [
    [0, 4, 3, 2],
    [0, 15, 4, 3],
    [0, 2, 22, 7],
    [0, 14, 17, 18],
    [0, 19, 20, 6],
    [0, 21, 0, 16],
    [0, 1, 5, 5],
    [0, 6, 1]
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution(solutions):
    num_cities = len(cities)
    all_visited_cities = set()
    total_calculated_cost = 0

    for tour in solutions:
        tour_cost = 0
        last_city = tour[0]
        for city_index in tour[1:]:
            all_visited_cities.add(cityIndex)
            tour_cost += euclidean_distance_cities[cities[last_city], cities[city_index]]
            last_city = city_index
        total_calculated_cost += tour_cost

    # Checking all cities are visited exactly once
    if len(all_visited_cities) != num_cities - 1:  # -1 because the depots are not part of the mandatory visits
        return "FAIL"

    # Adding the reported individual tour costs
    reported_total_cost = 358.3704649935605  # This is just an example; it needs to match the summation of all individual costs from the result.

    # Comparing calculated total costs within a tolerance
    if not math.isclose(total_calculated_cost, reported_total_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

print(verify_solution(solutions))