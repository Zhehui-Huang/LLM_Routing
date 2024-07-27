import numpy as np
import random

# City coordinates
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters
antnum = 10
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 5.0
rho = 0.5

# Number of cities and depots
num_cities = len(city_coords)
depots = [0, 1]

# Initialize pheromones
pheromones = np.full((num_cities, num_cities), inittrail, dtype=float)

# Distance matrix
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = np.linalg.norm(np.array(city_coords[i]) - np.array(city_coords[j]))

# Inverse of distances (heuristic info)
eta = np.zeros((num_cities, num_cities)) + 0.0001  # adding a small value to avoid division by zero
np.fill_diagonal(eta, 0)
eta = 1.0 / (distances + eta)

# Main optimization loop
def ant_colony_optimization():
    best_tours = {depot: None for depot in depots}
    best_costs = {depot: float('inf') for depot in depots}

    for _ in range(cyclenum):
        tours = {depot: [] for depot in depots}
        tour_costs = {depot: [] for depot in depots}
        
        for ant in range(antnum):
            # Split ants evenly amongst depots
            depot = depots[ant % len(depots)]
            tour = [depot]
            allowed = list(range(num_cities))
            allowed.remove(depot)
            
            current = depot
            while allowed:
                probabilities = (pheromones[current, allowed] ** alpha) * (eta[current, allowed] ** beta)
                probabilities /= probabilities.sum()
                next_city = np.random.choice(allowed, p=probabilities)
                tour.append(next_city)
                allowed.remove(next_city)
                current = next_city
            
            tour.append(depot)  # Return to depot
            cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
            
            tours[depot].append(tour)
            tour_costs[depot].append(cost)
        
        # Update best tours and costs
        for depot in depots:
            min_cost = min(tour_costs[depot])
            min_index = tour_costs[depot].index(min_cost)
            if min_cost < best_costs[depot]:
                best_costs[depot] = min_cost
                best_tours[depot] = tours[depot][min_index]
        
        # Update pheromones
        pheromones *= (1 - rho)
        for depot in depots:
            for tour, cost in zip(tours[depot], tour_costs[depot]):
                for i in range(len(tour) - 1):
                    pheromones[tour[i], tour[i + 1]] += 1 / cost
    
    return best_tours, best_costs

best_tours, best_costs = ant_colony_optimization()
overall_cost = sum(best_costs.values())

# Output the results
for robot_id, depot in enumerate(depots):
    print(f"Robot {robot_id} Tour: {best_tours[depot]}")
    print(f"Robot {robot_id} Total Travel Cost: {best_costs[depot]}")

print(f"Overall Total Travel Cost: {overall_cost}")