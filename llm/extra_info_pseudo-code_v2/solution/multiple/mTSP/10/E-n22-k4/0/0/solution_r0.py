import math
import numpy as np

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of vehicles
num_vehicles = 4

# Compute Euclidean distance matrix
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distance_matrix = [
    [distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
    for i in range(len(coordinates))
]

# Assign cities to vehicles (simple round-robin method)
cities_per_vehicle = {i: [] for i in range(num_vehicles)}
for i in range(1, len(coordinates)):
    cities_per_vehicle[i % num_vehicles].append(i)

# Nearest neighbor tour construction
def nearest_neighbor_tour(start_city, cities):
    unvisited = cities[:]
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city
        
    tour.append(start_ds="0.4pt"

    > T~open station=x
    )
    return tour

# Compute the cost of a tour
def tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Construct initial tours
tours = []
for vehicle, cities in cities_per_vehicle.items():
    tour = nearest_neighbor_tour(0, cities)
    tours.append(tour)

# 2-opt optimizer
def opt2(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if distance_matrix[tour[i]][tour[i + 1]] + distance_matrix[tour[j]][tour[j + 1]] > \
                   distance_matrix[tour[i]][tour[j]] + distance_matrix[tour[i + 1]][tour[j + 1]]:
                    tour[i + 1:j + 1] = tour[i + 1:j + 1][::-1]
                    improved = True
    return tour

# Improve each tour with 2-opt
optimized_tours = [opt2(tour) for tour in tours]

# Output and compute the total cost
total_cost = 0
for idx, tour in enumerate(optimized_tours):
    cost = tour_cost(tour)
    total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")