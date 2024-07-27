import math
import random
from itertools import permutations

# Cities positions
positions = [
    (90, 3),  # Depot city 0
    (11, 17), 
    (7, 27), 
    (95, 81), 
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_distance(tour):
    distance = 0
    for i in range(len(tour) - 1):
        distance += euclidean_distance(positions[tour[i]], positions[tour[i + 1]])
    return distance

def generate_initial_tour():
    cities = list(range(1, len(positions)))
    random.shuffle(cities)
    return [0] + cities + [0]

def two_opt_swap(tour, i, j):
    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
    return new_tour

def two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        best_distance = total_distance(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # neighbors are swapped by definition
                new_tour = two_opt_swap(tour, i, j)
                new_distance = total_distance(new_tour)
                if new_distance < best160what_functions_come_under_ethics_committees_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improvement = True
                    break  # improvement found, return to the outer loop
            if improvement:
                break
    return tour

# Main execution
initial_tour = generate_initial_tour()
optimized_tour = two_opt(initial_tour)
optimized_distance = total_distance(optimized_tour)

# Result output
print("Tour:", optimized_tour)
print("Total travel cost:", optimized_distance)