import numpy as np
import random

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

depots = list(range(8))  # Robots 0-7 correspond to Depot 0-7 respectively
num_cities = len(coordinates)

# Parameters
alpha = 1.0        # Influence of pheromone
beta = 2.0         # Influence of heuristic (inverse of distance)
rho = 0.5          # Evaporation rate
antnum = 32        # Number of ants
init_pheromone = 1.0
cyclenum = 100     # For simplicity, let's assume a fixed number of cycles

# Function to calculate Euclidean distance between two city indices
def distance(i, j):
    return np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Initialize pheromone levels
pheromones = np.full((num_cities, num_cities), init_pheromone)

# Main ACO Algorithm function
def aco_algorithm():
    best_tours = {depot: [] for depot in depots}
    best_costs = {depot: float('inf') for depot in depots}
    global_best_cost = float('inf')
    global_best_tours = None
    
    for cycle in range(cyclenum):
        # Loop over each depot (robot)
        for depot in depots:
            local_best_tour = None
            local_best_cost = float('inf')
            
            # Each ant constructs a tour
            for _ in range(antnum):
                tour = [depot]
                current_city = depot
                unvisited = set(range(num_cities)) - set([depot])
                
                # Construct the tour for the ant
                while len(unvisited) > 0:
                    choices = [(j, (pheromones[current_city][j] ** alpha) * ((1 / distance(current_city, j)) ** beta)) for j in unvisited]
                    probs = [c[1] for c in choices]
                    sum_probs = sum(probs)
                    probs = [p / sum_probs for p in probs]
                    next_city = np.random.choice([c[0] for c in choices], p=probs)
                    
                    tour.append(next_city)
                    current_city = next_city
                    unvisited.remove(current_city)

                # Close the tour
                tour.append(depot)

                # Calculate the cost of this tour
                tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
                
                # Check if it's the best found for this depot
                if tour_cost < local_best_cost:
                    local_best_tour = tour
                    local_best_cost = tour_cost

            # Update local depot's best tour
            if local_best_cost < best_costs[depot]:
                best_costs[depot] = local_best_cost
                best_tours[depot] = local_best_tour

            # Trail Update
            pheromones *= (1 - rho)
            for i in range(len(local_best_tour) - 1):
                pheromones[local_best_tour[i]][local_best_tour[i + 1]] += 1 / local_best_cost
        
        current_cost_sum = sum(best_costs.values())
        if current_cost_sum < global_best_cost:
            global_best_cost = current_cost_sum
            global_best_tours = best_tours.copy()

    return global_best_tours, best_costs, global_best_cost

# Execute the algorithm
best_tours, best_costs, global_best_cost = aco_algorithm()

# Output the result
for robot, tour in best_tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {best_costs[robot]}")

print(f"Overall Total Travel Cost: {global_best_cost}")