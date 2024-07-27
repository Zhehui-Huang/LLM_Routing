import numpy as np
import random
from itertools import permutations

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_distance(tour, coords):
    return sum(euclidean_distance(coords[tour[i]], coords[tour[i + 1]]) for i in range(len(tour) - 1))

def initial_tour(depot, cities, k):
    selected_cities = random.sample(cities, k - 1)
    selected_cities.append(depot)
    selected_cities.insert(0, depot)
    return selected_cities

def local_search(tour, coords):
    best_tour = tour
    best_distance = total_distance(tour, coords)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_distance = total_distance(new_tour, coords)
                if new_distance < best_distance:
                    best_tour, best_distance = new_tour, new_distance
                    improved = True
    return best_tour, best_distance

# Coordinates of cities [city_index: (x, y)]
coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

depot = 0
cities = list(coordinates.keys())
k = 16

# GNVS approach:
# Initialize a tour
tour = initial_tour(depot, [city for city in cities if city != depot], k)
current_tour, current_distance = local_search(tour, coordinates)

print("Tour:", current_tour)
print("Total travel cost:", current_distance)