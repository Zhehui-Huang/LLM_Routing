import numpy as as np
from math import sqrt

# Data Setup
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

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate all-pairs distances
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i, j] = euclidean_distance(cities[i], cities[j])

# Ant Colony System Algorithm
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
                    if remaining_cities:
                        current_city = tours[depot][-1]
                        probabilities = []
                        for city in remaining_cities:
                            tau = pheromones[current_city][city] ** alpha
                            eta = (1.0 / distances[current_city][city]) ** beta
                            probabilities.append(tau * eta)
                        
                        if sum(probabilities) == 0:
                            probabilities = [1] * len(probabilities)
                        
                        probabilities = np.array(probabilities) / sum(probabilities)
                        next_city = np.random.choice(list(remaining_cities), p=probabilities)
                        tours[depot].append(next_city)
                        remaining_cities.remove(next_city)
        
            for depot in depots:
                tours[depot].append(depot)  # Complete the loop
                all_tours.append(tours)

        # Update pheromones
        pheromones *= (1 - evaporation_rate)
        for tours in all_tours:
            for tour in tours.values():
                pheromone_deposit = 1 / calculate_cost(tour)
                for i in range(len(tour) - 1):
                    pheromones[tour[i], tour[i+1]] += pheromone_deposit

        # Evaluate solutions
        for tours in all_tours:
            total_cost = sum(calculate_cost(tours[depot]) for depot in tours)
            if total_cost < best_cost:
                best_cost = total_cost
                best_tours = tours

def calculate_cost(route):
    return sum(distances[route[i], route[i+1]] for i in range(len(route) - 1))

def print_tours_and_costs(tours, total_cost):
    for robot_id, tour in tours.items():
        tour_cost = calculate_cost(tour)
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    print(f"Overall Total Travel Cost: {total_cost}")

find_tours()
print_tours_and_costs(best_tours, best_cost)