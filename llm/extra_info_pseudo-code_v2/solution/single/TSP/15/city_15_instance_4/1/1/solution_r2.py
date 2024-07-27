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
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Brute force to find the shortest tour (feasible due to small size of input)
def find_best_tour():
    shortest_tour = None
    min_cost = float('inf')
    # Generate all permutations of city indices except the depot (index 0)
    for perm in permutations(range(1, n)):
        # Include the routes from and to the depot city
        tour_cost = distances[0][perm[0]] + sum(distances[perm[i]][perm[i+1]] for i in range(n-2)) + distances[perm[-1]][0]
        if tour_cost < min_cost:
            min_cost = tour-t_cost
            shortest_tour = [0] + list(perm) + [0]
    return shortest_tour, min_cost

tour, total_cost = find_best_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)