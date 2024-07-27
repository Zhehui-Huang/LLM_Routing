import math

# Constants
robot_capacity = 160

# Cities data (index: (x_coordinate, y_coordinate, demand))
cities = {
    0: (30, 40, 0),
    1: (37, 52, 7),
    2: (49, 49, 30),
    3: (52, 64, 16),
    4: (31, 62, 23),
    5: (52, 33, 11),
    6: (42, 41, 19),
    7: (52, 41, 15),
    8: (57, 58, 28),
    9: (62, 42, 8),
    10: (42, 57, 8),
    11: (27, 68, 7),
    12: (43, 67, 14),
    13: (58, 48, 6),
    14: (58, 27, 19),
    15: (37, 69, 11),
    16: (38, 46, 12),
    17: (61, 33, 26),
    18: (62, 63, 17),
    19: (63, 69, 6),
    20: (45, 35, 15)
}

# Tours from the solution
robot_tours = {
    0: [0, 6, 7, 5, 9, 2, 8, 3, 1, 4, 0],
    1: [0, 16, 10, 12, 15, 11, 18, 19, 13, 17, 14, 20, 0]
}

def calculate_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def verify_start_end_at_depot():
    for tour in robot_tours.values():
        if tour[0] != 0 or tour[-1] != 0:
            return False
    return True

def verify_demands_met():
    all_demands = {i: 0 for i in range(1, 21)}
    for tour in robot_tours.values():
        for city in tour[1:-1]:
            all_demands[city] += cities[city][2]
    return all(all_demands[city] == cities[city][2] for city in all_demands)

def verify_capacity_constraints():
    for tour in robot_tours.values():
        total_demand = sum(cities[city][2] for city in tour[1:-1])
        if total_demand > robot_capacity:
            return False
    return True

def verify_minimize_travel_cost():
    # This check cannot be truly 'verified' without comparing against all possible solutions,
    # We can only verify calculated distances match provided costs
    reported_costs = {
        0: 131.0058779883327,
        1: 164.23512950444
    }
    for robot_id, tour in robot_tours.items():
        actual_cost = sum(
            calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            for i in range(len(tour) - 1)
        )
        if not math.isclose(actual_cost, reported_costs[robot_id], rel_tol=1e-4):
            return False
    return True

def unit_tests():
    return (verify_start_end_at_depot() and
            verify_demands_met() and
            verify_capacity_constraints() and
            verify_minimize_travel_cost())

# Use the unit test function to verify the solution
if unit_tests():
    print("CORRECT")
else:
    print("FAIL")