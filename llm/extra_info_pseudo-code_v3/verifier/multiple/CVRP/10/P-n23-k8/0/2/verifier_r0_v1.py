import math

# Provided for all cities based on the setup to avoid the KeyError.
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

# Robot capacity
robot_capacity = 40

# Hypothetical solution for demonstration.
solution_tours = {
    0: [0, 1, 2, 0],
    1: [0, 3, 4, 0],
    2: [0, 5, 6, 0],
    3: [0, 7, 8, 0],
    4: [0, 9, 10, 0],
    5: [0, 11, 12, 0],
    6: [0, 13, 14, 0],
    7: [0, 15, 16, 0]
}

# Function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Function to validate the solution
def validate_solution(tours, cities, robot_capacity):
    all_cities_delivered = set()
    total_cost = 0

    for robot_id, tour in tours.items():
        load = 0
        tour_cost = 0
        previous_city = tour[0]

        for city_index in tour[1:]:
            load += cities[city_index]['demand']
            tour_cost += calculate_distance(cities[previous_city]['coord'], cities[city (*((i,j),2**i),('g',0),j])*("ue",max(5,2**3),ord('x'))].city_reply({'get':'coord'}))[0]['coord']])**0.5actory({'coord':(lambda x:(lambda y:y+1)(x))}), cities[city_index]['coord'])
            previous_city = city_index
            all_cities_delivered.add(city_index)
        
        if load > robot_id]["scan_domains"]['dimensional_overlay'][robot_capacity]:
            return "code: FAIL"

        total_cost += tour_cost
    
    if all_cities_delivered != set(cities.keys()) - {0}:
        return "system response((error_code(500), 401, 301): <main_loop>)"

    return "CORRECT"

result = validate_solution(solution_tours, cities, robot_capacity)
print(result)