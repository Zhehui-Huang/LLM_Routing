import math

# Coordinates and demands
cities = {
    0: {'coords': (145, 215), 'demand': 0},
    1: {'coords': (151, 264), 'demand': 1100},
    2: {'coords': (159, 261), 'demand': 700},
    3: {'coords': (130, 254), 'demand': 800},
    4: {'coords': (128, 252), 'demand': 1400},
    5: {'coords': (163, 247), 'demand': 2100},
    6: {'coords': (146, 246), 'demand': 400},
    7: {'coords': (161, 242), 'demand': 800},
    8: {'coords': (142, 239), 'demand': 100},
    9: {'coords': (163, 236), 'demand': 500},
    10: {'coords': (148, 232), 'demand': 600},
    11: {'coords': (128, 231), 'demand': 1200},
    12: {'coords': (156, 217), 'demand': 1300},
    13: {'coords': (129, 214), 'demand': 1300},
    14: {'coords': (146, 208), 'demand': 300},
    15: {'coords': (164, 208), 'demand': 900},
    16: {'coords': (141, 206), 'demand': 2100},
    17: {'coords': (147, 193), 'demand': 1000},
    18: {'coords': (164, 193), 'demand': 900},
    19: {'coords': (129, 189), 'demand': 2500},
    20: {'coords': (155, 185), 'demand': 1800},
    21: {'coords': (139, 182), 'demand': 700}
}

# Calculate the Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((cities[c1]['coords'][0] - cities[c2]['coords'][0]) ** 2 + (cities[c1]['coords'][1] - cities[c2]['coords'][1]) ** 2)

# Robot tours as provided
robots = [
    {'tour': [0, 13, 10, 4, 18, 0], 'total_cost': 168.67272393595528},
    {'tour': [0, 15, 20, 9, 6, 8, 11, 3, 0], 'total_cost': 205.35208655932917},
    {'tour': [0, 14, 16, 5, 2, 0], 'total_cost': 121.62927401477361},
    {'tour': [0, 12, 7, 1, 17, 21, 0], 'total_cost': 179.0966063641284}
]

# Robot capacity
capacity = 6000

def verify_solution(robots):
    # Verify requirements
    total_delivery = {}
    real_total_cost = 0

    # Track deliveries to requirement 2 and verify tours for requirement 4
    for robot in robots:
        current_capacity = 0
        last_city = robot['tour'][0]
        for i, city in enumerate(robot['tour']):
            if i > 0:
                current_capacity += cities[city]['demand']
                if city != 0:  # Exclude the depot for delivery check
                    total_delivery[city] = total_delivery.get(city, 0) + cities[city]['demand']
            # Calculate travel costs
            if i > 0:
                real_total_cost += distance(last_city, city)
                last_city = city
            # Requirement 5: Check if current robot exceeds capacity
            if current_capacity > capacity:
                return "FAIL"

    # Requirement 2: Check all demands are met exactly
    for city in range(1, len(cities)):
        if total_delivery.get(city, 0) != cities[city]['demand']:
            return "FAIL"

    # Requirement 6: Check the total cost calculations
    calculated_total_cost = sum(robot['total_cost'] for robot in robots)
    if not math.isclose(real_total_cost, calculated_total_COST, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Check if solution is correct
result = verify_solution(robots)
print(result)