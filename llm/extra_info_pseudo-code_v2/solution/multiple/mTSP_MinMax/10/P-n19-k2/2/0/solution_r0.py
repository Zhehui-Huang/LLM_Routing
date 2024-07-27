import numpy as np
from itertools import permutations
import random
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two coordinates
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Initialize the distances matrix
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialization procedure
def initialization():
    tours = [[] for _ in range(2)]  # Assuming 2 robots
    city_index = list(range(1, n))  # City indices excluding the depot
    random.shuffle(city_index)
    for i, city in enumerate(cityindex):
        tours[i % 2].append(city)
    return tours

# Compute cost of a tour
def compute_tour_cost(tour):
    tour_cost = 0
    current_city = 0  # start at the depot
    for city in tour:
        tour_cost += distances[current_city][city]
        current_city = city
    tour_cost += distances[current_city][0]  # return to depot
    return tour_cost

# GVNS procedures
def shake(tours, k):
    for _ in range(k):
        v = random.randint(0, 1)
        if tours[v]:
            i = random.randint(0, len(tours[v]) - 1)
            t = 1 - v
            tours[t].append(tours[v].pop(i))
    return tours

def local_optimization(tours):
    return tours  # In a full implementation, we should optimize each tour using 2-opt or 3-opt methods

def gvns():
    tours = initialization()
    best_tours = tours
    best_costs = [compute_tour_cost(tour) for tour in tours]
    max_cost = max(best_costs)
    
    max_iter = 100
    for _ in range(max_iter):
        for k in range(1, 6):  # Increase the shaking intensity
            new_tours = shake([list(tour) for tour in tours], k)
            new_tours = local_optimization(new_tours)
            new_costs = [compute_tour_cost(tour) for tour in new_tours]
            new_max_cost = max(new_costs)
            
            if new_max_cost < max_cost:
                best_tours, best_costs, max_cost = new_tours, new_costs, new_max_cost
                break
    
    return best_tours, best_costs, max_cost

# Run the GVNS
best_tours, best_costs, max_cost = gvns()

# Print results
for i, (tour, cost) in enumerate(zip(best_tours, best_costs)):
    print(f"Robot {i} Tour: {[0] + tour + [0]}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")