import math

# Definition of cities and their coordinates
city_coords = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Demands at each city, excluding the depot city 0
city_demands = {
    1: 7,
    2: 30,
    3: 16,
    4: 23,
    5: 11,
    6: 19,
    7: 15,
    8: 28,
    9: 8,
    10: 8,
    11: 7,
    12: 14,
    13: 6,
    14: 19,
    15: 11,
    16: 12,
    17: 26,
    18: 17,
    19: 6,
    20: 15,
    21: 5,
    22: 10
}

# Capacity of each robot
robot_capacity = 40

# Sample robot tours and their costs as per the provided solution
robot_tours = {
    0: ([0, 21, 16, 1, 10, 13, 0], 72.09),
    1: ([0, 6, 20, 19, 0], 101.15),
    2: ([0, 2, 22, 0], 61.09),
    3: ([0, 4, 11, 9, 0], 104.90),
    4: ([0, 7, 5, 12, 0], 95.16),
    5: ([0, 15, 3, 0], 78.20),
    6: ([0, 14, 18, 0], 106.50),
    7: ([0, 17, 0], 63.56)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((city_coords[c1][0] - city_coords[c2][0])**2 + (city_coords[c1][1] - city_coords[c2][1])**2)

# Check for the correctness of the given solution
def verify_solution(robot_tours):
    total_calculated_cost = 0
    all_visited_cities = set()
    
    for robot_id, (tour, reported_cost) in robot_tours.items():
        # Ensure tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate the travel cost and check the robot's capacity usage
        travel_cost = 0
        load = 0
        last_city = tour[0]
        
        for city in tour[1:]:
            travel_cost += euclidean_distance(last_city, city)
            if city != 0:  # Do not count depot city
                load += city_demands[city]
                all_visited_cities.add(city)
            last_city = city
        
        # Check if reported cost matches calculated cost (allowing for minor floating point rounding errors)
        if not math.isclose(travel_cost, reported_cost, abs_tol=0.01):
            return "FAIL"
        
        # Check if the load exceeds the robot capacity
        if load > robot_capacity:
            return "FAIL"
        
        # Accumulate total travel cost for validation
        total_calculated_cost += travel_cost
    
    # Check if all cities are visited at least once
    if all_visited_cities != set(city_demands.keys()):
        return "FAIL"
    
    return "CORRECT"

# Verification of the provided solution
result = verify_solution(robot_tours)
print(result)