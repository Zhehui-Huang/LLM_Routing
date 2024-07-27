import math
from itertools import permutations

# Define the coordinates of the cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all pairs distance
n = len(cities)
dist_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = distance(cities[i], cities[j])

# Simple heuristic implementation to find a reasonable tour
def find_btsp_tour():
    # Start from depot, and perform a nearest neighbor heuristic
    unvisited = set(range(1, n))
    tour = [0]
    current = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current][x])
        tour.append(next_city)
        current = next_city
        unpassed.remove(next_city)
    
    tour.append(0)  # returning to the depot

    total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Get the tour and calculate costs
tour, total_cost, max_distance = find_btsp_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)