import numpy as np
import math

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Define the depots
depots = list(range(8))

# Constants for the ant colony algorithm
antnum = 20
cyclenum = 100
init_pheromone = 1.0
alpha = 1.0
beta = 5.0
rho = 0.1

# Calculate distance matrix
distances = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            distances[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
        else:
            distances[i][j] = float('inf')

# Initialize pheromone levels and heuristic information
pheromones = np.full((len(cities), len(cities)), init_pheromone)
heuristic = 1 / distances
heuristic[np.isinf(heuristic)] = 0 # Avoid division by zero in heuristic calculation

# Main Ant Colony Optimization algorithm
def ant_colony_optimization():
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(cyclenum):
        solutions = []
        costs = []
        
        for __ in range(antnum):
            tour, cost = create_tour()
            solutions.append(tour)
            costs.append(cost)
        
        # Update the best solution
        for i, cost in enumerate(costs):
            if cost < best_cost:
                best_cost = cost
                best_solution = solutions[i]
        
        # Update pheromones
        update_pheromones(solutions, costs)
    
    return best_solution, best_cost

def create_tour():
    tour = []
    cost = 0
    robot = np.random.choice(len(depots))
    tour.append(depots[robot])
    
    unvisited = set(range(len(cities))) - set(depots)
    current_city = tour[-1]
    
    while unvisited:
        probs = pheromones[current_city] ** alpha * heuristic[current_city] ** beta
        if sum(probs) > 0:
            probs = probs / sum(probs)
            next_city = np.random.choice(len(cities), p=probs)
        else:
            next_city = unvisited.pop()  # To avoid a choice out of an empty distribution
        
        tour.append(next_city)
        cost += distances[current_city][next_city]
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(tour[0])  # Return to the start depot
    cost += distances[current_city][tour[0]]  # Add the cost to return to the depot
    
    return tour, cost

def update_pheromones(solutions, costs):
    # Evaporation
    pheromones *= (1 - rho)
    
    # Reinforcement
    for idx in range(len(solutions)):
        tour = solutions[idx]
        contribution = 1 / costs[idx]
        for i in range(len(tour)-1):
            pheromones[tour[i]][tour[i+1]] += contribution

# Execute the optimization
best_tour, best_tour_cost = ant_colony_optimization()

# Display output
print("Optimal tour:", best_tour)
print("Cost of the best tour:", best_tour_cost)