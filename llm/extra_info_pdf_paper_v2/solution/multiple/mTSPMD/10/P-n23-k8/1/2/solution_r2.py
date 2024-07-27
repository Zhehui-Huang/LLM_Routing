import numpy as np
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def initialize_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

def initialize_pheromones(num_cities, initial_pheromone):
    return np.full((num_cities, num_cities), initial_pheromone)

def choose_next_city(availability, pheromones, heuristic, alpha, beta):
    total = 0
    probabilities = np.zeros(len(availability))
    for i in range(len(availability)):
        if availability[i]:
            probabilities[i] = pheromones[i] ** alpha * (1 / heuristic[i]) ** beta
            total += probabilities[i]
    
    probabilities = probabilities / total
    return np.random.choice(len(probabilities), p=probabilities)

def update_pheromone(pheromones, tours, costs, evaporation_rate):
    n = pheromones.shape[0]
    for i in range(n):
        for j in range(n):
            pheromones[i][j] *= (1 - evaporation_rate)
    
    for idx, tour in enumerate(tours):
        contribution = 1.0 / costs[idx]
        for i in range(1, len(tour)):
            pheromones[tour[i-1]][tour[i]] += contribution
            pheromones[tour[i]][tour[i-1]] += contribution  # Symmetrical update

def ant_colony_optimization(cities, num_robots, num_ants, num_iterations, alpha, beta, evaporation_rate, initial_pheromone):
    num_cities = len(cities)
    distance_matrix = initialize_distance_matrix(cities)
    pheromones = initialize_pheromones(num_cities, initial_pheromone)
    
    best_solution = None
    global_best_cost = float('inf')
    
    for iteration in range(num_iterations):
        solutions = []
        costs = []
        
        for _ in range(num_ants):
            tours = [[] for _ in range(num_robots)]
            next_cities = list(range(num_robots))
            
            for tour_id in range(num_robots):
                tours[tour_id].append(next_cities[tour_id])
            
            for _ in range(num_cities - num_robots):
                for robot_index in range(num_robots):
                    current_city = tours[robot_index][-1]
                    availability = [i not in tours[robot_index] for i in range(num_cities)]
                    next_city = choose_next_city(availability, pheromones[current_city], distance_matrix[current_city], alpha, beta)
                    tours[robot_index].append(next_city)
            
            # Closing the tours by returning to their respective depots
            for robot_index in range(num_robots):
                tours[robot_index].append(tours[robot_index][0])
            
            # Calculate cost of the tours
            tour_costs = []
            for tour in tours:
                cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
                tour_costs.append(cost)
            
            total_cost = sum(tour_costs)
            solutions.append(tours)
            costs.append(tour_costs)
            
            if total_cost < global_best_cost:
                global_best_cost = total_cost
                best_solution = tours
        
        # Pheromone update
        update_pheromone(pheromones, solutions, costs, evaporation_rate)
    
    return best_solution, global_best_cost

# Define the cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Ant Colony Optimization Parameters
num_robots = 8
num_ants = 10
num_iterations = 100
alpha = 1
beta = 2
evaporation_rate = 0.1
initial_pheromone = 0.1

best_solution, best_cost = ant_colony_optimization(cities, num_robots, num_ants, num_iterations, alpha, bet=<|vq_6548|>.
    
for idx, tour in enumerate(best_solution):
    print(f'Robot {idx} Tour: {tour}')
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f'Robot {idx} Total Travel Cost: {tour_cost}')

print(f'Overall Total Travel Cost: {best_cost}')