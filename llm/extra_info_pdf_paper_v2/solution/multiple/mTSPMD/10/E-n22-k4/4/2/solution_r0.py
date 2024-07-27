import numpy as np
import random

class ACO:
    def __init__(self, cities, n_ants, n_iterations, decay, alpha, beta, Q):
        self.cities = cities
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.Q = Q
        self.rank = len(cities)
        self.pheromones = np.ones((self.rank, self.rank))
        self.distances = np.array([[np.linalg.norm(np.array(cities[i]) - np.array(cities[j])) for j in range(self.rank)] for i in range(self.rank)])

    def run(self):
        for _ in range(self.n_iterations):
            costs, all_paths = self.generate_all_paths()
            self.update_pheromones(all_paths, costs)
        return self.best_path()

    def generate_all_paths(self):
        all_paths = []
        costs = []
        for _ in range(self.n_ants):
            path = self.generate_path(0)  # Start at depot (fixed starting point for simplification)
            cost = self.path_cost(path)
            costs.append(cost)
            all_paths.append(path)
        return costs, all_paths

    def generate_path(self, start):
        path = []
        visited = set()
        current = start
        path.append(current)
        visited.add(current)
        for _ in range(1, self.rank):
            move = self.pick_move(self.pheromones[current], self.distances[current], visited)
            path.append(move)
            visited.add(move)
            current = move
        path.append(start)  # return to the depot
        return path

    def pick_move(self, pheromone, dist, visited):
        pheromones = np.copy(pheromone)
        pheromones[list(visited)] = 0
        row = pheromones ** self.alpha * ((1.0 / dist) ** self.beta)
        norm_row = row / row.sum()
        move = np.random.choice(range(self.rank), 1, p=norm_row)[0]
        return move

    def path_cost(self, path):
        return sum([self.distances[path[i], path[i+1]] for i in range(len(path)-1)])

    def update_pheromones(self, paths, costs):
        for i, path in enumerate(paths):
            for move, to in zip(path[:-1], path[1:]):
                self.pheromones[move, to] += self.Q / costs[i]
        self.pheromones *= self.decay

    def best_path(self):
        shortest_cost = float('inf')
        best_path = []
        for i in range(self.rank):
            path = self.generate_path(i)
            cost = self.path_cost(path)
            if cost < shortest1_cost:
                shortest_cost = cost
                best_path = path
        return best_path, shortest_cost

# Define the cities' coordinates and parameters
cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), 
          (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), 
          (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)]
n_ants = 20
n_iterations = 100
decay = 0.95
alpha = 1.0
beta = 5.0
Q = 100

# Instantiate and run the ACO
aco = ACO(cities, n_ants, n_iterations, decay, alpha, beta, Q)
tour, cost = aco.run()

# Output final results
print(f"Best Tour: {tour}")
print(f"Total Travel Cost: {cost}")