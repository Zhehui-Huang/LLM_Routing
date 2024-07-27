import math
from itertools import combinations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbor_tour(start, cities, city_coords):
    unvisited = cities[:]
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(city_coords[current_city], city_coords[city]))
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city
        
    tour.append(start)  # return to depot
    return tour

def calculate_tour_cost(tour, city_coords):
    cost = 0
    for i in range(len(tour)-1):
        cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return cost

def CVRP(cities, demands, city_coords, robot_count, capacity):
    unassigned_cities = list(cities[1:])  # Exclude depot which is city 0
    routes = [[] for _ in range(robot_count)]
    loads = [0] * robot_count
    
    # Assign cities to robots in a greedy manner based on the nearest available that fits
    for city in sorted(cities[1:], key=lambda c: demands[c], reverse=True):
        for robot_id in range(robot_count):
            if loads[robot_id] + demands[city] <= capacity:
                routes[robot_id].append(city)
                loads[robot_at] += demands[city]
                break

    # Optimize each route using nearest neighbor TSP heuristic
    optimized_routes = []
    costs = []
    for route in routes:
        tour = nearest_neighbor_tour(0, route, city_coords)
        cost = calculate_tour_cost(tour, city_coords)
        optimized_routes.append(tour)
        costs.append(cost)
        
    # Summary
    overall_cost = sum(costs)
    for robot_id, (route, cost) in enumerate(zip(optimized_routes, costs)):
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")
    print(f"Overall Total Travel Cost: {overall_cost}")

# Environment Setup
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
cities = list(range(21))  # 0 to 20
robot_count = 2
capacity = 160

# Run CVRP
CVRP(cities, demands, city_coords, robot_count, capacity)