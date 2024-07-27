import numpy as np

# City coordinates (including depots)
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
               (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
               (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
               (164, 193), (129, 189), (155, 185), (139, 182)]

# Parameters for ACO
num_ants = 20
num_iterations = 100
decay = 0.5
alpha = 1  # impact of pheromones on the probability
beta = 5   # impact of heuristic value (1/distance)
initial_pheromone = 1 / len(coordinates)

# Calculate Distance Matrix
def calculate_distances(coords):
    num_cities = len(coords)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            distances[i, j] = distances[j, i] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
    return distances

# Ant Colony Optimization
def aco_tsp(distances, num_ants, num_iterations, decay, alpha, beta):
    num_cities = len(distances)
    pheromones = np.ones((num_cities, num_cities)) * initial_pheromone
    shortest_path = None
    best_length = float('inf')
    
    for _ in range(num_iterations):
        paths = []
        lengths = []
        
        for __ in range(num_ants):
            path = [np.random.randint(4)] # starts randomly among 4 depots
            while len(set(path)) < num_cities:
                valid_moves = [city for city in range(num_cities) if city not in set(path)]
                probabilities = []
                
                for city in valid_moves:
                    pheromone = pheromones[path[-1], city] ** alpha
                    heuristic = (1.0 / distances[path[-1], city]) ** beta
                    probabilities.append(pheromone * heuristic)
                
                probabilities = np.array(probabilities) / sum(probabilities)
                next_city = np.random.choice(valid_moves, p=probabilities)
                path.append(next_city)
            
            path.append(path[0]) # Return to the starting depot
            length = sum(distances[path[i], path[i+1]] for i in range(len(path) - 1))
            
            paths.append(path)
            lengths.append(length)
        
        # Update pheromones
        pheromones *= decay
        for path, length in zip(paths, lengths):
            for i in range(len(path)-1):
                pheromones[path[i], path[i+1]] += 1 / length
        
        # Store the best solution
        if min(lengths) < best_length:
            best_length = min(lengths)
            shortest_path = paths[np.argmin(lengths)]
    
    return shortest_path, best_length

# Solving the problem
distances = calculate_distances(coordinates)
best_path, best_length = aco_tsp(distances, num_ants, num_iterations, decay, alpha, beta)

# Print the outputs
def print_solution(best_path, best_length):
    print(f'Best Path: {best_path}')
    print(f'Best Total Travel Cost: {best_length:.2f}')

print_solution(best_path, best_length)