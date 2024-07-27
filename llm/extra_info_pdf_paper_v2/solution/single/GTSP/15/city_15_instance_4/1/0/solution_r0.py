import math
from itertools import product
import random

# City coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Groups of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_path_distance(path):
    total_distance = 0
    for i in range(1, len(path)):
        total_distance += calculate_distance(path[i-1], path[i])
    total_distance += calculate_distance(path[-1], path[0])
    return total_distance

def find_best_tour(groups):
    min_distance = float('inf')
    best_tour = None
    
    for selected in product(*groups):
        full_tour = [0] + list(selected) + [0]
        distance = total_path_distance(full_tour)
        if distance < min_distance:
            min_distance = distance
            best_tour = full_tour
            
    return best_tour, min_distance

best_tour, min_distance = find_best_tour(groups)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")