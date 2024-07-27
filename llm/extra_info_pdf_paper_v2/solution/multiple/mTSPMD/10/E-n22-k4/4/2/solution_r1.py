import numpy as np
from itertools import cycle

class ACO:
    def __init__(self, cities, n_ants, n_iterations, decay, alpha, beta, Q, start_points):
        self.cities = np.array(cities)
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.Q = Q
        self.start_points = start_points
        self.rank = len(cities)
        self.pheromones = np.ones((self.rank, self.rank))
        self.distances = np.array([[np.linalg.norm(cities[i] - cities[j])
                                    for j in range(self.rank)] for i in range(self.rank)])

    def run(self):
        best_cost = float('inf')
        best_solution = None
        for _ in range(self.n_iterations):
            all_solutions = []
            all_costs = []
            for start in self.start_points:
                path = self.generate_path(start)
                cost = self.path_cost(path)
                all_solutions.append(path)
                all_costs.append(cost)
                self.update_pheromones([path], [cost])
            
            total_cost = sum(all_costs)
            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = all_solutions
        
        return best_solution, all_costs, best_cost

    def generate_path(self, start):
        path = [start]
        visited = set(path)
        current = start

        while len(visited) < self.rank:
            next_city = self.select_next_city(current, visited)
            path.append(next_city)
            visited.add(next_city)
            current = next_city
        path.append(start)  # Return to start point
        return path

    def select_next_city(self, current, visited):
        probabilities = self.pheromones[current] ** self.alpha * ((1.0 / (self.distances[current] + 1e-10)) ** self.beta)
        probabilities[list(visited)] = 0
        probabilities /= probabilities.sum()
        return np.random.choice(self.rank, 1, p=probabilities)[0]

    def path_cost(self, path):
        return sum(self.distances[path[i], path[i + 1]] for i in range(len(path) - 1))

    def update_pheromones(self, paths, costs):
        for path, cost in zip(paths, costs):
            for i in range(len(path) - 1):
                self.pheromones[path[i], path[i + 1]] += self.Q / cost
        self.pheromones *= self.decay

# Define the cities' coordinates
cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
          (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
          (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
          (164, 193), (129, 189), (155, 185), (139, 182)]

# Optimization parameters
n_ants = 20
n_iterations = 100
decay = 0.95
alpha = 1.0
beta = 2.0
Q = 100

# Robot depots
depots = [0, 1, 2, 3]

# Initialize and run ACO
aco_instance = ACO(cities=cities, n_ants=n_ants, n_iterations=n_iterations, decay=decay, 
                   alpha=alpha, beta=beta, Q=Q, start_points=depots)
solutions, costs, total_cost = aco_instance.run()

# Display result
for i, (path, cost) in enumerate(zip(solutions, costs)):
    print(f"Robot {i} Tour from Depot {depots[i]}: {path}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")