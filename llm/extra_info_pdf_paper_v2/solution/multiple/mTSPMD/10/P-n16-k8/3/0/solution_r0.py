import numpy as np
import math

# Number of cities and coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Number of robots and their depots
robot_depots = [0, 1, 2, 3, 4, 5, 6, 7]

# Distance Calculation
def calculate_distances(coords):
    num_cities = len(coords)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i, j] = math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
            else:
                distances[i, j] = float('inf')  # No self-loops
    return distances

# Initialize distances
distances = calculate_distances(coordinates)

# Ant Colony Optimization Parameters
num_ants = 20
num_iterations = 100
pheromone_evaporation_rate = 0.5
alpha = 1  # Influence of pheromone
beta = 2  # Influence of heuristic information (1/distance)
initial_pheromone = 1.0

# Pheromone matrix
pheromone_matrix = np.full((len(coordinates), len(coordinates)), initial_pheromone)

# ACS Algorithm
def ant_colony_optimization():
    best_tour_length = float('inf')
    best_tour = None
    for iteration in range(num_iterations):
        for ant in range(num_ants):
            tours = []
            tour_costs = []
            for depot in robot_depots:
                tour = [depot]
                current_city = depot
                while len(tour) < len(coordinates) // len(robot_depots) + 1:
                    probabilities = []
                    for next_city in range(len(coordinates)):
                        if next_city not in tour:
                            trail_level = math.pow(pheromone_matrix[current_city][next_city], alpha)
                            visibility = math.pow(1.0 / distances[current_city][next_city], beta)
                            probabilities.append(trail_level * visibility)
                        else:
                            probabilities.append(0)
                    probabilities /= np.sum(probabilities)
                    next_city = np.random.choice(range(len(coordinates)), p=probabilities)
                    tour.append(next_city)
                    current_city = next_city
                tour.append(depot)  # Return to the depot
                tours.append(tour)
                tour_costs.append(sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1)))
            
            # Update pheromones locally
            for i, tour in enumerate(tours):
                for j in range(len(tour) - 1):
                    pheromone_matrix[tour[j]][tour[j+1]] *= (1 - pheromone_evaporation_rate)
                    pheromone_matrix[tour[j]][tour[j+1]] += pheromone_evaporation_rate / tour_costs[i]
            
            # Check for the best tour
            current_tour_length = sum(tour_costs)
            if current_tour_length < best_tour_length:
                best_tour_length = current_tour_length
                best_tour = tours.copy()

    return best_tour, best_tour_length

# Run the optimization
best_tour_solution, total_cost = ant_colony_optimization()

# Output the solution
for i, tour in enumerate(best_tour_solution):
    print(f"Robot {robot_depots[i]} Tour: {tour}")
    print(f"Robot {robot_depots[i]} Total Travel Cost: {sum(distances[tour[j]][tour[j+1]] for j in range(len(tour)-1))}")

print(f"Overall Total Travel Cost: {total_cost}")