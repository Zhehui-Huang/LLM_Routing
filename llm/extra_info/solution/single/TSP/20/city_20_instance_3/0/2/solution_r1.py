import itertools
import math

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Precompute distances between all pairs of cities
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Generate all possible tours from city 0 and back to city 0, visiting other cities exactly once
all_tours = itertools.permutations(range(1, n))
min_distance = float('inf')
best_tour = None

for tour in all_tours:
    # Calculate the tour cost, starting and ending at the depot (city 0)
    cost = distances[0][tour[0]] + distances[tour[-1]][0]
    for i in range(1, len(tour)):
        cost += distances[tour[i-1]][tour[i]]
    
    # Update minimum cost and best tour found
    if cost < min_distance:
        min_distance = cost
        best_tour = tour

# Format the best tour to start and end with depot city 0
final_tour = [0] + list(best_tour) + [0]

# Output the results
print("Tour:", final_tour)
print("Total travel cost:", min_distance)