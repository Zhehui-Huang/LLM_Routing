import math

# Given data setups
cities_coordinates = {
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
    15: (37, 69)
}

city_demands = {
    1: 19,
    2: 30,
    3: 16,
    4: 23,
    5: 11,
    6: 31,
    7: 15,
    8: 28,
    9: 8,
    10: 8,
    11: 7,
    12: 14,
    13: 6,
    14: 19,
    15: 11
}

robot_capacity = 35
num_robots = 8
robot_tours = [
    [0, 9, 13, 0],
    [0, 12, 15, 0],
    [0, 5, 14, 0],
    [0, 4, 11, 0],
    [0, 3, 10, 0],
    [0, 1, 7, 0],
    [0, 2, 0],
    [0, 6, 0]
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check if robot tours meet the requirements
def verify_solution():
    total_system_cost = 0
    visited_cities = {0: num_robots}  # Every robot visits depot initially

    for robot_id in range(num_robots):
        tour = robot_tours[robot_id]
        robot_load = 0
        total_tour_cost = 0
        
        for i in range(len(tour) - 1):
            city_current = tour[i]
            city_next = tour[i + 1]
            
            # Calculate travel cost
            travel_cost = calculate_distance(city_current, city_next)
            total_tour_cost += travel_cost
            
            if city_next != 0:  # Do not count the depot for demand or capacity
                robot_load += city_demands[city_next]
                if city_next in visited_cities:
                    visited_cities[city_next] += 1
                else:
                    visited_cities[city_next] = 1
                
        # Check capacity does not exceed
        if robot_load > robot_capacity:
            return "FAIL"
        
        # Update system cost
        total_system_cost += total_tour_cost
        
        if tour[-1] != 0:  # Ensure return to depot
            return "FAIL"

    # Check all cities are visited and demands are fulfilled exactly once
    if all(visited_cities.get(city, 0) == 1 for city in range(1, 16)):
        return "CORRECT"
    else:
        return "FAIL"

# Run verification test
result = verify_solution()
print(result)