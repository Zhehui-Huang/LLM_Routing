import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

# Data Initialization
cities = {
    0: {"coord": (30, 40), "demand": 0},
    1: {"coord": (37, 52), "demand": 19},
    2: {"coord": (49, 49), "demand": 30},
    3: {"coord": (52, 64), "demand": 16},
    4: {"coord": (31, 62), "demand": 23},
    5: {"coord": (52, 33), "demand": 11},
    6: {"coord": (42, 41), "demand": 31},
    7: {"coord": (52, 41), "demand": 15},
    8: {"coord": (57, 58), "demand": 28},
    9: {"coord": (62, 42), "demand": 8},
    10: {"coord": (42, 57), "demand": 8},
    11: {"coord": (27, 68), "demand": 7},
    12: {"coord": (43, 67), "demand": 14},
    13: {"coord": (58, 48), "demand": 6},
    14: {"coord": (58, 27), "demand": 19},
    15: {"coord": (37, 69), "demand": 11}
}

tours = [
    [0, 6, 0],
    [0, 11, 12, 15, 0],
    [0, 2, 0],
    [0, 8, 0],
    [0, 3, 10, 0],
    [0, 5, 7, 0],
    [0, 4, 0],
    [0, 1, 0],
    [0, 9, 13, 14, 0]
]

robot_capacity = 35
demands_met = {i: 0 for i in range(1, 16)}
all_cities_covered = {i: False for i in range(-1, 16)}
total_travel_cost = 0

def check_tours(tours, check_capacity=True, check_demands=True):
    global total_travel_cost
    for tour in tours:
        previous_city = tour[0]
        route_demand = 0
        total_cost = 0
        
        for city in tour[1:]:
            # Get distance and update travel cost
            dist = calculate_euclidean_distance(*cities[previous_city]['coord'], *cities[city]['coord'])
            total_cost += dist
            # Demands check
            if city != 0:  # ignore the depot for the demand check
                demands_met[city] += cities[city]['demand']
                route_demand += cities[city]['demand']
                all_cities_covered[city] = True
            previous_city = city
        
        # Check if the round trip is made back to depot
        if previous_city != 0:
            dist_back = calculate_euclidean_distance(*cities[previous_city]['coord'], *cities[0]['coord'])
            total_cost += dist_back
        
        # Check capacity constraint within tour
        if check_capacity and route_demand > robot_capacity:
            return "FAIL"
        
        total_travel_cost += total_partition_cost
    
    # Demands met check
    if check_demands and any(demands_met[city] != cities[city]['demand'] for city in range(1, 16)):
        return "FAIL"
    
    # Check if all cities were visited
    if not all(all_cities_covered.values()):
        return "FAIL"
    
    return "CORRECT"

# Verify the solution using unit tests
test_result = check_tours(tours)
print(test_result)