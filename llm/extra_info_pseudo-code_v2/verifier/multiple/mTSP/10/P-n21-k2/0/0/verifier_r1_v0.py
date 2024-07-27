import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

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
    20: (45, 35),
}

# The solution provided (to be tested)
robot_0_tour = [0, 1, 11, 15, 3, 19, 13, 9, 17, 5, 7, 0]
robot_1_tour = [0, 16, 10, 4, 12, 18, 8, 2, 6, 14, 20, 0]
robot_0_cost = 147.58095252865388
robot_1_cost = 148.28305937543914
overall_cost = 295.864011904093

# Test cases
def test_all_cities_visited_once(tours):
    all_cities = set(range(1, 21))  # excluding depot
    visited_cities = set()
    for tour in tours:
        visited_cities.update(tour[1:-1])  # excluding the depot city at start and end
    return visited_cities == all_cities

def test_starts_ends_depot(tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

def test_calculate_costs(tours):
    calculated_costs = []
    for tour in tours:
        cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        calculated_costs.append(cost)
    return calculated_costs

# Start tests
tours = [robot_0_tour, robot_1_tour]
actual_costs = test_calculate_costs(tours)
calculated_robot_0_cost, calculated_robot_1_cost = actual_costs
correct_tour_visit = test_all_cities_visited_once(tours)
correct_tour_start_end = test_starts_ends_depot(tours)
calculated_overall_cost = sum(actual_costs)

# Results
if (correct_tour_visit and correct_tour_start_end and
    abs(calculated_robot_0_cost - robot_0_cost) < 1e-5 and 
    abs(calculated_robot_1_cost - robot_1_cost) < 1e-5 and
    abs(calculated_overall_cost - overall_cost) < 1e-5):
    print("CORRECT")
else:
    print("FAIL")