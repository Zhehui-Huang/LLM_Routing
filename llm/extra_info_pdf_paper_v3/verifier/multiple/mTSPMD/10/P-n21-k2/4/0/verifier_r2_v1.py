import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_tours():
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
        (62, 63), (63, 69), (45, 35)
    ]

    robot_0_tour = [0, 17, 6, 3, 0]
    robot_1_tour = [1, 10, 1]
    provided_robot_0_cost = 110.03
    provided_robot_1_cost = 14.14
    provided_total_cost = 124.18
    
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0:
        return "FAIL"
    if robot_1_tour[0] != 1 or robot_1_tour[-1] != 1:
        return "FAIL"
    
    def calculate_tour_cost(tour):
        cost = 0.0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        return round(cost, 2)

    calc_robot_0_cost = calculate_tour_cost(robot_0_tour)
    calc_robot_1_cost = calculate_tour_cost(robot_1_tour)
    calc_total_cost = round(calc_robot_0_cost + calc_robot_1_cost, 2)

    if calc_robot_0_cost != provided_robot_0_cost or calc_robot_1_cost != provided_robot_1_cost:
        return "FAIL"
    if calc_total_cost != provided_total_cost:
        return "FAIL"

    all_visited_cities = robot_0_tour[:-1] + robot_1_tour[:-1]
    unique_visited_cities = set(all_visited_cities)
    if len(unique_visited_cities) != len(coordinates) - 1:
        return "FAIL"

    from collections import Counter
    city_counts = Counter(all_visited_cities)
    if any(count > 1 for city, count in city_counts.items() if city not in [0, 1]):
        return "FAIL"

    return "CORRECT"

print(verify_tours())