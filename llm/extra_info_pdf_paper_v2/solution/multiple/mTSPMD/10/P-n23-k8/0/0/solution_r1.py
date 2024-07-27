import numpy as np
from scipy.spatial import distance

# Define the cities' coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots and their depots
depots = [0, 1, 2, 3, 4, 5, 6, 7]

# Compute distance matrix using Euclidean distance
def compute_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = distance.euclidean(cities[i], cities[j])
    return distance_matrix

distance_matrix = compute_distance_matrix(cities)

# Parameters for Ant Colony
num_ants = 40
num_iterations = 100
alpha = 1  # influence of pheromone
beta = 5  # influence of heuristic information (1/distance)
evaporation_rate = 0.5
pheromone_deposit_amount = 1
initial_pheromone = 1

# Initialize pheromone levels
pheromones = np.ones_like(distance_matrix) * initial_pheromone

def ant_colony_optimization():
    global pheromones
    best_cost = np.inf
    best_solution = None

    for iteration in range(num_iterations):
        for ant in range(num_ants):
            solution = {}
            solution_cost = {}
            total_cost = 0
            
            for depot in depots:
                current_city = depot
                tour = [current_city]
                tour_cost = 0
                while len(tour) < (len(cities) // len(depots)) + 1:
                    choices = list(set(range(len(cities))) - set(tour))
                    choice_probs = [pheromones[current_city][next_city]**alpha * (1 / distance_matrix[current_city][next_city])**beta for next_city in choices]
                    choice_probs /= np.sum(choice_probs)
                    next_city = np.random.choice(choices, p=choice_probs)
                    tour.append(next_city)
                    tour_cost += distance_matrix[current_city][next_city]
                    current_city = next_city

                tour.append(depot)  # return to starting depot
                tour_cost += distance_matrix[current_city][depot]
                solution[depot] = tour
                solution_cost[depot] = tour_cost
                total_cost += tour_cost

            # Update pheromones (evaporation and deposition)
            pheromones *= evaporation_rate
            for tour, cost in solution.items():
                for i in range(len(tour) - 1):
                    pheromones[tour[i]][tour[i+1]] += pheromone_deposit_amount / solution_cost[tour]

            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = solution

    return best_solution, best_cost

best_solution, best_cost = ant_colony_optimization()

# Output results
print(f"Overall Total Travel Cost: {best_cost}")
for depot, tour in best_solution.items():
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    print(f"Robot {depot} Tour: {tour}")
    print(f"Robot {depot} Total Travel Travel Cost: {cost}")