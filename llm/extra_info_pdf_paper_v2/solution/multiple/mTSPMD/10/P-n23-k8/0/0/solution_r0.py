import numpy as np
from scipy.spatial.distance import euclidean
from math import inf

# Define the cities' coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots and their depots
robots = list(range(8))
depots = robots[:8]  # Robots start and end at depots with the same index

# Compute distance matrix
def compute_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

distance_matrix = compute_distance_matrix(cities)

# Ant Colony Optimization parameters
num_ants = 40
num_iterations = 100
alpha = 1
beta = 2
evaporation = 0.5
pheromone_deposit = 10

# Initialize pheromones
pheromones = np.ones_like(distance_matrix)

def ant_colony_optimization():
    best_cost = inf
    best_solution = None
    
    for iteration in range(num_iterations):
        all_solutions = []
        all_costs = []
        for ant in range(num_ants):
            tours = []
            costs = []
            remaining_cities = set(range(len(cities))) - set(depots)
            for depot in depots:
                tour = [depot]
                current = depot
                while remaining_cities:
                    probabilities = []
                    for j in remaining_cities:
                        trail = pheromones[current][j] ** alpha * (1.0 / distance_matrix[current][j]) ** beta
                        probabilities.append(trail)
                    probabilities = np.array(probabilities)
                    probabilities /= probabilities.sum()
                    next_city = np.random.choice(list(remaining_cities), p=probabilities)
                    tour.append(next_city)
                    remaining_cities.remove(next_city)
                    current = next_city
                tour.append(depot)  # return to depot
                tours.append(tour)
                cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
                costs.append(cost)
            
            total_cost = sum(costs)
            all_solutions.append(tours)
            all_costs.append(total_cost)
            
            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = tours
            
        # Update pheromones
        pheromones *= evaporation
        for tours, cost in zip(all_solutions, all_costs):
            deposit = pheromone_deposit / cost
            for tour in tours:
                for i in range(len(tour) - 1):
                    pheromones[tour[i]][tour[i+1]] += deposit
            
    return best_solution, best_cost

best_solution, best_cost = ant_colony_optimization()

# Output results
print(f"Overall Total Travel Cost: {best_cost:.2f}")
for idx, tour in enumerate(best_solution):
    print(f"Robot {idx} Tour: {tour}")
    cost = sum(distance_box[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")