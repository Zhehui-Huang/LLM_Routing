import math

# Provided tours
robot_tours = {
    0: [0, 0, 21, 0],
    1: [1, 1, 10, 16, 1],
    2: [2, 2, 13, 2],
    3: [3, 3, 8, 12, 18, 19, 3],
    4: [4, 4, 11, 15, 4],
    5: [5, 5, 14, 17, 22, 5],
    6: [6, 6, 20, 6],
    7: [7, 7, 9, 7]
}

# Provided total travel costs expected
expected_costs = {
    0: 4.47213595499958,
    1: 24.85853025288332,
    2: 18.110770276274835,
    3: 62.03586299584028,
    4: 26.480522629341756,
    5: 27.25346379366317,
    6: 13.416407864998739,
    7: 20.09975124224178
}

# City locations
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities given their coordinates."""
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def check_start_end_tour():
    """ Each robot's tour must start and end at its assigned depot city. """
    for robot, tour in robot_tours.items():
        if tour[0] != tour[-1] or tour[0] != robot:
            return False
    return True

def check_visitation_requirement():
    """ Each city must be visited exactly once by any of the robots. """
    all_cities_visited = sorted([city for tour in robot_tours.values() for city in tour if city not in robot_tours])
    return all_cities_visited == sorted(cities.keys())

def check_minimized_costs():
    """ Check if the provided travel costs correspond to those calculated from the city coordinates. """
    for robot, tour in robot_tours.items():
        calculated_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if not math.isclose(calculated_cost, expected_costs[robot], rel_tol=1e-5):
            return False
    return True

# Running the checks
if check_start_end_tour() and check_visitation_requirement() and check_minimized_costs():
    print("CORRECT")
else:
    print("FAIL")