import numpy as np

# Provided solution details
robot_tours = {
    0: [0, np.int64(8), np.int64(7), np.int64(5), np.int64(6), np.int64(4)],
    1: [1, np.int64(9), np.int64(12), np.int64(10), np.int64(11), np.int64(13)],
    2: [2, np.int64(15), np.int64(14), np.int64(16), np.int64(17)],
    3: [3, np.int64(19), np.int64(21), np.int64(20), np.int64(18)]
}
tour_costs = {
    0: 84.81,
    1: 104.77,
    2: 90.94,
    3: 105.53
}
overall_cost = 386.05

# Data to verify the solutions against
city_coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}


def calculate_euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def check_tour_costs_calculation_and_completeness():
    calculated_overall_cost = 0
    for robot, tour in robot_tours.items():
        expected_starting_city = robot  # depot indexes are the same as robot ids for simplicity
        if tour[0] != expected_starting_city:
            return "FAIL"  # Starting city mismatch

        tour_cost = 0
        last_city = tour[0]
        visited_cities = set(tour)

        for city in tour[1:]:
            tour_cost += calculate_euclidean_distance(last_city, city)
            last_city = city

        if not np.isclose(tour_cost, tour_costs[robot], rtol=1e-5):
            return "FAIL"  # Tour cost mismatch
        
        calculated_overall_cost += tour_cost

    if not np.isclose(calculated_overall_cost, overall_cost, rtol=1e-5):
        return "FAIL"  # Overall cost mismatch

    all_visited_cities = set(city for tour in robot_tours.values() for city in tour)
    if len(all_visited_cities) != len(city_coordinates):
        return "FAIL"  # Not all cities visited or some cities visited more than once

    return "CORRECT"


# Run the verification tests
result = check_tour_costs_calculation_and_completeness()
print(result)