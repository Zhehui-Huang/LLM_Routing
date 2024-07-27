import numpy as np
from scipy.spatial import distance_matrix
import random

# Define cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242), 
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Depots
depots = [0, 1, 2, 3]

# Generate the distance matrix
coordinates = np.array(list(cities.values()))
dist_matrix = distance_matrix(coordinates, coordinates)

# Function to calculate total travel cost of a tour
def calculate_total_cost(tour):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Simple greedy algorithm to create initial tour for each robot from its depot
def create_tour(depot, cities):
    remaining_cities = set(cities) - set(depots)
    tour = [depot]
    current_city = depot
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: dist_matrix[current_city, x])
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    tour.append(depot)  # return to the depot
    return tour

# Function to split cities approximately equally and create tours for each robot
def create_initial_tours():
    # Assign equitably non-depot cities to each depot
    non_depot_cities = [c for c in cities.keys() if c not in depots]
    random.shuffle(non_depot_cities)
    split = np.array_split(non_depot_cities, len(depots))
    tours = {}
    costs = {}
    for i, depot in enumerate(depots):
        tour = create_tour(depot, list(split[i]) + [depot])
        tours[depot] = tour
        costs[depot] = calculate_total_cost(tour)
    return tours, costs

# Create tours
tours, costs = create_initial_tours()

# Output information
total_cost = sum(costs.values())

for depot, tour in tours.items():
    print(f"Robot from Depot {depot} Tour: {tour}")
    print(f"Robot from Depot {depot} Total Travel Cost: {costs[depot]}")

print(f"Overall Total Travel Cost: {total_cost}")