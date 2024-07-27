import numpy as np
import math

# Coordinates of the cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots and their respective start/end depots
depots = [0, 1, 2, 3]

# Parameters for ACO
antnum = 10
cycles = 100
alpha = 1.0
beta = 5.0
rho = 0.1
init_phero = 1.0

# Distance matrix calculation
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

distance_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initial pheromone levels
pheromone = [[init_phero for _ in range(len(coordinates))] for _ in range(len(coordinates))]

# Heuristic (visibility)
visibility = [[1 / distance_matrix[i][j] if i != j else 0 for j in range(len(coordinates))] for i in range(len(coordinates))]

def choose_next_city(current, allowed, pheromone, visibility):
    denominators = sum(pheromone[current][j] ** alpha * visibility[current][j] ** beta for j in allowed)
    probabilities = [(pheromone[current][j] ** alpha * visibility[current][j] ** beta) / denominators for j in allowed]
    return np.random.choice(allowed, p=probabilities)
    
def update_pheromone(pheromone, tours, costs):
    for i in range(len(pheromone)):
        for j in range(len(pheromone)):
            pheromone[i][j] *= (1 - rho)  # Evaporation
        
    for tour_idx, tour in enumerate(tours):
        contribution = 1 / costs[tour_idx]
        for i in range(len(tour) - 1):
            pheromone[tour[i]][tour[i+1]] += contribution

def ant_colony_optimization():
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(cycles):
        all_tours = []
        all_costs = []
        
        for depot in depots:
            for _ in range(int(antnum / len(depots))):  # ants per depot
                tour = [depot]
                unvisited = set(range(len(coordinates))) - {depot}
                
                while unvisited:
                    current_city = tour[-1]
                    if unvisited:
                        next_city = choose_next_city(current_city, list(unvisited), pheromone, visibility)
                        tour.append(next_city)
                        unvisited.remove(next_city)
                
                tour.append(depot)  # Return to depot
                tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
                
                all_tours.append(tour)
                all_costs.append(tour_cost)
                
        current_best_cost = min(all_costs)
        if current_best_cost < best_cost:
            best_cost = current_best_cost
            best_solution = all_tours[all_costs.index(current_best_cost)]
        
        update_pheromone(pheromone, all_tours, all_costs)
    
    return best_solution, best_cost

solution, total_cost = ant_colony_optimization()
print(f"Best Solution Tour: {solution}")
print(f"Best Solution Total Cost: {total_cost}")