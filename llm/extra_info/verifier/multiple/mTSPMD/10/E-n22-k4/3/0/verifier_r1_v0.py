import math

# Test data
robot_tours = {
    0: [0, 14, 16, 13, 11, 8, 6, 10, 4, 19, 21, 0],
    1: [1, 5, 9, 15, 18, 1],
    2: [2, 7, 12, 17, 20, 2],
    3: [3, 3]
}
coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Requirement validation functions
def all_cities_visited_once(robot_tours):
    all_cities = set(range(22))
    visited_cities = set()
    for tour in robot_tours.values():
        visited_cities.update(tour)
    # Remove depot cities as they may appear twice (start and end)
    visited_cities = {city for city in visited_cities if city not in (0, 1, 2, 3) or tour.count(city) == 1}
    return visited_cities == all_cities

def correct_start_end_depot(robot_tours):
    correct = True
    for robot_id, tour in robot_tours.items():
        if tour[0] != robot_id or tour[-1] != robot_store_id:
            correct = False
    return correct

def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return cost

def verify_costs(robot_tours, coordinates):
    calculated_costs = {
        0: 219.27651548919482,
        1: 147.00683322940296,
        2: 157.65098083920589,
        3: 0.0
    }
    for robot_id, tour in robot_tours.items():
        if not math.isclose(calculate_tour_cost(tour, coordinates), calculated_costs[robot_id], rel_tol=1e-9):
            return False
    return True

# Verification of requirements
if (all_cities_visited_once(robot_tours)
    and correct_start_end_depot(robot_tours)
    and verify_costs(robot_tours, coordinates)):
    print("CORRECT")
else:
    print("FAIL")