import numpy as np
import random
import itertools

# Definitions and constants
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}
num_iter = 1000  # number of iterations for multi-start heuristic

def calculate_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def nearest_neighbor_tour(start_city, available_cities):
    tour = [start_city]
    current_city = start_city
    while available_cities:
        next_city = min(available_cities, key=lambda x: calculate_distance(current_city, x))
        tour.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city
    tour.append(start_city)
    return tour

def two_opt_swap(tour):
    best_tour = tour
    best_cost = total_tour_cost(tour)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True
                    break
            if improved:
                break
    return best_tour

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    for _ in range(num_iter):
        selected_cities = random.sample(list(cities.keys())[1:], 9) + [0, 0]
        initial_tour = nearest_neighbor_tour(0, selected_cities[:-1])
        optimized_tour = two_opt_swap(initial_tour)
        current_cost = total_tour_cost(optimized_tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = optimized_tour
    return best_tour, best_cost

# Perform the search
best_tour, best_cost = find_shortest_tour()
best_cost = round(best_cost, 2)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")