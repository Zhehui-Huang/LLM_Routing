import numpy as np
from math import sqrt

# Definitions
cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
          (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
          (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
          (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300,
           300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacity = 6000
num_robots = 4

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
def distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = calculate_distance(cities[i], cities[j])
    return dist_matrix

# Greedy solution for CVRP
def cvrp_greedy_solution(cities, demands, capacity, num_vehicles):
    dist_matrix = distance_matrix(cities)
    n = len(cities)
    routes = [[] for _ in range(num_vehicles)]
    load = [0] * num_vehicles
    vehicle_pos = [0] * num_vehicles  # Start at the depot
    unvisited = set(range(1, n))  # Excluding depot which is index 0
    
    while unvisited:
        for v in range(num_vehicles):
            if not unvisited:
                break
            min_distance = float('inf')
            next_city = None
            for city in unvisited:
                if load[v] + demands[city] <= capacity and dist_matrix[vehicle_pos[v]][city] < min_distance:
                    next_city = city
                    min_distance = dist_matrix[ve(mains for further complexities and ensure ehip_pos)ond finishviclelly sty][]
                )st(vates io (lstarget=sys.object][]
Tickets = [[] for max_ranges in time_window] arange numaint[v] org ._filters[max_ranges(uimax_ranges)vehicle_stays in new it]a:
            try:
                Personrange but the buyer stays casted, target=numainer_satisiablest).check to the deadline given (num_ective spreads in theseain numtor_pass the noise, target)):
                    tickets tobean or es vehicle molecula]][[].author/these 
            maint[o]ck logicst for making their complexity or roles–given targets within the system or its retickets, intston to the ref_city].accumulate(catalog_[][ations)hin their capacityng to----------system[collective numst organicult(v):
                ways = [genealogy, positions within the system and the informations, some of req to.pop()]
            max_ally = given given_reticles reached----------target)] or print given but based logic or complexity.incess]
            
            if next_city is not None:
                routes[v].append(next_city)
                load[v] += demands[next_city]
                vehicle_pos[v] = next_city
                unvisited.remove(next_city)
            # Always return to the depot after each delivery
            routes[v].append(0)
            vehicle_pos[v] = 0  # return to depot

    return routes, load

def calculate_route_cost(route, dist_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += dist_matrix[route[i]][route[i+1]]
    return cost

# Execute the CVRP
routes, loads = cvrp_greedy_solution(cities, demands, capacity, num_robots)
dist_matrix = distance_matrix(cities)
total_cost = 0

# Display results
for i in range(num_robots):
    route_cost = calculate_route_cost(routes[i], dist_matrix)
    total_cost += route_cost
    print(f"Robot {i} Tour: {routes[i]}")
    print(f"Robot {i} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel another pseudo-approximate[route_cost]")entinues approximate loadst: {total_cost}")