import math
import random

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def swap_cities(tour, cities, non_tour_cities):
    best_tour = tour[:]
    best_cost = total_tour_cost(best_tour, cities)
    improved = False
    for i in range(1, len(tour) - 2):
        for j in non_tour_cities:
            new_tour = tour[:]
            new_tour[i] = j
            new_cost = total_tour_cost(new_tour, cities)
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost
                improved = True
    return best_tour, best_cost, improved

def local_optimization(tour, cities):
    best_tour = tour[:]
    best_cost = total_tour_cost(best_tour, cities)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_cost(new_tour, cities)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    improved = True
    return best_tour, best_cost

# City coordinates (index 0 is the depot city)
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
    (64, 72), (14, 89)
]

# Initial k-TSP tour selection
selected_cities = random.sample(range(1, len(cities)), 15)
selected_cities = [0] + selected_cities + [0] # Start and end at the depot

# Run local optimization
best_tour, best_cost = local_optimization(selected_cities, cities)
non_tour_cities = list(set(range(len(cities))) - set(best_tour))

# Swap cities not in tour and rerun local optimization
best_tour, best_cost, improved = swap_cities(best_tour, cities, non_tour_cities)
if improved:
    best_tour, best_cost = local_optimization(best_tour, cities)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)