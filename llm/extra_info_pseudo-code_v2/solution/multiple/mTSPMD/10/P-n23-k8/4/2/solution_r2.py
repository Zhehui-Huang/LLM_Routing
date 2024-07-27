import numpy as np
import math

# Define the cities' coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Distances matrix and pheromone matrix initialization
num_cities = len(city_coords)
distances = np.zeros((num_cities, num_cities))
pheromones = np.ones((num_cities, num_cities)) * 0.1  # initial pheromone levels

# Calculate pairwise city distances
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = math.hypot(city_coords[i][0] - city_coords[j][0], city_coords[i][1] - city_coords[j][1])
        else:
            distances[i][j] = float('inf')  # no self-loop

alpha = 1.0  # Influence of pheromone
beta = 5.0   # Influence of heuristic (1/distance)
evaporation = 0.5
ant_count = 20
generations = 100

def select_next_city(pheromones, distances, current_city, visited):
    pheromone = np.power(pheromones[current_city], alpha)
    heuristic = np.power(1.0 / distances[current_city], beta)
    probabilities = pheromone * heuristic * np.logical_not(visited)
    probabilities /= probabilities.sum()
    next_city = np.random.choice(np.arange(num_cities), p=probabilities)
    return next_city

# Simulation of ant colony optimization
best_route = None
best_distance = float('inf')

for gen in range(generations):
    routes = np.zeros((ant_count, num_cities), dtype=int)
    distances_travelled = np.zeros(ant_count)
    
    for ant in range(ant_count):
        visited = np.zeros(num_cities, dtype=bool)
        current_city = np.random.randint(num_cities)
        route = [current_city]
        visited[current_city] = True
        
        for i in range(1, num_cities):
            next_city = select_next_city(pheromones, distances, current_city, visited)
            route.append(next_city)
            visited[next_city] = True
            distances_travelled[ant] += distances[current_city][next_city]
            current_city = next_city
        
        route.append(route[0])  # Returning to the start city
        distances_travelled[ant] += distances[current_city][route[0]]
        
        if distances_travelled[ant] < best_distance:
            best_distance = distances_travelled[ant]
            best_route = route
        
        routes[ant] = route
    
    # Update pheromones
    pheromones *= evaporation  # evaporation
    for ant in range(ant_count):
        for i in range(num_cities):
            pheromones[routes[ant, i], routes[ant, (i + 1) % num_cities]] += 1.0 / distances_travelled[ant]

# Display best route and its distance
print("Best route found:")
print(best_route)
print("Best distance:")
print(best_distance)