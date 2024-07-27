import math
import numpy as np
from scipy.spatial.distance import pdist, squareform
from collections import defaultdict

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distances):
    total = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    return total

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Number of robots and their starting depots
num_robots = 2
depots = {0: 0, 1: 1}

# Calculate distances
all_cities = list(cities.keys())
distances = squareform(pdist([cities[i] for i in all_cities]))

# Approximate solution by clustering based on nearest to each depot
clusters = {0: [0], 1: [1]}
for city in cities:
    if city not in depots.values():
        closest_depot = min(depots, key=lambda x: distances[city, x])
        clusters[closest_depot].append(city)

# Greedy TSP solution for each cluster starting at the respective depot
tours = {}
total_cost = 0

for robot in clusters:
    unvisited = set(clusters[robot])
    current_city = depots[robot]
    tour = [current_city]
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current_city, x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tours[robot] = tour
    tour_cost = calculate_total_distance(tour, distances)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")
    total_cost += tour150

print(f"Overall Total Travel Cost: {total_cost}")