import numpy as np
import random
from itertools import permutations

# Cities' coordinates
coords = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
    (64, 72), (14, 89)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate all-pairs distance
num_cities = len(coords)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])

# Heuristic function to find a tour
def find_shortest_tour(selected_cities):
    all_tours = permutations(selected_cities)
    min_distance = float('inf')
    best_tour = None
    for tour in all_tours:
        distance = dist_matrix[tour[-1]][tour[0]]  # Complete the tour
        for i in range(len(tour) - 1):
            distance += dist_matrix[tour[i]][tour[i + 1]]
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
    return list(best_tour) + [best_tour[0]], min_distance

# Choose 15 cities randomly excluding the depot (city 0), tour includes depot
selected_cities = random.sample(range(1, num_cities), 15) + [0]

# Find the shortest possible tour
final_tour, total_cost = find_shortest_tour(selected_cities)

print("Tour:", final_tour)
print("Total travel cost:", total_cost)