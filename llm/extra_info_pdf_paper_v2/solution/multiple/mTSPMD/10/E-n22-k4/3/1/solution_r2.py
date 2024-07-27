import numpy as np
import math

# Define city coordinates and depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 199), (163, 226), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)]

depots = [0, 1, 2, 3]
num_robots = 4

# Ant colony parameters
num_ants = 10
num_iterations = 100
evaporation_rate = 0.5
alpha = 1.0  # influence of pheromone
beta = 2.0   # influence of heuristic
Q = 100  # pheromone deposit factor

# Calculate the Euclidean distance between two points
def euclidean_dist(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Initialize distance and pheromone matrices
distances = np.array([[euclidean_dist(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))])
pheromones = 0.1 * np.ones((len(coordinates), len(coordinates)))

def probabilistic_choices(available, current):
    pheromone = np.array([pheromones[current][j] for j in available])
    distance = np.array([distances[current][j] for j in available])
    heuristics = 1 / distance
    probabilities = pheromone**alpha * heuristics**beta
    probabilities /= probabilities.sum()
    return np.random.choice(available, p=probabilities)

# Solve mTSP using Ant Colony Optimization
def solve_mTSP():
    best_routes = None
    best_cost = float('inf')
    
    for iteration in range(num_iterations):
        routes = {i: [] for i in range(num_robots)}
        costs = {i: 0 for i in range(num_robots)}
        
        # Each ant generates a solution
        for ant in range(num_ants):
            all_nodes = set(range(len(coordinates))) - set(depots)
            robots_positions = depots[:]
            
            while all_nodes:
                for robot_id in range(num_robots):
                    if not all_nodes:
                        break
                    
                    current = robots_positions[robot_id]
                    if not routes[robot_id]:
                        routes[robot_id].append(current)
                    
                    available_nodes = list(all_nodes)
                    next_city = probabilistic_choices(available_nodes, current)
                    routes[robot_id].append(next_city)
                    robots_positions[robot_id] = next_city
                    costs[robot_id] += distances[current][next_city]
                    all_nodes.remove(next_city)

            for robot_id in range(num_robots):
                routes[robot_id].append(depots[robot_id])
                costs[robot_id] += distances[robots_positions[robot_id]][depots[robot_id]]

            # Update pheromones
            for robot_id in range(num_robots):
                route = routes[robot_id]
                for i in range(len(route) - 1):
                    pheromones[route[i]][route[i+1]] += Q / costs[robot_id]
                    pheromones[route[i+1]][route[i]] += Q / costs[robot_id]  # Symmetric

        # Evaporation of pheromones
        pheromones *= (1 - evaporation_rate)

        if sum(costs.values()) < best_cost:
            best_cost = sum(costs.values())
            best_routes = routes
    
    return best_routes, best_cost

# Run the solution and output the results
best_solution, best_total_cost = solve_mTSP()
for robot_id in range(num_robots):
    route = best_solution[robot_id]
    tour_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))
    print(f"Robot {robot_id+1} Tour: {route}")
    print(f"Robot {robot_id+1} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {best_total_style.stripound()}")