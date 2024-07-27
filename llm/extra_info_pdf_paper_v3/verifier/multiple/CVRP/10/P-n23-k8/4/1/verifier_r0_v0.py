import math

# Given city coordinates
coordinates = {
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
    21: (32, 39),
    22: (56, 37)
}

# Given demands by city, excluding depot city (city 0)
demands = {
    1: 7,
    2: 30,
    3: 16,
    4: 23,
    5: 11,
    6: 19,
    7: 15,
    8: 28,
    9: 8,
    10: 8,
    11: 7,
    12: 14,
    13: 6,
    14: 19,
    15: 11,
    16: 12,
    17: 26,
    18: 17,
    19: 6,
    20: 15,
    21: 5,
    22: 10
}

# Robot tour and travel cost data – this is the setup that needs validation
robot_tours = {
    0: ([0, 21, 16, 1, 10, 13, 0], 72.08744208476426),
    1: ([0, 6, 20, 19, 0], 101.15233190761194),
    2: ([0, 2, 22, 0], 61.088744687683246),
    3: ([0, 4, 11, 9, 0], 104.8967158934193),
    4: ([0, 7, 5, 12, 0], 95.16037446322657),
    5: ([0, 15, 3, 0], 78.20189727339391),
    6: ([0, 14, 18, 0], 106.500359623892),
    7: ([0, 17, 0], 63.56099432828282)
}
capacity = 40

# Check if demands are fully met and capacity constraints are maintained
def check_demands_and_capacity():
    total_delivered = {key: 0 for key in demands.keys()}
    for tour, _ in robot_tours.values():
        current_capacity = 0
        for city in tour:
            if city != 0:
                total_delivered[city] += demands[city]
                current_capacity += demands[city]
                if current_capacity > capacity:
                    return False
    return total_delivered == demands

# Check if the routes start and end at depot city
def check_route_start_end():
    for tour, _ in robot_tours.values():
        if tour[0] != 0 or tour[-1] != 0:
            return False
    return True

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Check if the travel costs are correctly calculated
def check_travel_costs():
    for tour, expected_cost in robot_tours.values():
        total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
            return False
    return True

# Main check to validate
def validate_solution():
    if all([check_demands_and_capacity(), check_route_start_end(), check_travel_costs()]):
        return "CORRECT"
    else:
        return "FAIL"

# Output the result of the validation
print(validate_solution())