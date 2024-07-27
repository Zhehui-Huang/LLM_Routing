import numpy as np
from scipy.spatial import distance_matrix
import random

# Environment setup
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]
num_cities = len(city_coordinates)
dist_matrix = distance_matrix(city_coordinates, city_coordinates)

robots = [
    {'id': 0, 'depot': 0},
    {'id': 1, 'depot': 1},
    {'id': 2, 'depot': 2},
    {'id': 3, 'depot': 3}
]
num_robots = len(robots)

# Ant Colony Optimization (ACO) setup
class AntColonyOptimizer:
    def __init__(self, dist_matrix, num_ants=10, num_iterations=100, decay=0.1, alpha=1, beta=3):
        self.dist_matrix = dist_matrix
        self.pheromone = np.ones(dist_matrix.shape) / num_cities
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
    
    def run(self):
        best_cost = float('inf')
        best_solution = None
        
        for _ in range(self.num_iterations):
            solutions = []
            for _ in range(self.num_ants):
                solution = self.generate_solution()
                solutions.append(solution)
            
            for solution in solutions:
                cost = self.calculate_cost(solution)
                if cost < best_cost:
                    best_cost = cost
                    best_solution = solution
            
            self.update_pheromone(solutions, best_cost)
        
        return best_solution, best_cost
    
    def generate_solution(self):
        all_tours = [[] for _ in range(num_robots)]
        available_cities = set(range(1, num_cities))  # excluding depots
        cities_to_visit = np.array_split(list(available_cities), num_robots)
        
        for index, robot in enumerate(robots):
            start = robot['depot']
            tour = [start]
            cities = list(cities_to_visit[index])
            while cities:
                probabilities = self.move_probabilities(tour[-1], cities)
                next_city = np.random.choice(cities, p=probabilities)
                tour.append(next_city)
                cities.remove(next_city)
            tour.append(start)
            all_tours[index] = tour
        
        return all_tours
    
    def move_probabilities(self, current, cities):
        pheromones = self.pheromone[current, cities]
        distances = self.dist_matrix[current, cities]
        probabilities = pheromones ** self.alpha / (distances ** self.beta)
        return probabilities / sum(probabilities)
    
    def calculate_cost(self, solutions):
        total_cost = 0
        for solution in solutions:
            tour_cost = sum([self.dist_matrix[solution[i], solution[i + 1]] for i in range(len(solution) - 1)])
            total_cost += tour_cost
        return total_cost
    
    def update_pheromone(self, solutions, best_cost):
        for row in range(num_cities):
            for col in range(num_cities):
                self.pheromone[row, col] *= (1 - self.decay)
        
        for solution in solutions:
            for tour in solution:
                for i in range(len(tour) - 1):
                    self.pheromone[tour[i], tour[i + 1]] += 1 / best_cost

# Execute ACO
aco = AntColonyOptimizer(dist_matrix)
best_solution, best_cost = aco.run()

# Presenting results
print("Best Solution found:")
for idx, tour in enumerate(best_solution):
    print(f"Robot {idx} Tour: {tour}")
    tour_cost = sum([dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1)])
    print(f"Robot {idx} Total Travel Cost: {tour_id}")

print(f"Overall Total Travel Cost: {best_cost}")