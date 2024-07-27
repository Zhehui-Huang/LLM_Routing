import numpy as np
import random
from math import sqrt

# Define the city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
depots = [0, 1, 2, 3]  # Indices of the depots

# Define number of robots
num_robots = len(depots)

# Compute Euclidean distance
def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create distance matrix
distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Initialize a random tour for the robots
def initialize_tours():
    cities = list(range(len(coordinates)))
    non_depot_cities = [city for city in cities if city not in depots]
    random.shuffle(non_depot_cities)
    
    # Split cities roughly equally amongst robots
    sizes = np.array_split(non_depot_cities, num_robots)
    tours = {depots[i]: [depots[i]] + list(sizes[i]) + [depots[i]] for i in range(num_robots)}
    return tours

def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def total_travel_cost(tours):
    return sum(calculate_tour_cost(tour) for tour in tours.values())

# Genetic Algorithm to optimize the paths
def genetic_algorithm(tours):
    for generation in range(100):  # Number of generations
        new_tours = {}
        for depot, tour in tours.items():
            if len(tour) > 3:  # Can perform a 2-opt move
                # Get a random segment to potentially reverse
                i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                    new_tours[depot] = new_tour
                else:
                    new_tours[depot] = tour
            else:
                new_tours[depot] = tour
        tours = new_tours
    return tours

# Initialize tours
initial_tours = initialize_tours()
optimized_tours = genetic_algorithm(initial_tours)
costs = {robot: calculate_tour_cost(tour) for robot, tour in optimized_tours.items()}
total_cost = total_travel_cost(optimized_tours)

# Output final tours and costs
for robot, tour in optimized_tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {costs[robot]}")

print(f"Overall Total Travel Cost: {total_cost}")