import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, demands, capacities, coordinates):
    # Verify all demands are met exactly once
    city_demand_met = [0] * len(demands)
    for robot, tour in enumerate(tours):
        load = 0
        last_city = 0
        route_demand = 0
        for city in tour[1:]:  # start checking from the first city after depot
            if city != 0:  # if it's not returning to the depot
                load += demands[city]
                city_demand_met[city] += demands[city]
            last_city = city
        if load > capacities[robot]:  # Checking if capacity constraints are met
            return "FAIL"

    if any(x != y for x, y in zip(city_demand_met[1:], demands[1:])):  # demand must be met exactly, not exceeding/under for each city
        return "FAIL"

    # Verify that each tour starts and ends at the depot city
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    return "CORRECT"

# Robot tours
robot_tours = [
    [0, 16, 17, 13, 15, 14, 7, 4, 10, 18, 0],  # Robot 0 Tour
    [0, 8, 3, 9, 12, 11, 5, 2, 1, 0]           # Robot 1 Tour
]

# City demands and coordinates
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Capacities of each robot
robot_capacities = [160, 160]

result = verify_solution(robot_tours, demands, robot_capacities, coordinates)
print(result)