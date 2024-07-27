from math import sqrt

# City data including coordinates and demands
cities = {
    0: {'coord': (145, 215), 'demand': 0},
    1: {'coord': (151, 264), 'demand': 1100},
    2: {'coord': (159, 261), 'demand': 700},
    3: {'coord': (130, 254), 'demand': 800},
    4: {'coord': (128, 252), 'demand': 1400},
    5: {'coord': (163, 247), 'demand': 2100},
    6: {'coord': (146, 246), 'demand': 400},
    7: {'coord': (161, 242), 'demand': 800},
    8: {'coord': (142, 239), 'demand': 100},
    9: {'coord': (163, 236), 'demand': 500},
    10: {'coord': (148, 232), 'demand': 600},
    11: {'coord': (128, 231), 'demand': 1200},
    12: {'coord': (156, 217), 'demand': 1300},
    13: {'coord': (129, 214), 'demand': 1300},
    14: {'coord': (146, 208), 'demand': 300},
    15: {'coord': (164, 208), 'demand': 900},
    16: {'coord': (141, 206), 'demand': 2100},
    17: {'coord': (147, 193), 'demand': 1000},
    18: {'coord': (164, 193), 'demand': 900},
    19: {'coord': (129, 189), 'demand': 2500},
    20: {'coord': (155, 185), 'demand': 1800},
    21: {'coord': (139, 182), 'demand': 700},
}

robot_capacity = 6000
calculated_costs = []
demands_fulfilled = {i: 0 for i in range(1, 22)}  # Exclude depot

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]['coord']
    x2, y2 = cities[city2]['coord']
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

valid = True

# Robot tours and their reported travel costs
tours = {
    0: {'tour': [0, 1, 2, 3, 4, 0], 'reported_cost': 131.29},
    1: {'tour': [0, 5, 6, 7, 8, 9, 10, 11, 0], 'reported_cost': 168.61},
    2: {'tour': [0, 12, 13, 14, 15, 16, 0], 'reported_cost': 107.31},
    3: {'tour': [0, 17, 18, 19, 0], 'reported_cost': 104.85},
    4: {'tour': [0, 20, 21, 0], 'reported_cost': 81.44}
}

# Check the correctness of the tests
for robot, data in tours.items():
    tour = data['tour']
    capacity_used = 0
    cost_sum = 0
    previous_city = tour[0]

    for city in tour[1:]:
        if city != 0:  # Skip depot when calculating demands and capacity
            capacity_used += cities[city]['demand']
            demands_fulfilled[city] += cities[city]['demand']
        cost_sum += calculate_distance(previous_city, city)
        previous_city = city

    # Return to depot cost
    cost_sum += calculate_distance(previous_city, 0)
    calculated_costs.append(cost_sum)

    if capacity_used > robot_capacity:
        print(f"FAIL: Robot {robot} exceeds capacity.")
        valid = False

if valid and all(demands_fulfilled[c] == cities[c]['demand'] for c in demands_fulfilled):
    if all(round(data['reported_cost'], 2) == round(calculated_costs[i], 2) for i, data in enumerate(tours.values())):
        print("CORRECT")
    else:
        print("FAIL: Incorrect travel cost calculations.")
else:
    print("FAIL: Demands not properly fulfilled or capacity exceeded.")