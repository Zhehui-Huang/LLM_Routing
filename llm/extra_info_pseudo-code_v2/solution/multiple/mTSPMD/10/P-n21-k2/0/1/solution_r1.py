import math
import random

# Coordinates of Cities including Depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Helper Functions
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def initialize_pheromones(num_cities, initial_pheromone):
    return [[initial_pheromone for _ in range(num_cities)] for __ in range(num_cities)]

# Ant Colony Optimization Implementation based on environment specifics
class AntColonyOptimizer:
    def __init__(self, cities, num_ants, depot_0, depot_1, alpha, beta, rho, num_iterations):
        self.cities = cities
        self.depot_0 = depot_0
        self.depot_1 = depot_1
        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.iterations = num_iterations
        self.pheromones = initialize_pheromones(len(cities), 1)
        self.heuristic_info = [[1 / (euclidean_distance(i, j) if i != j else 1e-10) for j in range(len(cities))] for i in range(len(cities))]

    def solve(self):
        best_cost = float('inf')
        best_tours = None
        
        for _ in range(self.iterations):
            all_tours = []
            all_costs = []
            
            for ant in range(self.num_ants):
                if ant % 2 == 0:
                    tour, cost = self.construct_tour(self.depot_0)
                else:
                    tour, cost = self.construct_tour(self.depot_1)
                
                all_tours.append(tour)
                all_costs.append(cost)
                
                if cost < best_cost:
                    best_cost = cost
                    best_tours = tour
            
            self.update_pheromones(all_tours, all_costs)
        
        return best_tours, best_cost

    def construct_tour(self, start_depot):
        tour = [start_depot]
        current_city = start_depot
        unvisited = set(self.cities.keys()) - {start_depot}
        
        while unvisited:
            next_city = self.select_next_city(current_city, unvisited)
            tour.append(next_city)
            current_city = next_city
            unvisited.remove(next_city)
        
        tour.append(start_depot)  # return to depot
        cost = self.calculate_tour_cost(tour)
        return tour, cost

    def select_next_city(self, current_city, unvisited):
        probabilities = []
        total_prob = 0
        
        for city in unvisited:
            prob = (self.pheromones[current_city][city] ** self.alpha) * (self.heuristic_info[current_city][city] ** self.beta)
            probabilities.append(prob)
            total_prob += prob
        
        probabilities = [prob / total_prob for prob in probabilities]
        next_city = random.choices(list(unvisited), weights=probabilities, k=1)[0]
        
        return next_city

    def update_pheromones(self, tours, costs):
        for i in range(len(cities)):
            for j in range(len(cities)):
                self.pheromones[i][j] *= (1 - self.rho)  # evaporation
        
        for tour, cost in zip(tours, costs):
            for i in range(len(tour) - 1):
                self.pheromones[tour[i]][tour[i + 1]] += 1.0 / cost

    def calculate_tour_cost(self, tour):
        return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Parameters
num_ants = 10
iterations = 100
alpha = 1.0
beta = 2.0
rho = 0.5

# Create the optimizer instance for solving
aco = AntColonyOptimizer(cities, num_ants, 0, 1, alpha, beta, rho, iterations)
best_tours, best_cost = aco.solve()

# Print Results
for robot, start_depot in enumerate([0, 1]):
    proper_tour = [city for city in best_tours if cities[city] in [cities[start_depot]] or city not in [0, 1]]
    cost = aco.calculate_tour_cost(proper_tour)
    proper_tour = [start_depot] + proper_tour + [start_depot]
    
    print(f"Robot {robot} Tour: {proper_tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

overall_cost = aco.calculate_tour_cost(best_tours)
print(f"Overall Total Travel Cost: {overall_cost:.2f}")