import math

# City coordinates and demands
cities = {
    0: {'coords': (30, 40), 'demand': 0},
    1: {'coords': (37, 52), 'demand': 7},
    2: {'coords': (49, 49), 'demand': 30},
    3: {'coords': (52, 64), 'demand': 16},
    4: {'coords': (31, 62), 'demand': 23},
    5: {'coords': (52, 33), 'demand': 11},
    6: {'coords': (42, 41), 'demand': 19},
    7: {'coords': (52, 41), 'demand': 15},
    8: {'coords': (57, 58), 'demand': 28},
    9: {'coords': (62, 42), 'demand': 8},
    10: {'coords': (42, 57), 'demand': 8},
    11: {'coords': (27, 68), 'demand': 7},
    12: {'coords': (43, 67), 'demand': 14},
    13: {'coords': (58, 48), 'demand': 6},
    14: {'coords': (58, 27), 'demand': 19},
    15: {'coords': (37, 78), 'demand': 11},
    16: {'coords': (38, 46), 'demand': 12},
    17: {'coords': (61, 33), 'demand': 26},
    18: {'coords': (62, 63), 'demand': 17},
    19: {'coords': (63, 69), 'demand': 6},
    20: {'coords': (45, 35), 'demand': 15},
    21: {'coords': (32, 39), 'demand': 5},
    22: {'coords': (56, 37), 'demand': 10}
}

# Robot tours and reported travel costs
tours = {
    0: {'tour': [0, 18, 19, 1, 21, 0], 'reported_cost': 92.72},
    1: {'tour': [0, 9, 17, 0], 'reported_cost': 72.90},
    2: {'tour': [0, 12, 15, 16, 0], 'reported_cost': 69.31},
    3: {'tour': [0, 8, 13, 0], 'reported_cost': 71.62},
    4: {'tour': [0, 14, 22, 0], 'reported_cost': 67.24},
    5: {'tour': [0, 4, 11, 0], 'reported_cost': 57.39},
    6: {'tour': [0, 3, 10, 20, 0], 'reported_cost': 82.78},
    7: {'tour': [0, 5, 7, 0], 'reported_cost': 53.11}
}

robot_capacity = 40

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    coord1, coord2 = cities[city1]['coords'], cities[city2]['coords']
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_tours():
    demands_met = {i: 0 for i in cities}
    total_calculated_cost = 0

    for robot, data in tours.items():
        tour = data['tour']
        reported_cost = data['reported_cost']
        calculated_cost = 0
        load = 0
        
        # Calculate travel cost and load for the tour
        for i in range(len(tour) - 1):
            city_current = tour[i]
            city_next = tour[i + 1]
            calculated_cost += calculate_distance(city_current, city_next)
            if city_next != 0:  # Excluding depot city
                demands_met[city_next] += cities[city_next]['demand']
                load += cities[city_next]['demand']
        
        if abs(calculated_cost - reported_cost) > 0.01 or load > robot_capacity:
            return "FAIL"
        
        total_calculated_cost += calculated_cost

    if not all(demands_met[city] == cities[city]['demand'] for city in cities if city != 0):
        return "FAIL"

    return "CORRECT"

# Running the verification
print(verify_tours())