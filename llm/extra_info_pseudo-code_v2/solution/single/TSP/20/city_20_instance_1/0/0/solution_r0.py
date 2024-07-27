import math
import random
from itertools import permutations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Coordinates of the cities
cities = [
    (14, 77), # Depot city 0
    (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), 
    (27, 45), (90, 85), (98, 76), (6, 19), 
    (26, 29), (21, 79), (49, 23), (78, 76), 
    (68, 45), (50, 28), (69, 9)
]

# Precomputing distances between all pairs of cities
N = len(cities)
distances = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])

def total_distance(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Find a solution using Random permutations
best_tour = list(range(N)) + [0]
best_cost = total_distance(best_tour)
failed_attempts = 0

while failed_attempts < 100:
    # Generate a new tour randomly
    current_tour = [0] + random.sample(range(1, N), N - 1) + [0]
    current_cost = total_distance(current_tour)
    
    if current_cost < best_cost:
        best_tour = current_tour
        best_cost = current_cost
        failed_attempts = 0
    else:
        failed_attempts += 1

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")