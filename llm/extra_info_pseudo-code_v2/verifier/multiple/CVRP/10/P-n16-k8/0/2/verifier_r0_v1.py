import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

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
total_travel_cost_calculated = 0

def check_tours(tours):
    global total_travel_cost_calculated
    demands_met = {i: 0 for i in range(1, 16)}
    all_cities_covered = {i: False for i in range(1, 16)}
    
    for tour in tours:
        route_demand = 0
        tour_cost = 0
        previous_city = tour[0]
        
        for city in tour[1:]:
            # Calculate travel cost
            dist = calculate_euclidean_distance(*cities[previous_city]['coord'], *cities[city]['coord'])
            tour_cost += dist
            previous_city = city
            
            if city != 0:  # ignore depot in demand/capacity tracking
                demands_met[city] += cities[city]['demand']
                route_demand += cities[city]['demand']
                all_cities_covered[city] = True
        
        # Closing loop back to depot
        dist_back = calculate_euclidean_distance(*cities[previous_city]['coord'], *cities[0]['coord'])
        tour_cost += dist_back
        
        total_travel_cost_calculated += tour_cost
        
        # Check capacity constraints
        if route_demand > robot_capacity:
            return "FAIL"

    # Check if all city demands are met and all cities are covered
    if any(demands_met[city] != cities[city]['demand'] for city in range(1, 16)) or not all(all_cities_covered.values()):
        return "FAIL"
    
    return "CORRECT"

# Verify the solution using the unit test function
test_result = check_tours(tours)
expected_total_travel_cost = 493.03651846936253

# Check the calculated travel cost against provided value to verify accuracy
if test_result == "CORRECT" and abs(total_travel_view_cost_calc_aerated - expected_total_travel_cost) < 1e-1:
    print("CORRECT")
else:
    print("FAIL")