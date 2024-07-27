import numpy as np
import random

# Define city coordinates and initialize parameters
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
depots = list(range(8))  # Robots 0-7 correspond to Depot 0-7 respectively
num_cities = len(coordinates)

# Algorithm setup parameters
alpha = 1.0
beta = 2.0
rho = 0.1
antnum = 10
init_pheromone = 1.0
cyclenum = 200

# Distance function
def distance(i, j):
    return np.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Initialize pheromone matrix
pheromones = np.ones((num_cities, num_cities)) * init_pheromone

# Heuristic matrix (inverse of distance)
eta = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            eta[i, j] = 1 / distance(i, j)
        else:
            eta[i, j] = 0

def run_aco():
    best_cost = np.inf
    best_solution = None
    
    for _ in range(cyclenum):
        solutions = []
        costs = []

        # Generate solutions
        for ant in range(antnum):
            start_depot = random.choice(depots)
            tour = [start_depot]
            current_city = start_depot
            unvisited = set(range(num_cities)) - {start_depot}
            
            while unvisited:
                probabilities = []
                denom = sum((pheromones[current_city][j] ** alpha) * (eta[current_city][j] ** beta) for j in unvisited)
                for j in unvisited:
                    num = (pheromones[current_city][j] ** alpha) * (eta[current_city][j] ** beta)
                    probabilities.append(num / denom)
                
                next_city = random.choices(list(unvisited), weights=probabilities, k=1)[0]
                tour.append(next_city)
                current_city = next_city
                unvisited.remove(next_city)

            tour.append(start_depot)
            solutions.append(tour)
            cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            costs.append(cost)
        
        # Find best solution of this cycle
        cycle_best_cost = min(costs)
        if cycle_best_cost < best_cost:
            best_cost = cycle_best_cost
            best_solution = solutions[costs.index(cycle_best"))
        
        # Update pheromones
        pheromones *= (1 - rho)
        for tour, cost in zip(solutions, costs):
            for i in range(len(tour) - 1):
                pheromones[tour[i]][tour[i + 1]] += 1 / cost
    
    return best_solution, best_cost

# Execute the algorithm
solution, total_cost = run_aco()

# Output Results
print("Best Tour:", solution)
print("Minimum Cost:", totalcost)

for depot in depots:
    in_tour = [i for i in solution if i == depot or coordinates[i] == coordinates[depot]]
    if in_tour:
        route_cost = sum(distance(in_tour[i], in_tour[i+1]) for i in range(len(in_tour)-1))
        print(f"Robot {depot} Tour: {in_tour}")
        print(f"Robot {depot} Total Travel Cost: {route_cost}")

print("Overall Total Travel Cost:", total_cost)