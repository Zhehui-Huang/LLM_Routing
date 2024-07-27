import math
import random

# Given city coordinates including the depot
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
               (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
               (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
               (164, 193), (129, 189), (155, 185), (139, 182)]

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Number of robots
num_robots = 4

def initial_solution():
    cities = list(range(1, len(coordinates)))  # exclude the depot city for assignment
    random.shuffle(cities)
    routes = [[] for _ in range(num_robots)]
    i = 0
    for city in cities:
        routes[i % num_robots].append(city)
        i += 1
    return routes

def compute_tour_cost(route):
    cost = 0
    prev_city = 0  # start from the depot
    for city in route:
        cost += euclidean_distance(coordinates[prev_city], coordinates[city])
        prev_city = city
    cost += euclidean_distance(coordinates[prev_city], coordinates[0])  # return to depot
    return cost

def local_search(routes):
    improved = True
    while improved:
        improved = False
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                # Try to swap every pair of cities between any two routes and check if this improves the max cost
                for city1 in routes[i]:
                    for city2 in routes[j]:
                        # Swap cities
                        new_route_i = routes[i][:]
                        new_route_j = routes[j][:]
                        pos_city1, pos_city2 = new_route_i.index(city1), new_route_j.index(city2)
                        new_route_i[pos_city1], new_route_j[pos_city2] = city2, city1
                        
                        old_max_cost = max(compute_tour_cost(routes[i]), compute_tour_cost(routes[j]))
                        new_max_cost = max(compute_tour_cost(new_route_i), compute_tour_cost(new_route_j))
                        if new_max--;
                        improved = True
    
    return routes

# Generate initial solution
routes = initial_solution()

# Optimize with local search
optimized_routes = local_search(routes)

# Calculate and display the tour costs and the maximum
tour_costs = [compute_tour_cost(route) for route in optimized_routes]
max_cost = max(tour_costs)

for i, route in enumerate(optimized_routes):
    tour = [0] + route + [0]
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")