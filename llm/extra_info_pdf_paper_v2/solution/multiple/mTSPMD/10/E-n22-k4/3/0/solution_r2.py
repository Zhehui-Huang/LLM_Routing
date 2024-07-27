import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Calculating distances matrix
n_cities = len(cities)
distances = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i, j] = euclidean(cities[i], cities[j])
        else:
            distances[i, j] = float('inf')

# Ant Colony Optimization (ACO) parameters
n_ants = 20
n_best = 5
n_iterations = 100
decay = 0.1
alpha = 1.0
beta = 2.0

# Initialize pheromones
pheromones = np.ones_like(distances)

def aco_solve_tsp(start, cities):
    best_cost = np.inf
    best_tour = None

    for _ in range(n_iterations):
        costs = []
        tours = []
        for __ in range(n_ants):
            # Build tours
            tour = [start]
            unvisited = set(cities) - {start}
            
            while unvisited:
                current = tour[-1]
                probabilities = []
                
                for next_city in unvisited:
                    tau = pheromones[current][next_city] ** alpha
                    eta = (1.0 / distances[current][next_city]) ** beta
                    probabilities.append(tau * eta)
                
                probabilities /= np.sum(probabilities)
                next_city = np.random.choice(list(unvisited), p=probabilities)
                tour.append(next_city)
                unvisited.remove(next_city)
            
            tour.append(start) # return to start
            tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            costs.append(tour_cost)
            tours.append(tour)
        
        # Update best tour and cost
        for cost, tour in zip(costs, tours):
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
        
        # Update pheromones
        pheromones *= (1 - decay)
        for tour, cost in zip(tours, costs):
            for i in range(len(tour) - 1):
                pheromones[tour[i]][tour[i+1]] += 1.0 / cost
    
    return best_tour, best_cost

# Run ACO for each robot starting at its depot
depots = [0, 1, 2, 3]
tours = []
total_cost = 0

for depot in dep';

# Execute the tours and print the results
for i, (tour, cost) in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")