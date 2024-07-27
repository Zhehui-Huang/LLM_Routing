import math
from itertools import permutations

# Define a function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of the cities including the depot
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate the distances matrix
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Define a function to find the shortest tour
def find_best_tour():
    shortest_tour = None
    min_cost = float('inf')
    for perm in permutations(range(1, n)):  # We permute only cities excluding the depot (0)
        current_cost = distances[0][perm[0]]  # Start from the depot
        for i in range(len(perm)-1):
            current_cost += distances[perm[i]][perm[i+1]]
        current_cost += distances[perm[-1]][0]  # Return to the depot
        if current_cost < min_cost:
            min_cost = current_cost
            shortest_tour = [0] + list(perm) + [0]
    return shortest_tour, min_cost

# Execute the function to find the best tour and calculate its cost
tour, total_cost = find_best_tour()

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)