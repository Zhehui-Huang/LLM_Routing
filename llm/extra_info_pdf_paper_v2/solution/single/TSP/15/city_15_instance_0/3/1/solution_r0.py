import math
import itertools
import random

# Coordinates of the cities (indexed by city number)
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50),
    (21, 23), (88, 59), (79, 77), (63, 23), 
    (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_cost(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total

def generate_initial_tour():
    tour = list(range(1, len(coordinates))) # excluding the depot city at first
    random.shuffle(tour)
    tour = [0] + tour + [0] # Adding depot city to start and end
    return tour

def two_opt_swap(tour):
    best_tour = tour
    best_cost = total_cost(tour)
    made_improvement = True
    
    while made_improvement:
        made_improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = total_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    made_improvement = True
        tour = best_tour
    
    return tour, best_cost

# Initial tour generation and 2-opt based improvement
initial_tour = generate_initial_tour()
optimized_tour, optimized_cost = two_opt_swap(initial_tour)

# Output the result
print("Tour:", optimized_tour)
print("Total travel cost:", optimized_cost)