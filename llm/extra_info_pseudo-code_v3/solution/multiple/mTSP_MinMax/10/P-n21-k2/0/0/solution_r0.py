import numpy as np
from scipy.spatial.distance import cdist
import random

def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def fuzzy_c_means_clustering(cities, k=2, m=2):
    n = len(cities)
    max_iter = 500
    convergence_criteria = 1e-4
    v = np.array(random.choices(cities, k=k))  # Initialize cluster centers randomly
    u = np.random.dirichlet(np.ones(k), n)  # Initialize membership matrix
    
    for iteration in range(max_iter):
        previous_v = np.copy(v)
        for j in range(k):
            u_col_pow = u[:, j] ** m
            v[j] = np.sum(u_col_pow[:, None] * cities, axis=0) / np.sum(u_col_pow)
            
        dist = cdist(cities, v)
        for i in range(n):
            for j in range(k):
                u[i, j] = 1 / np.sum((dist[i, j] / dist[i]) ** (2 / (m - 1)))
                
        if np.linalg.norm(v - previousv) < convergence_criteria:
            break
    
    return np.argmax(u, axis=1), v

def greedy_route(cluster_indices, cities, num_robots):
    routes = [[] for _ in range(num_robots)]
    cities_per_robot = [list(np.where(cluster_indices == i)[0]) for i in range(num_robots)]
    
    for robot_id, city_indices in enumerate(cities_per_robot):
        current_city = 0  # Start at the depot
        route = [current_city]
        while city_indices:
            next_city = min(city_indices, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
            route.append(next_city)
            city_indices.remove(next_city)
            current_city = next_city
        route.append(0)  # Return to the depot
        routes[robot_id] = route
    
    return routes

def calculate_route_cost(route, cities):
    return sum(euclidean_distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route) - 1))

def main(cities, num_robots):
    cluster_indices, cluster_centers = fuzzy_c_means_clustering(np.array(cities[1:]), num_robots, m=2)
    cluster_indices += 1  # because indices are offset due to the depot exclusion in clustering
    
    routes = greedy_route(cluster_indices, cities, num_robots)
    costs = [calculate_route_cost(route, cities) for route in routes]
    max_cost = max(costs)
    
    for i, route in enumerate(routes):
        print(f'Robot {i} Tour: {route}')
        print(f'Robot {i} Total Travel Cost: {costs[i]}')
    print(f'Maximum Travel Cost: {max_cost}')
    
# Specify city coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

main(cities, 2)  # Execute with 2 robots as specified