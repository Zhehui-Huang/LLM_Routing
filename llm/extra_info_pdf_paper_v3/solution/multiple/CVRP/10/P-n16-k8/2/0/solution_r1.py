import math
import numpy as np

# Cities coordinates
coordinates = [
    (30, 40),  # depot
    (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), 
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69)
]

# Demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number of Robots & their capacity
num_robots = 8
capacity = 35

# Euclidean distance calculation
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Heuristic solver for CVRP using a simplistic greedy approach
def solve_cvrp(coordinates, demands, num_robots, capacity):
    cities = list(range(1, len(coordinates)))  # Exclude the depot for the city list
    tours = [[] for _ in range(num_robots)]
    capacities = [capacity] * num_robots
    depot = 0

    # Assign cities to robots in a greedy manner
    city_index = 0
    for robot in range(num_robots):
        while city_index < len(cities) and capacities[robot] >= demands[cities[city_index]]:
            if capacities[robot] >= demands[cities[city_index]]:
                tours[robot].append(cities[city_index])
                capacities[robot] -= demands[cities[city_index]]
                city_index += 1
            else:
                break

    # Include depot as start and end point
    for i in range(num_robots):
        tours[i] = [depot] + tours[i] + [depot] if tours[i] else [depot, depot]
    
    return tours

def calculate_travel_costs(tours):
    total_cost = 0
    costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(tour[i], tour[i+1])
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

tours = solve_cvrp(coordinates, demands, num_robots, capacity)
costs, total_cost = calculate_travel_costs(tours)

# Output tour information and costs
for idx, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")