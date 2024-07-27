import numpy as np

# Coordinates given for each city including depots
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
               (45, 35)]

# Parameters for ACO
antnum = 20
cyclenum = 100
inittrail = 1.0
alpha = 1
beta = 5
rho = 0.5

# Derived parameters
num_cities = len(coordinates)

# Calculate all pairwise distances
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

distances = np.array([[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)])
pheromone = np.ones((num_cities, num_cities)) * inittrail
heuristic = 1 / (distances + 1e-10)

def aco_algorithm():
    best_cost = float('inf')
    best_tours = None
    
    for cycle in range(cyclenum):
        routes = []
        costs = []
        for ant in range(antnum):
            # Randomly decide starting depot
            start_depot = np.random.choice([0, 1])
            tour = [start_depot]
            current_city = start_depot
            unvisited = set(range(num_cities)) - {current_city}
            
            while unvisited:
                probabilities = np.zeros(num_cities)
                if current_city in [0, 1] and len(tour) > 1:
                    break
                for city in unvisited:
                    probabilities[city] = (pheromone[current_city][city] ** alpha) * (heuristic[current_city][city] ** beta)
                probabilities /= probabilities.sum()
                next_city = np.random.choice(num_clecties, p=probabilities)
                tour.append(next_city)
                unvisited.remove(next_city)
                current_city = next_city
            
            tour.append(start_depot)
            routes.append(tour)
            cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            costs.append(cost)
        
        # Find the best ant
        min_cost_index = np.argmin(costs)
        if costs[min_cost_index] < best_cost:
            best_cost = costs[min_cost_index]
            best_tours = routes[min_cost_index]
        
        # Update pheromone
        pheromone *= (1 - rho)
        for i, route in enumerate(routes):
            contribution = 1 / costs[i]
            for j in range(len(route) - 1):
                pheromone[route[j]][route[j+1]] += contribution
    
    return best_tours, best_cost

best_tours, best_cost = aco_algorithm()
print("Best tours:", best_tours)
print("Best total cost:", best_cost)