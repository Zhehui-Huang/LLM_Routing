def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities given their coordinates. """
    from math import sqrt
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, demands, robot_capacities):
    visited_cities = set()
    total_cost = 0
    city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
                        (52, 71), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
                        (58, 27), (37, 69)]
    
    # Check each robot's tour
    for robot_idx, tour in enumerate(tours):
        # Start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate load and validate capacity
        load = 0
        for i in range(1, len(tour) - 1):
            city = tour[i]
            load += demands[city]
            visited_cities.add(city)

        if load > robot_capacities:
            return "FAIL"

        # Calculate travel cost for this tour
        robot_total_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            robot_total_cost += calculate_distance(city_coordinates[city1], city_coordinates[city2])

        # Sum all costs
        total_cost += robot_total_cost
    
    # Check if all cities are visited
    if sorted(visited_cities) != list(range(1, 16)):
        return "FAIL"
    
    # Check if overall cost is incorrectly reported
    if total_cost != 0:
        return "FAIL"

    return "CORRECT"

# Robot tours details (example provided)
tours = [
    [0, 2, 0],
    [0, 3, 1, 0],
    [0, 4, 0],
    [0, 6, 0],
    [0, 8, 0],
    [0, 9, 7, 5, 0],
    [0, 13, 12, 11, 10, 0],
    [0, 15, 14, 0]
]

# City demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot capacity
robot_capacity = 35

# Verify the provided solution
result = verify_solution(tours, demands, robot_capacity)
print(result)