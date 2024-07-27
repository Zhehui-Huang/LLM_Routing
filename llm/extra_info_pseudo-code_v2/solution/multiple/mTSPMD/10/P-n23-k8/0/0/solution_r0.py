import numpy as np
from scipy.spatial import distance_matrix

# Define cities and their coordinates
coordinates = np.array([
    (30,40),(37,52),(49,49),(52,64),(31,62),(52,33),
    (42,41),(52,41),(57,58),(62,42),(42,57),(27,68),
    (43,67),(58,48),(58,27),(37,69),(38,46),(61,33),
    (62,63),(63,69),(45,35),(32,39),(56,37)
])

# Calculate distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Defining the robots
num_robots = 8
starting_depot = list(range(num_robots))

# ACO parameters
num_ants = 40
num_generations = 100
alpha = 1.0
beta = 2.0
rho = 0.1
init_pheromone = 1.0 / len(coordinates)

# Initialize pheromone levels
pheromones = np.full((len(coordinates), len(coordinates)), init_pheromone)

def calculate_transition_probabilities(current_city, pheromones, dist_matrix, visited):
    probs = np.zeros(len(coordinates))
    unvisited = [i for i in range(len(coordinates)) if i not in visited]
    
    if not unvisited:  # no unvisited cities left
        return probs
    
    pheromone_current = pheromones[current_city][unvisited]
    dist_current = dist_matrix[current_city][unvisited]
    heuristic = 1 / dist_current
    numerator = pheromone_current**alpha * heuristic**beta
    
    probs[unvisited] = numerator / np.sum(numerator)
    return probs

# Run simulation
best_tours = [[] for _ in range(num_robots)]
best_costs = [np.inf for _ in range(num_robots)]
best_overall_cost = np.inf

for generation in range(num_generations):
    for ant in range(num_ants):
        tours = [[] for _ in range(num_robots)]
        costs = [0.0 for _ in range(num_robots)]
        for robot in range(num_robots):
            current_city = starting_depot[robot]
            tour = [current_city]
            visited = set(tour)
            while len(tour) < (len(coordinates) + 1) // num_robots:
                probabilities = calculate_transition_probabilities(current_city, pheromones, dist_matrix, visited)
                next_city = np.random.choice(len(coordinates), p=probabilities)
                tour.append(next_city)
                visited.add(next_city)
                costs[robot] += dist_matrix[current_city][next_city]
                current_city = next_city
            
            # Returning to starting depot
            tour.append(starting_depot[robot])
            costs[robot] += dist_matrix[current_city][starting_depot[robot]]
            tours[robot] = tour
        
        # Pheromone update
        pheromones *= (1 - rho)  # evaporation
        for robot in range(num_robots):
            for city_idx in range(len(tours[robot]) - 1):
                i, j = tours[robot][city_idx], tours[robot][city_idx + 1]
                pheromones[i][j] += 1.0 / costs[robot]  # pheromone deposit
        
        # Track best tours
        current_total_cost = np.sum(costs)
        if current_total_cost < best_overall_cost:
            best_tours = tours
            best_costs = costs
            best_overall_cost = current_total_cost

# Results output
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {best_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {best_costs[robot]}")
print(f"Overall Total Travel Cost: {best_overallolew_cost}")