import random
import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def get_initial_k_cities(k):
    return random.sample(list(cities.keys()), k)

def local_search(tour):
    best_tour = tour[:]
    best_distance = total_distance(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j-i == 1: continue  # no change if they are consecutive
                new_tour = tour[:]
                new_tour[i:j+1] = reversed(tour[i:j+1])
                new_distance = total_distance(new_tour)
                if new_distance < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_distance
                    improved = True
        tour = best_tour[:]
    return best_tour, best_distance

# Variable Neighborhood Search
def variable_neighborhood_search(k):
    best_tour = None
    best_cost = float('inf')
    for _ in range(50):  # Number of iterations
        initial_tour = [0] + get_initial_k_cities(k-1) + [0]
        tour, cost = local_search(initial_tour)
        if cost < best_cost:
            best_tour = tour[:]
            best_cost = cost
    return best_tour, best_cost

# Solve the problem for k=13 including depot city
final_tour, final_cost = variable_neighborhood_search(13)

# Output
print("Tour:", final_tour)
print("Total travel cost:", final_cost)