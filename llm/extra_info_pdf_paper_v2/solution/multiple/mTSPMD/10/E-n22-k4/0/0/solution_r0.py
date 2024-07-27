import numpy as np
import random

# Constants
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}
depots = [0, 1, 2, 3]
num_robots = 4

# Functions
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize pheromone levels and distance matrix
n_cities = len(cities)
pheromones = np.ones((n_cities, n_cities)) * 0.1
distances = np.array([[calculate_distance(i, j) for j in range(n_cities)] for i in range(n_cities)])

# Ant Colony Optimization parameters
n_ants = 20
alpha = 1.0  # influence of pheromone
beta = 2.0  # influence of heuristic information (1/distance)
evaporation_rate = 0.5
iterations = 100

# Amendment for depots (specializing ants)
initial_city_for_ants = [depots[i % num_robots] for i in range(n_ants)]

def update_pheromone(pheromone_matrix, ant_tours, quality):
    pheromone_matrix *= (1 - evaporation_rate)
    for tour, cost in zip(ant_tours, quality):
        for i in range(len(tour) - 1):
            pheromone_matrix[tour[i], tour[i+1]] += 1 / cost
            pheromone_matrix[tour[i+1], tour[i]] += 1 / cost

def ant_colony_optimization():
    best_tour = None
    best_cost = float('inf')
    for iteration in range(iterations):
        ant_tours = []
        costs = []
        for ant in range(n_ants):
            tour = [initial_city_for_ants[ant]]
            visited = set(tour)
            current_city = tour[0]
            while len(visited) < len(cities):
                probabilities = []
                for next_city in range(n_cities):
                    if next_city not in visited:
                        trail = pheromones[current_city, next_city] ** alpha
                        desirability = (1.0 / distances[current_city, next(self)) if distances[current_city, next_city] > 0 else 10e-6) ** beta
                        probabilities.append(trail * desirability)
                    else:
                        probabilities.append(0)
                probabilities = probabilities / np.sum(probabilities)
                next_city = np.random.choice(range(n_cities), p=probabilities)
                tour.append(next_city)
                visited.add(next_city)
                current_city = next_city
            tour.append(tour[0])  # return to depot
            ant_tours.append(tour)
            cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
            costs.append(cost)

        # Update pheromone paths
        update_pheromone(pheromones, ant_tours, costs)

        # Update best solution
        iteration_best_cost = min(costs)
        if iteration_best_cost < best_cost:
            best_cost = iteration_cost
            best_tour = ant_tours[np.argmin(costs)]
        
    return best_tour, best_cost

# Run the optimization
tour, cost = ant_colony_optimization()

# Output the result
print(f"Best Tour: {tour}")
print(f"Total Travel Cost: {cost}")