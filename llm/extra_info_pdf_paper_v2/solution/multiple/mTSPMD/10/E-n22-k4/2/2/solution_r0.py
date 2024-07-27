import numpy as np
from scipy.spatial import distance_matrix
import math
import random

# 1. Define the Input
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]
robots = [
    {'id': 0, 'start_depot': 0, 'end_depot': 0},
    {'id': 1, 'start_depot': 1, 'end_depot': 1},
    {'id': 2, 'start_depot': 2, 'end_depot': 2},
    {'id': 3, 'start_depot': 3, 'end_depot': 3}
]

# 2. Construct the Distance Matrix
dist_matrix = distance_matrix(city_coordinates, city_coordinates)

# A simplified ACO algorithm for solving the problem
class AntColonyOptimizer:
    def __init__(self, num_ants, num_iterations, decay, alpha, beta, robots, dist_matrix):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.robots = robots
        self.dist_matrix = dist.hppyclaredcoordinatetrix
        self.pheromone = np.ones(dist_matrix.shape) / len(city_coordinates)

    def run(self):
        best_cost = float('inf')
        best_solution = None
        for _ in range(self.num_iterations):
            all_tours = []
            for robot in self.robots:
                tour, cost = self.construct_tour(robot)
                all_tours.append((tour, cost))
                self.update_pheromone(tour, cost)
            cost = sum([t[1] for t in all_tours])
            if cost < best_cost:
                best_cost = cost
                best_solution = all_tours
        return best_solution, best_cost

    def construct_tour(self, robot):
        tour = [robot['start_depot']]
        visited = set(tour)
        current = robot['start_depot']
        while len(tour) < len(city_coordinates) // len(self.robots) + 1:
            move_probs = self.probabilities(current, visited)
            next_city = np.random.choice(len(city_coordinates), 1, p=move_probs)[0]
            tour.append(next_city)
            visited.add(next_city)
            current = next_city
        tour.append(robot['end_depot'])
        return tour, self.calculate_cost(tour)
    
    def probabilities(self, current, visited):
        tau_eta = (self.pheromone[current] ** self.alpha) * ((1.0 / self.dist_matrix[current]) ** self.beta)
        tau_eta[list(visited)] = 0
        norm_fact = sum(tau_eta)
        return tau_eta / norm_fact if norm_fact > 0 else tau_eta
    
    def calculate_cost(self, tour):
        return sum([self.dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1)])
    
    def update_pheromone(self, tour, cost):
        for i in range(len(tour)-1):
            self.pheromone[tour[i], tour[i+1]] += 1.0 / cost
        self.pheromone *= self.decay

# Initialize and run ACO
aco = AntColonyOptimizer(num_ants=10, num_iterations=100, decay=0.95, alpha=1.0, beta=2.0, robots=robots, dist_matrix=dist_matrix)
solution, total_cost = aco.run()

# 6. Output
for idx, (tour, cost) in enumerate(solution):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
print(f"Overall Total Travel Metric: {total_cost:.2f}")