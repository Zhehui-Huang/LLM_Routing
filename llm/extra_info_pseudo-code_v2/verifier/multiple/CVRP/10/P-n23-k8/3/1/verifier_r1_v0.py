import math
from collections import defaultdict

# City Coordinates and Demands
cities = {
    0: {'coord': (30, 40), 'demand': 0},
    1: {'coord': (37, 52), 'demand': 7},
    2: {'coord': (49, 49), 'demand': 30},
    3: {'coord': (52, 64), 'demand': 16},
    4: {'coord': (31, 62), 'demand': 23},
    5: {'coord': (52, 33), 'demand': 11},
    6: {'coord': (42, 41), 'demand': 19},
    7: {'coord': (52, 41), 'demand': 15},
    8: {'coord': (57, 58), 'demand': 28},
    9: {'coord': (62, 42), 'demand': 8},
    10: {'coord': (42, 57), 'demand': 8},
    11: {'coord': (27, 68), 'demand': 7},
    12: {'coord': (43, 67), 'demand': 14},
    13: {'coord': (58, 48), 'demand': 6},
    14: {'coord': (58, 27), 'demand': 19},
    15: {'coord': (37, 69), 'demand': 11},
    16: {'coord': (38, 46), 'demand': 12},
    17: {'coord': (61, 33), 'demand': 26},
    18: {'coord': (62, 63), 'demand': 17},
    19: {'coord': (63, 69), 'demand': 6},
    20: {'coord': (45, 35), 'demand': 15},
    21: {'coord': (32, 39), 'demand': 5},
    22: {'coord': (56, 37), 'demand': 10}
}

# Robot Tours and Costs
tours = [
    {'tour': [0, 18, 19, 18, 0], 'cost': 90.98},
    {'tour': [0, 3, 19, 3, 0], 'cost': 89.28},
    {'tour': [0, 8, 19, 8, 0], 'cost': 89.96},
    {'tour': [0, 13, 3, 18, 0], 'cost': 95.67},
    {'tour': [0, 13, 18, 3, 0], 'cost': 87.25},
    {'tour': [0, 13, 9, 17, 0], 'cost': 77.17},
    {'tour': [0, 13, 17, 9, 0], 'cost': 85.54},
    {'tour': [0, 9, 13, 8, 0], 'cost': 81.77}
]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1]['coord'][0] - cities[city2]['coord'][0]) ** 2 + (cities[city1]['coord'][1] - cities[city2]['coord'][1]) ** 2)

def verify_solution():
    total_calculated_cost = 0
    demand_fulfilled = defaultdict(int)
    max_capacity = 40
    
    for robot in tours:
        tour = robot['tour']
        calculated_cost = 0
        
        # Ensure each tour starts and ends at Depot City 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate costs between cities
        for i in range(len(tour) - 1):
            calculated_cost += euclidean_distance(tour[i], tour[i + 1])
            demand_fulfilled[tour[i + 1]] += cities[tour[i + 1]]['demand']
        
        if not math.isclose(calculated_cost, robot['cost'], rel_tol=1e-2):
            return "FAIL"
        
        # Check capacity constraints
        load = 0
        visited = set()
        for city in tour:
            if city in visited and city != 0:
                load = 0 # Assuming unloading and reloading happening at depot
            visited.add(city)
            load += cities[city]['demand']
            if load > max_capacity:
                return "FAIL"
        
        total_calculated_cost += calculated_cost
    
    # Check demand fulfillment
    for city in range(1, len(cities)):
        if demand_fulfilled[city] < cities[city]['demand']:
            return "FAIL"
    
    return "CORRECT"

# Unit Test Result
print(verify_solution())