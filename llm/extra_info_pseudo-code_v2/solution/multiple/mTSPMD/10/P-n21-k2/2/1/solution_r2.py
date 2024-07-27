import numpy as np

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

num_cities = len(coordinates)
distances = np.array([[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)])

def initialize_pheromone(level, num_cities):
    return np.full((num_cities, num_cities), level)

def calculate_probabilities(pheromone, heuristics, alpha, beta, mask):
    probabilities = (pheromone ** alpha) * (heuristics ** beta)
    probabilities *= mask  # Apply mask
    row_sums = probabilities.sum(axis=1, keepdims=True)
    # Avoid division by zero
    probabilities /= np.where(row_sums == 0, 1, row_sums)
    return probabilities

def update_pheromone(pheromone, tours, costs, rho, Q):
    pheromone *= (1 - rho)  # Evaporation
    for tour, cost in zip(tours, costs):
        deposit = Q / cost
        for i in range(len(tour) - 1):
            pheromone[tour[i], tour[i + 1]] += deposit
            pheromone[tour[i + 1], tour[i]] += deposit  # since it's symmetric
    return pheromone

def aco_solve_tsp(distances, num_ants, num_iterations, alpha, beta, rho, Q, initial_pheromone):
    num_cities = distances.shape[0]
    pheromone = initialize_pheromone(initial_pheromone, num_cities)
    heuristics = 1 / (distances + 1e-5)  # Inverse of distance
    
    best_tour = None
    best_cost = np.inf
    
    for iteration in range(num_iterations):
        tours = []
        costs = []
        
        for _ in range(num_ants):
            tour = [np.random.randint(num_cities)]
            for _ in range(num_cities - 1):
                current = tour[-1]
                mask = np.zeros(num_cities)
                mask[tour] = 1  # 1 means not allowed
                probabilities = calculate_probabilities(pheromone[current], heuristics[current], alpha, beta, 1 - mask)
                next_city = np.random.choice(num_cities, p=probabilities)
                tour.append(next_city)
            
            tour.append(tour[0])  # Close the tour
            tour_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
            tours.append(tour)
            costs.append(tour_cost)
            
            if tour_cost < best_cost:
                best_cost = tour_cost
                best_tour = tour
        
        pheromone = update_pheromone(pheromone, tours, costs, rho, Q)
        
    return best_tour, best_cost

best_tour, best_cost = aco_solve_tsp(distances, num_ants=10, num_iterations=100, alpha=1, beta=5, rho=0.1, Q=100, initial_pheromone=1.0)

print("Best Tour:", best_tour)
print("Best Tour Cost:", best_cost)