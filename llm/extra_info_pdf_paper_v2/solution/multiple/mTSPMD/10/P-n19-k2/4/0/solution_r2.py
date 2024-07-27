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

def initialize_pheromone(num_cities, initial_value):
    return [[initial_value for _ in range(num_cities)] for _ in range(num_cities)]

def initialize_visibility(coordinates):
    num_cities = len(coordinates)
    visibility = [[0 if i == j else 1 / euclidean_distance(coordinates[i][0], coordinates[i][1],
                                                          coordinates[j][0], coordinates[j][1])
                   for j in range(num_cities)] for i in range(num_cities)]
    return visibility

class Ant:
    def __init__(self, start_city):
        self.current_city = start_city
        self.tour = [start_city]
        self.tour_length = 0

    def select_next_city(self, pheromone, visibility, alpha, beta):
        probabilities = []
        denominator = 0
        for i in range(len(pheromone)):
            if i not in self.tour:
                denominator += (pheromone[self.current_city][i] ** alpha) * (visibility[self.current_city][i] ** beta)
        
        for i in range(len(pheromone)):
            if i not in self.tour:
                numerator = (pheromone[self.current_city][i] ** alpha) * (visibility[self.current_city][i] ** beta)
                probabilities.append(numerator / denominator)
            else:
                probabilities.append(0)
        
        next_city = random.choices(range(len(pheromone)), weights=probabilities, k=1)[0]
        self.tour.append(next_city)
        self.tour_length += euclidean_distance(coordinates[self.current_city][0], coordinates[self.current_city][1],
                                               coordinates[next_city][0], coordinates[next_circle][1])
        self.current_city = next_city

    def complete_tour(self, coordinates):
        initial_city = self.tour[0]
        self.tour_length += euclidean_distance(coordinates[self.current_city][0], coordinates[self.current_city][1],
                                               coordinates[initial_city][0], coordinates[initial_city][1])
        self.tour.append(initial_city)

def ant_colony_optimization(coordinates, num_ants, num_iterations, alpha, beta, evaporation_rate):
    num_cities = len(coordinates)
    pheromone = initialize_pheromone(num_cities, 1)
    visibility = initialize_visibility(coordinates)
    best_tour = None
    best_tour_length = float('inf')
    
    for _ in range(num_iterations):
        ants = [Ant(start_city=i % num_cities) for i in range(num_ants)]
        
        for ant in ants:
            while len(ant.tour) < num_cities:
                ant.select_next_city(pheromone, visibility, alpha, beta)
            ant.complete_tour(coordinates)
            
            if ant.tour_length < best_tour_length:
                best_tour_length = ant.tour_length
                best_tour = ant.tour[:]
        
        # Pheromone Evaporation
        for i in range(num_cities):
            for j in range(num_cities):
                pheromone[i][j] *= (1 - evaporation_rate)
        
        # Pheromone Update
        for ant in ants:
            for k in range(len(ant.tour) - 1):
                i, j = ant.tour[k], ant.tour[k + 1]
                pheromone[i][j] += 1 / ant.tour_length
    
    return best_tour, best_tour_length

# Define the cities and their coordinates
coordinates = [
   (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
   (42, 25), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
   (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), 
   (45, 35)
]

# Run the algorithm
best_tour, best_tour_length = ant_colony_optimization(coordinates, num_ants=10, num_iterations=100,
                                                      alpha=1, beta=2, evaporation_rate=0.5)

# Output the results
print("Best tour:", best_tour)
print("Best tour length:", best_tour_length)