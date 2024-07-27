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
    ([0, 4, 3, 2], 58.59568496168186),
    ([0, 15, 4, 3], 46.12595586786377),
    ([0, 2, 22, 7], 28.093301984259718),
    ([0, 14, 17, 18], 72.94640652465631),
    ([0, 19, 20, 6], 80.17897205584205),
    ([0, 21, 0, 16], 21.455612434792677),
    ([0, 1, 5, 5], 48.41487374764082),
    ([0, 6, 1], 24.166091947189145)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(solutions):
    all_visited_cities = set()
    total_reported_cost = 0.0

    for tour, reported_cost in solutions:
        last_city_index = tour[0]
        calculated_cost = 0.0

        for city_index in tour[1:]:
            all_visited_cities.add(city_index)
            calculated_cost += euclidean_distance(cities[last_city_index], cities[city_index])
            last_city_index = city_index

        if not math.isclose(calculated_cost, reported_cost, abs_tol=1e-4):
            return "FAIL"
        total_reported_cost += reported_cost

    overall_reported_total_cost = 380.9718995259766  # Sum of the reported individual tour costs above

    if len(all_visited_cities) != len(set(range(len(cities))) - {0}):
        return "FAIL"

    if not math.isclose(total_reported_cost, overall_reported_total_tcost, abs_tol=1e-4):
        return "FAIL"

    return "CORRECT"

print(verify_solution(solutions))