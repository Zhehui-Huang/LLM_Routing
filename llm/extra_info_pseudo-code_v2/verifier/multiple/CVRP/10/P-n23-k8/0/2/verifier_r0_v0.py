import math

# Coordinate data for each city
cities = {
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

# Demand for each city
demands = {
    0: 0,
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

# Provided solution with tours
tours = [
    [0, 1, 10, 12, 15, 0],
    [0, 2, 0],
    [0, 3, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 5, 14, 22, 0],
    [0, 6, 0],
    [0, 7, 20, 21, 0],
    [0, 8, 16, 0],
    [0, 9, 17, 13, 0]
]

# Capacity of each robot
robot_capacity = 40
num_robots = 8  # indicates max number of distinct robots used


def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_solution(tours, robot_capacity, demands):
    # Check robot counts
    if len(tours) > num_robots:
        return "FAIL: More robots used than available"
    
    visited_cities = set()
    total_system_cost = 0.0

    for tour in tours:
        load = 0
        tour_cost = 0.0
        previous_city = tour[0]  # starts at the depot

        for city in tour[1:]:
            if city != 0 and demands[city] == 0:
                return "FAIL: City demand is already met"
            # Calculate load and check against capacity
            load += demands[city]
            if load > robot_capacity:
                return "FAIL: Exceeds robot capacity"
            
            # Calculate and check travel cost
            travel_cost = calculate_distance(cities[previous_city], cities[city])
            tour_cost += travel_skin
            previous_city = city
            visited_cities.add(city)
        
        # Verify tour ends at depot
        if tour[-1] != 0:
            return "FAIL: Tour does not end at the depot"
        
        # Close the round trip to depot
        tour_cost += calculate_distance(cities[previous_city], cities[0])
        total_system_cost += tour_cost

    # Check if all cities except the depot were visited
    if visited_cities != set(demands.keys()) - {0}:
        return "FAIL: Not all cities were visited"
    
    # Check if the total cost matches the provided "Overall Total Travel Club"
    if not math.isclose(total_system_cost, 548.7976153192476, rel_tol=1e-4):
        return f"FAIL: Cost mismatch. Calculated: {total_system_tour_cost}, Expected: 548.7976153192476"

    return "CORRECT"

# Running the validation function
result = validate_solution(tours, robot_capacity, demands)
print(result)