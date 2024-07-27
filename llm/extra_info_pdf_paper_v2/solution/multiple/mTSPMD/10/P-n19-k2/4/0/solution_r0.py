import math
import random

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(route, coordinates):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += euclidean_distance(coordinates[route[i]][0], coordinates[route[i]][1],
                                         coordinates[route[i + 1]][0], coordinates[route[i + 1]][1])
    return total_dist

class AntColonyOptimizer:
    def __init__(self, coordinates, num_ants, num_iterations, decay, alpha=1, beta=5):
        self.coordinates = coordinates
        self.num_cities = len(coordinates)
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.pheromone = [[1 / (self.num_cities * self.num_cities) for _ in range(self.num_cities)] for _ in range(self.num_cities)]
        self.distances = [[euclidean_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]) for j in range(self.num_cities)] for i in range(self.num_cities)]
    
    def run(self):
        best_cost = float('inf')
        best_solution = []
        for _ in range(self.num_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheromone(all_paths, best_cost, best_solution)
            best_cost, best_solution = self.find_best_path(all_paths, best_cost, best_solution)
        return best_solution, best_cost
    
    def gen_all_paths(self):
        all_paths = []
        for _ in range(self.num_ants):
            path = self.gen_path(0)  # Assume starting from city 0; this will be changed for depots
            all_paths.append((path, calculate_total_distance(path, self.coordinates)))
        return all_paths
    
    def gen_path(self, start):
        path = [start]
        visited = set(path)
        for _ in range(1, self.num_cities):
            move = self.pick_move(path[-1], visited)
            path.append(move)
            visited.add(move)
        path.append(start)  # Return to start depot
        return path
    
    def pick_move(self, current, visited):
        denom = sum([self.pheromone[current][i] ** self.alpha * ((1.0 / self.distances[current][i]) ** self.beta) if i not in visited else 0 for i in range(self.num_cities)])
        probabilities = [(self.pheromone[current][i] ** self.alpha * ((1.0 / self.distances[current][i]) ** self.beta)) / denom if i not in visited and denom != 0 else 0 for i in range(self.num_cities)]
        move = random.choices(range(self.num_cities), probabilities)[0]
        return move

    def spread_pheromone(self, all_paths, best_cost, best_solution):
        for path, cost in all_paths:
            for i in range(len(path) - 1):
                self.pheromone[path[i]][path[i+1]] += 1.0 / self.distances[path[i]][path[i+1]]
    
    def find_best_path(self, all_paths, best_cost, best_solution):
        for path, cost in all_paths:
            if cost < best_cost:
                best_cost = cost
                best_solution = path
        return best_cost, best_solution