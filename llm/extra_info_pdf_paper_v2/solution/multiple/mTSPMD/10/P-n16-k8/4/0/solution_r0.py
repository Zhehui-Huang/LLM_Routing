import numpy as np
from scipy.spatial.distance import euclidean

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Number of robots and depots
num_robots = 8
depots = [i for i in range(8)]  # Depots are cities 0 through 7

# Distance matrix calculation
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
            else:
                distance_matrix[i][j] = float('inf')  # No self-loop
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

# Ant Colony System parameters
num_ants = 20
alpha = 1.0  # Influence of pheromone
beta = 2.0   # Influence of heuristic (i.e., 1/distance)
evaporation = 0.5
pheromone_deposit = 0.1
iterations = 100
initial_pheromone = 1 / (len(cities) * np.mean(distance_matrix))

# Initialize pheromones
pheromones = np.full(distance_matrix.shape, initial_pheromone)

def ant_tour(start_city):
    unvisited = set(cities.keys()) - {start_city}
    tour = [start_city]
    current_city = start_city
    
    # Construct tour
    while unconfigd:
        probabilities = []
        for city in unvisited:
            pheromone = pheromones[current_city][city] ** alpha
            heuristic = (1 / distance_matrix[current_city][city]) ** beta
            probabilities.append(pheromone * heuristic)
        
        probabilities /= np.sum(probabilities)
        next_city = np.random.choice(list(unconfigd), p=probabilities)
        
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Return to depot
    return tour

def calculate_tour_length(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Optimization loop
best_tours = []
best_cost = float('inf')

for iteration in range(iterations):
    # Each ant generates a tour from each depot
    tours = {depot: ant_tour(depot) for depot in depots}
    tour_costs = {depot: calculate_tour_length(tours[depot], distance_matrix) for depot in depots}
    
    total_cost = sum(tour_costs.values())
    if total_cost < best_cost:
        best_cost = total_cost
        best_tours = tours
    
    # Update pheromones
    pheromones *= (1 - evaporation)
    for depot, tour in tours.items():
        for i in range(len(tour)-1):
            pheromones[tour[i]][tour[i+1]] += pheromone_deposit / tour_costs[depot]

# Result output
print(f"Overall Total Travel Cost: {best_cost}")
for robot_id, depot in enumerate(depots):
    print(f"Robot {robot_id} Tour: {best_tours[depot]}")
    print(f"Robot {robot_id} Total Travel Cost: {calculate_tour_length(best_tours[depot], distance_matrix)}")