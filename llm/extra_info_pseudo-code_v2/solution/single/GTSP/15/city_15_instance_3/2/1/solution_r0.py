import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities' coordinates
cities = [
    (16, 90), # Depot city 0
    (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), 
    (64, 30), (70, 95), (29, 64), (32, 79)
]

# Groups of cities
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Pre-calculate distances
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def initial_tour():
    # Start with depot, visit one random city from each group, return to depot
    tour = [0]
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)
    return tour

def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distances[tour[i]][tour[i+1]]
    return cost

def local_optimization(tour):
    # Attempt simple 2-opt swaps to reduce tour cost
    improved = True
    while improved:
        improved = False
        best_cost = tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 1 or j != len(tour) - 2:  # Do not break the depot constraint
                    new_tour = tour[:]
                    new_tour[i:j+1] = reversed(tour[i:j+1])
                    new_cost = tour_cost(new_tour)
                    if new_cost < best_cost:
                        tour = new_tour
                        best_cost = new_cost
                        improved = True
        return tour

def simulated_annealing(tour):
    temp = 100
    alpha = 0.99
    max_iterations = 1000
    current_tour = tour
    current_cost = tour_cost(current_tour)
    
    for _ in range(max_iterations):
        i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
        new_tour = current_tour[:]
        new_tour[i:j+1] = reversed(current_tour[i:j+1])
        new_cost = tour_cost(new_tour)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_tour, current_cost = new_tour, new_cost
        
        temp *= alpha
    
    return current_tour

# Run optimization
best_tour = initial_tour()
best_tour = simulated_annealing(best_tour)
best_tour = local_optimization(best_tour)
best_cost = tour_cost(best_tour)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)