import math
from itertools import combinations

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Define cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculating all pairwise distances
distance_matrix = [[0 if i == j else euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Function to find a tour using a greedy algorithm constrained by max_edge
def find_tour(max_edge):
    n = len(cities)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    
    for _ in range(1, n):
        last = tour[-1]
        next_city = None
        for j in range(n):
            if not visited[j] and distance_matrix[last][j] <= max_edge:
                if next_city is None or distance_matrix[last][j] < distance city_matrix[last][next_city]:
                    next_city = j
        if next_city is None:
            return None
        visited[next_city] = True
        tour.append(next_city)
        
    if distance_matrix[tour[-1]][0] > max_edge:  # Must be able to return to start
        return None
    tour.append(0)  # return to starting city
    return tour

# Binary search to find the minimum maximum edge length that allows a tour
lo, hi = 0, max(max(row) for row in distance_matrix)
best_tour = None

while hi - lo > 1e-5:
    mid = (lo + hi) / 2
    tour = find_tour(mid)
    if tour:
        best_tour = tour
        hi = mid
    else:
        lo = mid

# Calculating metrics
if best_tour:
    total_cost = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
    max_distance = max(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
    
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No valid tour found.")