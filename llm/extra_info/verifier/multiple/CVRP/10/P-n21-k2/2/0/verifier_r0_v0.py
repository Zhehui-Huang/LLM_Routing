import math

# City coordinates and demands
cities = {
    0: (30, 40, 0), 1: (37, 52, 7), 2: (49, 49, 30), 3: (52, 64, 16),
    4: (31, 62, 23), 5: (52, 33, 11), 6: (42, 41, 19), 7: (52, 41, 15),
    8: (57, 58, 28), 9: (62, 42, 8), 10: (42, 57, 8), 11: (27, 68, 7),
    12: (43, 67, 14), 13: (58, 48, 6), 14: (58, 27, 19), 15: (37, 69, 11),
    16: (38, 46, 12), 17: (61, 33, 26), 18: (62, 63, 17), 19: (63, 69, 6),
    20: (45, 35, 15)
}

# Robotic tours - list of tuples (tour list, reported travel cost)
robots = [
    ([0, 1, 12, 15, 0], 66.21),
    ([0, 4, 11, 0], 57.39),
    ([0, 2, 6, 7, 9, 13, 0], 77.60),
    ([0, 16, 10, 3, 8, 18, 19, 0], 98.81),
    ([0, 5, 20, 14, 17, 0], 70.07)
]

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Verify the tours
def verify_tours(robots, cities):
    total_cost_calculated = 0
    demand_fulfilled = {i: 0 for i in range(1, 21)}
    robot_capacity = 160
    
    for tour, reported_cost in robots:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Start and end at depot
        
        travel_cost = 0
        load = 0
        
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i+1]
            travel_cost += euclidean_distance(cities[city_from][:2], cities[city_to][:2])
            if city_to != 0:
                load += cities[city_to][2]
                demand_fulfilled[city_to] += cities[city_to][2]
        
        if load > robot_capacity:
            return "FAIL"  # Exceeded capacity
        
        if abs(travel_cost - reported_cost) >= 0.01:
            return "FAIL"  # Reported cost incorrect
        
        total_cost_calculated += reported_cost
    
    if any(demand_fulfilled[city] != cities[city][2] for city in range(1, 21)):
        return "FAIL"  # Demands not met

    return "CORRECT"

# Check if the solution is correct
print(verify_tours(robots, cities))