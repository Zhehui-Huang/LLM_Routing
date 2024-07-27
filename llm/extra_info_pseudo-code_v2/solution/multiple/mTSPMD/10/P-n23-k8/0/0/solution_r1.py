import numpy as np
from scipy.spatial.distance import cdist

# City coordinates and depot setups
coordinates = np.array([
    (30,40), (37,52), (49,49), (52,64), (31,62), (52,33),
    (42,41), (52,41), (57,58), (62,42), (42,57), (27,68),
    (43,67), (58,48), (58,27), (37,69), (38,46), (61,33),
    (62,63), (63,69), (45,35), (32,39), (56,37)
])

# Number of robots and their starting depots
num_robots = 8
depots = list(range(num_robots))

# Distance matrix computation
dist_matrix = cdist(coordinates, coordinates)

# ACO Parameters
num_ants = 40
num_generations = 100
alpha = 1.0
beta = 2.0
rho = 0.1
initial_pheromone = 1 / len(coordinates)

# Initialize pheromone matrix
pheromones = np.full_like(dist_matrix, fill_value=initial_pheromone)

def select_next_city(current_city, pheromone, heur, visited):
    probs = np.zeros(len(coordinates))
    mask = np.ones(len(coordinates), dtype=bool)
    mask[list(visited)] = False
    probs[mask] = pheromone[current_city][mask] ** alpha * (1 / heur[current_city][mask]) ** beta
    total_prob = np.sum(probs)
    if total_prob == 0:  # prevent division by zero
        return np.random.choice(np.where(mask)[0])
    return np.random.choice(len(coordinates), p=probs / total_prob)

# Simulation
best_solution = None
best_cost = np.inf

for generation in range(num_generations):
    for ant in range(num_ants):
        all_tours = []
        all_costs = []
        
        for robot in range(num_robots):
            current_city = depots[robot]
            tour = [current_city]
            visited = set(tour)
            
            while len(visited) < len(coordinates):
                next_city = select_next_city(current_city, pheromones, dist_matrix, visited)
                if next_city in depots and next_city != current_city:  # enforce a valid return to depot
                    break
                tour.append(next_city)
                visited.add(next_city)
                current_city = next_city
            
            tour.append(depots[robot])  # Return to depot
            all_tours.append(tour)
            tour_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
            all_costs.append(tour_cost)
        
        # Pheromone update
        pheromones *= (1 - rho)
        for robot, tour in enumerate(all_tours):
            for i in range(len(tour) - 1):
                pheromones[tour[i], tour[i+1]] += 1 / all_costs[robot]
        
        total_cost = sum(all_costs)
        if total_cost < best_cost:
            best_solution = all_tours
            best_cost = total_cost

# Output the best solution
overall_total_cost = sum(dist_matrix[solution[i], solution[i+1]] for solution in best_solution for i in range(len(solution)-1))
print("Best tours and costs for each robot:")

for i, solution in enumerate(best_solution):
    print(f"Robot {i} Tour: {solution}")
    print(f"Robot {i} Total Travel Cost: {dist_matrix[solution[i], solution[i+1]] for i in range(len(solution)-1)}")

print(f"Overall Total Travel Cost: {overall_total_cost}")