import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tour_and_cost(robot_tour, robot_travel_cost, coordinates, demand, capacity):
    total_demand = 0
    last_city = robot_tour[0]
    calculated_cost = 0
    
    # Track load, tour start and end with depot
    current_load = 0
    
    for city in robot_tour[1:]:
        # Calculate travel cost
        calculated_cost += calculate_euclidean_distance(*coordinates[last_city], *coordinates[city])
        last_city = city

        # Check if the current city is the depot, reset current load
        if city == 0:
            current_load = 0
        else:
            current_load += demand[city]
            total_demand += demand[city]
            # Check if current load exceeds capacity
            if current_load > capacity:
                return False
    
    # Add final return to depot cost
    calculated_cost += calculate_euclidean_distance(*coordinates[last_city], *coordinates[0])

    if round(calculated_cost, 2) != robot_travel_cost:
        return False

    return total_demand, calculated_cost

def unit_test_solution(robot_tours_data, coordinates, demands, capacity):
    cities_covered = set()
    total_calculated_cost = 0
    capacity_constraint = True

    for data in robot_tours_data:
        robot_tour, robot_travel_cost = data
        total_demand, calculated_cost = check_tour_and_cost(robot_tour, robot_travel_cost, coordinates, demands, capacity)

        if total_demand is False:
            return "FAIL"
        
        total_calculated_cost += calculated_cost
        cities_covered.update(robot_tour)
        # Add demands and check capacities
        if total_demand > capacity:
            capacity_constraint = False

    all_cities_covered = (cities_covered == set(range(len(coordinates)))) # to check all cities including depot are visited

    # Check if each city's demand is covered exactly once excluding depot (0)
    if len(cities_covered) == len(coordinates) and capacity_constraint and all_cities_covered:
        return "CORRECT"
    else:
        return "FAIL"

# City coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot tours and travel costs provided
robot_0_tour = [0, 11, 9, 14, 0, 17, 13, 0, 15, 19, 0, 18, 8, 3, 12, 0]
robot_0_cost = 387.86

robot_1_tour = [0, 6, 1, 4, 2, 5, 0, 7, 20, 10, 16, 0]
robot_1_cost = 172.51

data = [([robot_0_tour, robot_0_cost], [robot_1_tour, robot_1_cost])]

result = unit_test_solution(data, coordinates, demands, 160)
print(result)