import numpy as np

class AntColonyOptimizer:
    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        self.distances = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.construct_paths()
            self.update_pheromone(all_paths)
            shortest_path = min(all_paths, key=lambda x: x[1])
            print(f"Iteration {i+1}: Best Path {shortest_path[0]}, Cost {shortest_path[1]}")
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone * self.decay
        return all_time_shortest_path

    def construct_paths(self):
        all_paths = []
        for _ in range(self.n_ants):
            path = self.generate_path(0)
            all_paths.append((path, self.path_cost(path)))
        return all_paths

    def generate_path(self, start):
        path = [start]
        visited = set(path)
        prev = start
        for _ in range(len(self.distances) - 1):
            move = self.probabilistic_next_move(self.pheromone[prev], self.distances[prev], visited)
            path.append(move)
            prev = move
            visited.add(move)
        path.append(start)  # ending point to start
        return path

    def probabilistic_next_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0
        row = pheromone ** self.alpha * ((1.0 / dist) ** self.beta)
        norm_row = row / row.sum()
        move = np.random.choice(self.all_inds, 1, p=norm_row)[0]
        return move

    def path_cost(self, path):
        return sum([self.distances[path[i], path[i + 1]] for i in range(len(path) - 1)])

    def update_pheromone(self, paths):
        sorted_paths = sorted(paths, key=lambda x: x[1])
        for path, length in sorted_paths[:self.n_best]:
            for i in range(len(path) - 1):
                self.pheromone[path[i]][path[i + 1]] += 1.0 / self.distances[path[i]][path[i + 1]]

def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

if __name__ == "__main__":
    cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
          (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
          (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
          (164, 193), (129, 189), (155, 185), (139, 182)]

    distances = np.array([[distance(x, y) for y in cities] for x in cities])
    aco = AntColonyOptimizer(distances, n_ants=10, n_best=5, n_iterations=100, decay=0.95, alpha=1, beta=2)
    shortest_path = aco.run()
    print("Best path found:", shortest_path)