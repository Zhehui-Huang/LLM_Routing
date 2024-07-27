import math
import random
from collections import defaultdict

# City coordinates indexed by city ID
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Simulated Annealing to optimize route
def simulated_annealing(initial_route):
    temp = 1000
    cooling_rate = 0.99
    current_route = initial_route[:]
    best_route = current_route[:]
    best_cost = route_cost(current_route)

    while temp > 1:
        new_route = current_route[:]
        l = len(new_route)
        i, j = random.randint(0, l-1), random.randint(0, l-1)
        new_route[i], new_route[j] = new_route[j], new_route[i]
        
        current_cost = route_cost(current_route)
        new_cost = route_cost(new_route)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_route = new_route[:]
            if new_cost < best_cost:
                best_route = new_route[:]
                best_cost = new_cost
                
        temp *= cooling_rate

    return best_route, best_cost

# Compute total cost of a tour
def route_cost(route):
    cost = 0
    for i in range(1, len(route)):
        cost += distance(route[i-1], route[i])
    return cost

# Distribute cities among the robots
def distribute_cities():
    non_depot_cities = list(range(2, 21))
    random.shuffle(non_depot_cities)
    mid = len(non_depot_cities) // 2
    robot_0_cities = sorted([0] + non_depot_cities[:mid])
    robot_1_cities = sorted([1] + non_depot_cities[mid:])
    return robot_0_cities, robot_1_cities

# Main function to solve the problem
def optimize_routes():
    robot_0_cities, robot_1_cities = distribute_cities()

    robot_0_tour, robot_0_cost = simulated_annealing(robot_0_cities)
    robot_1_tour, robot_1_cost = simulated_annealing(robot_1_cities)

    robot_0_tour.append(robot_0_tour[0])
    robot_1_tour.append(robot_1_tour[0])

    print(f"Robot 0 Tour: {robot_0_tour}")
    print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
    print(f"Robot 1 Tour: {robot_1_tour}")
    print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
    print(f"Overall Total Travel Cost: {robot_0_cost + robot_1_cost}")

optimize_routes()