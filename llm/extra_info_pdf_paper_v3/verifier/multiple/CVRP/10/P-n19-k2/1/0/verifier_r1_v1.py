import math

# City coordinates and demands
cities = {
    0: {'coord': (30, 40), 'demand': 0},
    1: {'coord': (37, 52), 'demand': 19},
    2: {'coord': (49, 43), 'demand': 30},
    3: {'coord': (52, 64), 'demand': 16},
    4: {'coord': (31, 62), 'demand': 23},
    5: {'coord': (52, 33), 'demand': 11},
    6: {'coord': (42, 41), 'demand': 31},
    7: {'coord': (52, 41), 'demand': 15},
    8: {'coord': (57, 58), 'demand': 28},
    9: {'coord': (62, 42), 'demand': 14},
    10: {'coord': (42, 57), 'demand': 8},
    11: {'coord': (27, 68), 'demand': 7},
    12: {'coord': (43, 67), 'demand': 14},
    13: {'coord': (58, 27), 'demand': 19},
    14: {'coord': (37, 69), 'demand': 11},
    15: {'coord': (61, 33), 'demand': 26},
    16: {'coord': (62, 63), 'demand': 17},
    17: {'coord': (63, 69), 'demand': 6},
    18: {'coord': (45, 35), 'demand': 15}
}

# Robot tours and provided costs
robots = [
    {'tour': [0, 6, 18, 5, 7, 2, 9, 15, 16, 0], 'provided_cost': 129.15403265466222},
    {'tour': [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0], 'provided_cost': 172.59405136136587}
]

# Robot capacity
robot_capacity = 160

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Check demands are met and rule out capacity overflow
def check_demands_and_capacity():
    total_demand = sum(city['demand'] for city in cities.values())
    delivered = 0
    for robot in robots:
        for city_id in robot['tour'][1:-1]:  # Corrected: Excluding repeated city (depot)
            delivered += cities[city_id]['demand']
        load = sum(cities[city_id]['demand'] for city_id in robot['tour'][1:-1])
        if load > robot_capacity:
            return False
    return total_demand == delivered and delivered != 0  # Added demand not zero to confirm delivery

# Validate tour costs
def validate_costs():
    total_calculated_cost = 0
    for robot in robots:
        tour = robot['tour']
        tour_cost = sum(euclidean_distance(cities[tour[i]]['coord'], cities[tour[i + 1]]['coord']) for i in range(len(tour) - 1))
        total_calculated_cost += tour_cost
        if not math.isclose(tour_cost, robot['provided_cost'], abs_tol=1e-5):
            return False
    return math.isclose(total_calculated_cost, 301.7480840160281, abs_tol=1e-5)

# Check if all conditions are satisfied
def validate_solution():
    if len(cities) != 19:
        return "FAIL"
    if not check_demands_and_capacity():
        return "FAIL"
    if not validate_costs():
        return "FAIL"
    return "CORRECT"

# Execute the test
result = validate_solution()
print(result)