import math

# City coordinates and demands
cities = {
    0: (30, 40, 0),
    1: (37, 52, 19),
    2: (49, 43, 30),
    3: (52, 64, 16),
    4: (31, 62, 23),
    5: (52, 33, 11),
    6: (42, 41, 31),
    7: (52, 41, 15),
    8: (57, 58, 28),
    9: (62, 42, 14),
    10: (42, 57, 8),
    11: (27, 68, 7),
    12: (43, 67, 14),
    13: (58, 27, 19),
    14: (37, 69, 11),
    15: (61, 33, 26),
    16: (62, 63, 17),
    17: (63, 69, 6),
    18: (45, 35, 15)
}

# Tours provided in the solution
tours = {
    0: [0, 17, 10, 16, 2, 8, 9, 13, 7, 12, 0],
    1: [0, 15, 5, 6, 18, 4, 1, 11, 14, 3, 0]
}

# Robot capacities
robot_capacity = 160

def calculate_euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(cities, tours, robot_capacity):
    supply_record = {city: 0 for city in cities}
    total_cost = 0.0

    for robot, tour in tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start and end at depot for robot {}".format(robot)
        
        load = 0
        tour_cost = 0.0
        
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            city_from_coordinates = cities[city_from][:2]  # Exclude demand
            city_to_coordinates = cities[city_to][:2]  # Exclude demand
            distance = calculate_euclidean_distance(city_from_coordinates, city_to_coordinates)
            tour_cost += distance
            
            if city_to != 0:
                load += cities[city_to][2]
                supply_record[city_to] += cities[city_to][2]
        
        if load > robot_capacity:
            return "FAIL: Capacity exceeded for robot {}".format(robot)
        
        total_cost += tour_cost

    # Check demands are met exactly    
    for city, (x, y, demand) in cities.items():
        if supply_record[city] != demand:
            return "FAIL: Demand not fulfilled for city {}".format(city)
    
    # Check minimization of total cost is reasonable
    if not (total_cost <= 414.51 + 0.1 and total_cost >= 414.51 - 0.1):
        return "FAIL: Total cost does not match expected value within a reasonable range"

    return "CORRECT"

# Validation of the provided solution
print(verify_solution(cities, tours, robot_capacity))