import numpy as np

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Calculate the distance matrix
n = len(coordinates)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Ant Colony Optimization parameters
num_ants = 8
num_iterations = 100
decay = 0.9
alpha = 1
beta = 5
initial_pheromone = 1 / (n * np.mean(dist_matrix)) # heuristic

# Initialize pheromones
pheromones = np.ones((n, n)) * initial_pheromone

def aco_solve_mdvrp():
    global pheromones
    
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_iterations):
        all_routes = []
        all_costs = []

        for ant in range(num_ants):
            route = [ant]  # start from respective depot
            total_cost = 0

            unvisited = set(range(n)) - {ant}
            while unvisited:
                current = route[-1]
                probabilities = np.array([pheromones[current][j] * (1 / dist_matrix[current][j])**beta for j in unvisited])
                probabilities /= probabilities.sum()
                next_city = np.random.choice(list(unvisited), p=probabilities)
                route.append(next_city)
                unvisited.remove(next_city)
                total_cost += dist_matrix[current][next_city]

            # Completing the tour by returning to the depot
            route.append(ant)
            total_cost += dist_matrix[next_city][ant]

            all_routes.append(route)
            all_costs.append(total_cost)

            # Update pheromones (local updating rule)
            for i in range(len(route)-1):
                pheromones[route[i]][route[i+1]] *= decay
                pheromones[route[i]][route[i+1]] += initial_pheromone
                
        # Collect the best solution found in all iterations
        current_iteration_cost = sum(all_costs)
        if current_iteration_cost < best_cost:
            best_cost = current_iteration_cost
            best_solution = all_routes
    
    return best_solution, best_cost, all_costs

best_solution, best_total_cost, individual_costs = acomponent_mdvrp()

# Output tours and costs:
print(f"Overall Total Travel Cost: {best_total_cost}")
for i, tour in enumerate(best_solution):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Coast: {individual_costs[i]}")