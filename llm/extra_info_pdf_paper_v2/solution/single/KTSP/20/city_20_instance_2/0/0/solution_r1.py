import numpy as np
import random
from scipy.spatial import distance

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

def init_tour():
    tour = random.sample(list(cities.keys()), 10)
    if 0 not in tour:
        tour[0] = 0
    tour.append(0)
    return tour

def calculate_tour_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def swap_cities(tour):
    idx1, idx2 = np.random.choice(range(1, len(tour) - 2), 2, replace=False)
    new_tour = tour[:]
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    return new_tour

def local_search(tour):
    min_distance = calculate_tour_distance(tour)
    best_tour = tour[:]
    improving = True
    
    while improving:
        improving = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 0 and j != 0:
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = tour[j], tour[i]
                    new_distance = calculate_tour_distance(new_tour)
                    if new_distance < min_distance:
                        min_distance = new_distance
                        best_tour = new_tour
                        improving = True
    return best_tour, min_distance

best_tour_overall = None
best_distance_overall = float('inf')

# Simple stochastic repeated local search
for _ in range(100):
    initial_tour = init_tour()
    local_tour, local_distance = local_search(initial_tour)
    if local_distance < best_distance_overall:
        best_distance_overall = local_distance
        best_tour_overall = local_tour

print("Tour:", best_tour_overall)
print("Total travel cost:", best_distance_overall)