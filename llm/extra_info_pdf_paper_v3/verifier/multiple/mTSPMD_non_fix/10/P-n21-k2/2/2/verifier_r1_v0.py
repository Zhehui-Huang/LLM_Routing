import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def unit_tests():
    # Coordinates of the cities
    cities = {
        0: (30, 40),
        1: (37, 52),
        2: (49, 49),
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
        13: (58, 48),
        14: (58, 27),
        15: (37, 69),
        16: (38, 46),
        17: (61, 33),
        18: (62, 63),
        19: (63, 69),
        20: (45, 35)
    }

    # Solution provided
    robot_0_tour = [0, 4, 15, 19, 3, 2, 9, 5, 20, 6, 0]
    robot_0_cost = 138.87
    robot_1_tour = [1, 11, 10, 12, 8, 18, 13, 17, 14, 7, 16, 1]
    robot_1_cost = 144.94
    overall_cost = 283.81

    # Total number of distinct cities visited
    all_cities_visited = set(robot_0_tour + robot_1_tour)
    if len(all_cities_visited) != 21:
        return "FAIL"

    # Verify starting points
    if robot_0_tour[0] != 0 or robot_1_tour[0] != 1:
        return "FAIL"

    # Verify cost calculation
    calculated_costs = []
    for tour in [robot_0_tour, robot_1_tour]:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_costs.append(round(tour_cost, 2))
    
    if not (calculated_costs[0] == robot_0_cost and calculated_costs[1] == robot_1_cost):
        return "FAIL"
    
    # Verify overall cost
    if round(sum(calculated_costs), 2) != overall_cost:
        return "FAIL"

    return "CORRECT"

print(unit_tests())