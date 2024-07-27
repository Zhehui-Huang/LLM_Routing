import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Defining cities and their demands
cities = {
    0: {'coords': (30, 40), 'demand': 0},
    1: {'coords': (37, 52), 'demand': 19},
    2: {'coords': (49, 43), 'demand': 30},
    3: {'coords': (52, 64), 'demand': 16},
    4: {'coords': (31, 62), 'demand': 23},
    5: {'coords': (52, 33), 'demand': 11},
    6: {'coords': (42, 41), 'demand': 31},
    7: {'coords': (52, 41), 'demand': 15},
    8: {'coords': (57, 58), 'demand': 28},
    9: {'coords': (62, 42), 'demand': 14},
    10: {'coords': (42, 57), 'demand': 8},
    11: {'coords': (27, 68), 'demand': 7},
    12: {'coords': (43, 67), 'demand': 14},
    13: {'coords': (58, 27), 'demand': 19},
    14: {'coords': (37, 69), 'demand': 11},
    15: {'coords': (61, 33), 'demand': 26},
    16: {'coords': (62, 63), 'demand': 17},
    17: {'coords': (63, 69), 'demand': 6},
    18: {'coords': (45, 35), 'demand': 15}
}

# Tours and demands claimed met
robot_tours = [
    {'tour': [0, 6, 18, 5, 7, 2, 9, 15, 16, 0], 'capacity': 160, 'reported_cost': 129.15},
    {'tour': [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0], 'capacity': 160, 'reported_cost': 172.59}
]

# Unit Test: Validate City Data Consistency
def test_city_data_validation():
    visited = set()
    for robot in robot_tours:
        for city in robot['tour']:
            if city in visited and city != 0:
                return "FAIL"  # City visited more than once
            visited.add(city)
    if len(visited) < len(cities):
        return "FAIL"  # Not all cities visited
    return "CORRECT"

# Unit Test: Validate Demand Met and Capacity
def test_demand_capacity():
    for robot in robot_tours:
        total_demand = 0
        for city in robot['tour']:
            total_demand += cities[city]['demand']
        if total_demand > robot['capacity']:
            return "FAIL"
    return "CORRECT"

# Unit Test: Validate Distances and Travel Cost
def test_travel_cost():
    for robot in robot_tours:
        tour = robot['tour']
        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += calculate_distance(cities[tour[i]]['coords'], cities[tour[i + 1]]['coords'])
        if not math.isclose(total_distance, robot['reported_cost'], rel_tol=1e-2):
            return "FAIL"
    return "CORRECT"

# Running the tests
def run_tests():
    if test_city_data_validation() == "FAIL":
        return "FAIL"
    if test_demand_capacity() == "FAIL":
        return "FAIL"
    if test_travel_cost() == "FAIL":
        return "FAIL"
    return "CORRECT"

# Print the result of the test
print(run_tests())