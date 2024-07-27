import math
import random

# City coordinates
coordinates = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Groups of cities
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def initial_tour(groups, depot=0):
    tour = [depot]
    for group in groups:
        tour.append(random.choice(group))
    tour.append(depot)
    return tour

def compute_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

def local_optimize(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != j:
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tine[i]
                    new_cost = compute_cost(new_tour)
                    if new_cost < compute_cost(tour):
                        tour = new_tour
                        improved = True
    return tour

def glns_algorithm(groups, num_trials=100):
    best_tour = initial_tour(groups)
    best_cost = compute_cost(best_tour)
    
    for _ in range(num_trials):
        current_tour = initial_tour(groups)
        current_tour = local_optimize(current_tour)
        current_cost = compute_cost(current_tour)
        
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost
            
    return best_tour, best_cost

# Run GLNS algorithm
final_tour, final_cost = glns_algorithm(groups)

# Output the final tour and cost
print("Tour:", final_tour)
print("Total travel cost:", final_cost)