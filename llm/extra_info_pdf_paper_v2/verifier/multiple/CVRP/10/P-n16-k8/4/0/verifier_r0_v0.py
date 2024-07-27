import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
city_coordinates = [
    (30, 40), # Depot
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Robot tours
robots_tours = [
    [0, 1, 0],
    [0, 2, 0],
    [0, 3, 10, 0],
    [0, 4, 0],
    [0, 5, 7, 0],
    [0, 6, 0],
    [0, 8, 0],
    [0, 9, 13, 14, 0],
    [0, 11, 12, 15, 0]
]

# Robot capacities
robot_capacity = 35

# City demands
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Validation of requirements
def validate_solution(robots_tours, city_coordinates, robot_capacity, city_demands):
    all_cities_visited = set(range(1, len(city_demands)))
    demand_fulfilled = [0] * len(city_demands)
    robot_capacity_usage = []
    total_cost = 0

    for tour in robots_tours:
        robot_load = 0
        last_city = 0
        tour_cost = 0

        for city in tour:
            if city != last_city:
                tour_cost += euclidean_distance(city_coordinates[last_city], city_coordinates[city])
                robot_load += city_demands[city]
                demand_fulfilled[city] += city_demands[city]
                last_city = city

        robot_capacity_usage.append(robot_load)
        total_cost += tour_cost + euclidean_distance(city_coordinates[last_city], city_coordinates[0])  # Return to depot

        # Requirement 3 check within loop
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
    # Requirement 6
    if all_cities_visited != set(city for tour in robots_tours for city in tour[1:-1]):
        return "FAIL"
    
    # Requirement 1
    if any(city_demands[i] != demand_fulfilled[i] for i in range(len(city_demands))):
        return "FAIL"
    
    # Requirement 2
    if any(load > robot_capacity for load in robot_capacity_usage):
        return "FAIL"

    return "CORRECT"

result = validate_solution(robots_tours, city_coordinates, robot_capacity, city_demands)
print(result)