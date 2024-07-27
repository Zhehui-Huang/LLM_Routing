import numpy as np
import random
import math

# Define the coordinates of each depot and city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = math.dist(coords[i], coords[j])
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)
num_cities = len(coordinates)

# Ant Colony Optimization parameters and initial setup
num_ants = 20
num_iterations = 100
num_robots = 8
alpha = 1.0  # Pheromone importance
beta = 5.0   # Distance priority
rho = 0.1    # Evaporation rate
initial_pheromone = 1.0 / (num_cities * np.mean(distance_matrix))

pheromones = np.full((num_cities, num_cities), initial_pheromone)

def choose_next_city(current_city, feasible_cities):
    pheromone = np.array([pheromones[current_city][i] for i in feasible_cities])
    distances = np.array([distance_matrix[current_city][i] for i in feasible_cities])
    attractiveness = (pheromone ** alpha) * ((1.0 / distances) ** beta)
    probabilities = attractiveness / np.sum(attractiveness)
    next_city = np.random.choice(feasible_cities, p=probabilities)
    return next_city

def update_pheromones(tours, costs):
    for k in range(num_robots):
        for i in range(len(tours[k]) - 1):
            a = tours[k][i]
            b = tours[k][i+1]
            pheromones[a][b] += 1.0 / costs[k]
            pheromones[b][a] += 1.0 / costs[k]  # because it's symmetrical
    pheromones *= (1 - rho)  # Evaporation

def ant_colony_optimization():
    best_tours = None
    best_cost = float('inf')
    
    for iteration in range(num_iterations):
        tours = [[] for _ in range(num_robots)]
        tour_costs = [0] * num_robots
        for ant in range(num_ants):
            start_points = list(range(num_robots))
            for i in range(num_robots):
                current_city = start_points[i]
                tours[i].append(current_city)
                unvisited = set(range(num_cities)) - set(start_points)
                
                while unvisited:
                    next_city = choose_next_city(current_city, list(unwanted))
                    tours[i].append(next_city)
                    tour_costs[i] += distance_matrix[current_city][next_city]
                    current_city = next_city
                    unwanted.remove(next_city)
                
                # Return to start point
                tours[i].append(start_points[i])
                tour_costs[i] += distance_matrix[current_city][start_points[i]]
            
            if sum(tour_costs) < best_cost:
                best_cost = sum(tour_costs)
                best_tours = [tour[:] for tour in tours]
        
        update_pheromones(tours, tour_costs)
    
    return best_tours, best_cost

best_tours, best_total_cost = ant_colony_optimization()

# Output robot tours and costs
print(f"Overall Total Travel Cost: {best_total_cost}")
for idx, tour in enumerate(best_tours):
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")