import math
import random
from itertools import combinations

def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def total_tour_cost(tour, coords):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coords[tour[i]], coords[tour[i+1]])
    return total_cost

def create_initial_tour(depot, cities, k):
    selected_cities = [depot] + random.sample(cities, k-1)
    selected_cities.append(depot)
    return selected_cities

def two_opt_swap(tour):
    best = tour
    best_cost = total_tour_cost(tour, coordinates)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            if j - i == 1: continue
            new_tour = tour[:]
            new_tour[i:j] = tour[j-1:i-1:-1]
            new_cost = total_tour_cost(new_tour, coordinates)
            if new_cost < best_cost:
                best = new_tour
                best_cost = new_cost
    return best

def gvns(tour, coordinates, max_iter=100):
    best_tour = tour
    best_cost = total_tour_cost(tour, coordinates)
    for _ in range(max_iter):
        new_tour = two_opt_swap(best_tour)
        new_cost = total_tour_cost(new_tour, coordinates)
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
    return best_tour

# Coordinates (city index: (x, y))
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92),
    4: (54, 93), 5: (34, 73), 6: (6, 61), 7: (86, 69),
    8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30), 
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

selected_tour = create_initial_tour(0, list(range(1, 15)), 10)
best_tour = gvns(selected_tour, coordinates)
best_tour_cost = total_tour_cost(best_tour, coordinates)

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)