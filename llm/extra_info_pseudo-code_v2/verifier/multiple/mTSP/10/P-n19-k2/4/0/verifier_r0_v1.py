import math

# Definition of city coordinates
city_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

robots_tours = [
    [0, 6, 18, 7, 15, 8, 16, 12, 10, 11, 0],
    [0, 1, 4, 14, 3, 17, 9, 2, 5, 13, 0]
]
correct_tours_costs = [148.62767754005085, 152.52152945750305]
correct_overall_total_cost = 301.1492069975539

def test_solution(robots_tours, correct_tours_costs, correct_overall_total_cost, city_coordinates):
    computed_costs = []
    all_cities_visited = set()
    for tour in robots_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        cost = calculate_tour_cost(tour, city_coordinates)
        computed_costs.append(cost)
        all_cities_visited.update(tour[1:-1])

    if len(all_cities_visited) != 18 or all_cities_visited != set(range(1, 19)):
        return "FAIL"

    if any(not math.isclose(computed_costs[i], correct_tours_costs[i], abs_tol=0.01) for i in range(len(robots_tours))):
        return "FAIL"

    overall_computed_cost = sum(computed_costs)
    if not math.isclose(overall_computed_cost, correct_overall_total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Run the tests
result = test_solution(robots_tours, correct_tours_costs, correct_overall_total_cost, city_coordinates)
print(result)