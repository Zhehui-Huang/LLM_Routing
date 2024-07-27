import numpy as np
from scipy.spatial.distance import euclidean

def calc_distance(city1, city2):
    return euclidean(city1, city2)

def initialize_pheromone(num_cities):
    return np.ones((num_cities, num_cities)) * 0.1

def evaporate_pheromone(pheromone_matrix, evaporation_rate):
    return pheromone_matrix * (1 - evaporation_rate)

def update_pheromone(pheromone_matrix, tours, costs):
    for k, tour in enumerate(tours):
        for i in range(len(tour) - 1):
            a, b = tour[i], tour[i + 1]
            additional_pheromone = 1 / costs[k]
            pheromone_matrix[a][b] += additional_pheromone
            pheromone_matrix[b][a] += additional_pheromone  # Symmetric update
    return pheromone_matrix

def generate_tour(pheromone_matrix, distances, desirability, alpha, beta, depot, nodes):
    tour = [depot]
    current = depot
    vis_nodes = set(nodes)

    while vis_nodes:
        probabilities = []
        for j in vis_nodes:
            probabilities.append((pheromone_matrix[current][j] ** alpha) * (desirability[current][j] ** beta))
        
        probabilities = np.array(probabilities) / sum(probabilities)
        next_city = np.random.choice(list(vis_nodes), p=probabilities)
        tour.append(next_city)
        vis_nodes.remove(next_city)
        current = next_city

    tour.append(depot)  # Return to depot
    return tour

def calculate_total_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Given cities and their coordinates
cities = {...}  # As defined

# Covert city coordinates to distance matrix
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calc_distance(cities[i], cities[j])

# Ant Colony Optimization parameters
alpha = 1
beta = 1
evaporation_rate = 0.5
num_iterations = 100
num_ants = 20

# Robotic information
robot_start_depot = {0: 0, 1: 1, 2: 2, 3: 3}

# Partition out cities under corresponding depots, simplified partition for illustration
robot_cities = {
    0: list(range(4, 10)),
    1: list(range(10, 14)),
    2: list(range(14, 18)),
    3: list(range(18, 22))
}

overall_cost = 0
for robot_id, depot in robot_start_depot.items():
    cities_per_robot = robot_cities[robot_id] + [depot]
    num_local_cities = len(cities_per_robot)
    pheromone = initialize_pheromone(num_local_cities)
    desirability = 1 / distances

    best_cost = float('inf')
    best_tour = None

    for _ in range(num_iterations):
        local_tours = []
        local_costs = []
        for _ in range(num_ants):
            tour = generate_tour(pheromone, distances, desirability, alpha, beta, depot, cities_per_robot)
            cost = calculate_total_cost(tour, distances)
            local_tours.append(tour)
            local_costs.append(cost)
            
            if cost < best_cost:
                best_cost = cost
                best_tour = tour

        pheromone = evaporate_pheromone(pheromone, evaporation_rate)
        pheromone = update_pheromone(pheromone, local_tours, local_costs)
    
    overall_cost += best_cost
    print(f"Robot {robot_id} Tour: {best_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {best_cost}")

print(f"Overall Total Travel Cost: {overall Civil}")