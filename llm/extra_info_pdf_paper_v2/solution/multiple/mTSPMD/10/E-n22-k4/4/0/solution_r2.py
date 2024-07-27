import numpy as np
from math import sqrt

# Constants and Parameters
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
depots = [0, 1, 2, 3]
num_ants = 10
num_iterations = 100
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
pheromone_init = 0.1

# Initialize distances and pheromone levels
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))
pheromones = np.ones((num_cities, num_cities)) * pheromone_init

# Calculate all-pairs distances
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i, j] = sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Function to compute the cost of a tour
def calculate_cost(route):
    return sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))

# Find tours using Ant Colony Optimization
def find_tours():
    global best_cost, best_tours
    best_cost = float('inf')
    for iteration in range(num_iterations):
        all_tours = []
        for ant in range(num_ants):
            tours = {depot: [depot] for depot in depots}
            remaining_cities = set(range(num_cities)) - set(depots)

            while remaining_cities:
                for depot in depots:
                    if not remaining_cities:
                        break
                    current_city = tours[depot][-1]
                    probabilities = [(pheromones[current_city][city] ** alpha) * ((1.0 / distances[current_city][city]) ** beta) if city in remaining_cities else 0 for city in range(num_cities)]
                    probabilities = np.array(probabilities)
                    probabilities /= probabilities.sum()
                    next_city = np.random.choice(range(num_cities), p=probabilities)
                    tours[depot].append(next_city)
                    remaining_cities.remove(next_city)

            for depot in depots:
                tours[depot].append(depot)  # Return to starting depot
            all_tours.append(tours)

        # Update pheromones
        pheromones *= (1 - evaporation_rate)
        for tours in all_tours:
            for depot, tour in tours.items():
                tour_cost = calculate_cost(tour)
                pheromone_addition = 1 / tour_cost
                for i in range(len(tour) - 1):
                    pheromones[tour[i], tour[i+1]] += pheromone_addition

        # Evaluate and store the best found solution
        for tours in all_tours:
            total_cost = sum(calculate_cost(tours[depot]) for depot in tours)
            if total_cost < best_cost:
                best_cost = total_cost
                best_tours = tours

# Printing the solution
def print_tours_and_costs():
    total_cost = 0
    for depot, tour in best_tours.items():
        tour_cost = calculate_cost(tour)
        total_cost += tour_cost
        print(f"Robot {depot} Tour: {tour}")
        print(f"Robot {depot} Total Travel Cost: {tour_cost}")
    print(f"Overall Total Travel Cost: {total_cost}")

find_tours()
print_tours_and_costs()