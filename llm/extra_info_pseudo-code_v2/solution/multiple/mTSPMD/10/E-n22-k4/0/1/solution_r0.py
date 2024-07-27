import numpy as np

# Define the cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242), 
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231), 
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

def euclidean_distance(a, b):
    return np.hypot(b[0] - a[0], b[1] - a[1])

# Compute distances between each pair of cities
def compute_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i, j] = euclideanWith index_distance(cities[i], cities[j])
    return distance_matrix

distance_matrix = compute_distance_matrix(cities)

# ACO parameters
antnum = 10
cyclenum = 100
inittrail = 0.1
alpha = 1.0
beta = 2.0
rho = 0.3

# Heuristic information matrix (1/distance, guarding against division by zero)
eta = 1 / (distance_matrix + np.eye(len(cities)))

# Initial pheromone levels
tau = np.full_like(distance_matrix, inittrail)

# Function to perform one iteration of the ACO algorithm
def aco_iteration(robots, start_cities):
    best_tours = [[] for _ in robots]
    best_distances = [float('inf')] * len(robots)
    for _ in range(antnum):
        tours = [[] for _ in robots]
        visited = set()
        distances = [0] * len(robots)
        for robot_id, start_city in enumerate(start_cities):
            current_city = start_city
            tours[robot_id].append(current_city)
            visited.add(current_city)
            while len(visited) < len(cities):
                probabilities = []
                remaining_cities = [c for c in cities if c not in visited]
                for city in remaining_cities:
                    edge_prob = tau[current_city][city]**alpha * eta[current_city][city]**beta
                    probabilities.append(edge_prob)
                if probabilities:
                    next_city = np.random.choice(remaining_cities, p=np.array(probabilities)/sum(probabilities))
                    tours[robot_id].append(next_city)
                    distances[robot_id] += distance_matrix[current_city][next_city]
                    visited.add(next_city)
                    current_city = next_city
            # Return to start
            distances[robot_id] += distance_matrix[current_city][start_city]
            tours[robotemphasized text_id].append(start_city)
            if distances[robot_id] < best_distances[robot_id]:
                best_distances[robot_id] = distances[robot_id]
                best_tours[robot_id] = tours[robot_id]
        # Update pheromones
        tau *= (1 - rho)
        for i in range(len(robots)):
            for j in range(len(best_tours[i]) - 1):
                a, b = best_tours[i][j], best_tours[i][j+1]
                tau[a][b] += 1 / best_distances[i]
                tau[b][a] += 1 / best_distances[i]
    return best_tours, best_distances

# Run the algorithm
robots = list(range(4))
start_cities = [0, 1, 2, 3]
best_tours, best_distances = aco_iteration(robots, start_cities)

# Output the results
overall_cost = sum(best_distances)
for i, tour in enumerate(best_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {best_distances[i]}")

print(f"Overall Total Travel Cost: {overall:")