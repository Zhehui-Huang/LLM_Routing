import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour_requirements(tour, cities):
    visited = set(tour)
    if len(visited) != len(cities) or not all(city in visited for city in range(len(cities))):
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    max_distance = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    is_total_cost_correct = math.isclose(total_cost, 544.3, abs_tol=0.1)
    is_max_distance_correct = math.isclose(max_distance, 42.3, abs_tol=0.1)

    if not is_total_cost_correct or not is_max_distance_correct:
        return "FAIL"

    return "CORRECT"

cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
    4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
    8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}
solution_tour = [0, 5, 0, 4, 10, 4, 0, 9, 3, 7, 1, 6, 13, 2, 11, 12, 11, 2, 8, 14, 8, 2, 13, 6, 1, 7, 3, 9, 0]

result = check_tour_requirements(solution_tour, cities)
print(result)