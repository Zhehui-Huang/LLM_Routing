import numpy as np
import math
import random

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52),  # Depot 0, Depot 1
    (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Compute distance matrix
num_cities = len(coordinates)
distance_matrix = [[math.dist(coordinates[i], coordinates[j]) if i != j else float('inf') for j in range(num_cities)] for i in range(num_cities)]

# Ant Colony Optimization parameters
ant_num = 10  # Number of artificial ants
cycles_num = 100  # Number of cycles
alpha = 1  # Influence of pheromone
beta = 5  # Influence of heuristic (inverse of distance)
evaporation_rate = 0.5  # Pheromone evaporation rate
initial_pheromone = 1.0 / num_cities  # Initial pheromone level

# Pheromone matrix initialization
pheromone_levels = [[initial_pheromone for _ in range(num_cities)] for _ in range(num_cities)]

# Simulation function
def aco_simulation():
    best_cost = float('inf')
    best_tours = None

    for cycle in range(cycles_num):
        tours = []
        costs = []

        for _ in range(ant_num):
            # Initialize tours starting at their respective depots
            tour = [[0], [1]]  # Tour for robots starting at depots 0 and 1
            
            for t_idx in range(2):
                while len(tour[t_idx]) < (num_cities // 2 + int(t_idx < num_cities % 2)):
                    last_city = tour[t_idx][-1]
                    probabilities = []

                    for j in range(num_cities):
                        if j not in tour[0] and j not in tour[1] and last_city != j:  # City not yet visited and not the same
                            heuristic = 1 / distance_matrix[last_city][j]
                            probability = (pheromone_levels[last_city][j] ** alpha) * (heuristic ** beta)
                            probabilities.append((probability, j))

                    total = sum(prob[0] for prob in probabilities)
                    probabilities = [(prob[0] / total, prob[1]) for prob in probabilities]
                    
                    next_city = random.choices([p[1] for p in probabilities], weights=[p[0] for p in probabilities], k=1)[0]
                    tour[t_idx].append(next_city)

            # Complete the tour by returning to respective depots
            tour[0].append(0)
            tour[1].append(1)

            tours.append(tour)
            total_cost = sum(calculate_travel_cost(t) for t in tour)
            costs.append(total_cost)
        
        # Update pheromones
        pheromone_levels = [[(1 - evaporation_rate) * pheromone_levels[i][j] for j in range(num_cities)] for i in range(num_cities)]
        for tour, cost in zip(tours, costs):
            for route in tour:
                for i in range(len(route) - 1):
                    pheromone_levels[route[i]][route[i + 1]] += 1 / cost  # Deposit pheromone

        min_cost_idx = np.argmin(costs)
        if costs[min_cost_idx] < best_cost:
            best_cost = costs[min_cost_idx]
            best_tours = tours[min_cost_idx]

    return best_tours, best_cost

# Execute the simulation
tours, total_cost = aco_simulation()

# Output results
for i, tour in enumerate(tours):
    tour_cost = calculate_travel_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")
print(f"Overall Total Travel Cost: {total_cost}")