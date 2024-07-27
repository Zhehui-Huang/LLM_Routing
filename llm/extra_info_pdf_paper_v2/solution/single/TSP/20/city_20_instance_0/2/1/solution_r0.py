import math
import random

# Given city coordinates
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]

def euclidean_distance(from_idx, to_idx):
    x1, y1 = city_coords[from_idx]
    x2, y2 = city_coords[to_idx]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initial random tour starting from the depot city 0
def initial_tour():
    cities = list(range(1, len(city_coords)))  # Cities without the depot
    random.shuffle(cities)
    return [0] + cities + [0]

def calculate_total_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# 2-opt swap heuristic for improving tours
def two_opt_swap(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j-i == 1: continue  # Skip consecutive 'i' and 'j'
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_cost(new_tour) < calculate_total_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

def find_shortest_tour():
    best_tour = initial_tour()
    best_cost = calculate_total_cost(best_tour)
    for _ in range(1000):  # Number of iterations for better optimal solution
        tour = initial_tour()
        improved_tour = two_opt_swap(tour)
        cost = calculate_total_cost(improved_tour)
        if cost < best_cost:
            best_tour, best_cost = improved_tour, cost
    return best_tour, best_cost

# Solve the TSP problem
tour, total_travel_cost = find_shortest_tour()

# Output result
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)