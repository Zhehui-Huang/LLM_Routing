import numpy as np
import random

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

class AntColonyOptimization:
    def __init__(self, cities, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        self.cities = cities
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        
        self.distances = np.array([
            [euclidean_distance(c1, c2) for c2 in cities]
            for c1 in cities
        ])
        self.n_cities = len(cities)
        self.pheromone = np.ones((self.n_cities, self.n_cities)) / self.n_cities
        
    def run(self):
        shortest_path = None
        all_time_shortest_path = ("path", float('inf'))
        for i in range(self.n_iterations):
            all_paths = self.generate_paths()
            self.spread_pheromone(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone *= self.decay
        return all_time_shortest_path
    
    def spread_pheromone(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]
    
    def generate_paths(self):
        all_paths = []
        for _ in range(self.n_ants):
            path = []
            visited = set()
            start = random.choice(range(self.n_cities))
            visited.add(start)
            current = start
            while len(visited) < self.n_cities:
                move = self.pick_move(self.pheromone[current], self.distances[current], visited)
                path.append((current, move))
                current = move
                visited.add(move)
            path.append((current, start))  # return to start
            all_paths.append((path, self.path_cost(path)))
        return all_paths
    
    def pick_move(self, pheromone, distances, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0
        row = pheromone ** self.alpha * ((1.0 / distances) ** self.beta)
        norm_row = row / row.sum()
        move = np_choice(range(self.n_cities), 1, p=norm_row)[0]
        return move
    
    def path_cost(self, path):
        total_cost = 0
        for (start, end) in path:
            total_cost += self.distances[start][end]
        return total_cost

# Example cities given by the problem
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Set parameters for the Ant Colony Optimization
n_ants = 10
n_best = 5
n_iterations = 100
decay = 0.95
alpha = 1
beta = 2

# Initialize ant colony optimization algorithm
aco = AntColonyOptimization(cities, n_ants, n_best, n_iterations, decay, alpha, beta)

# Run the ant colony optimization algorithm
best_path = aco.run()
print("Best path found by ant colony optimization:")
print(best_path)