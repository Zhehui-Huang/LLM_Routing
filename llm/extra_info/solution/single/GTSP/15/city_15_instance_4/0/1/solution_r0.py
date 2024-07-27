import math

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Groups of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate all distances between cities
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Generate all possible tours by selecting one city from each group plus the depot
from itertools import product

def generate_tours():
    for pr in product(*groups):
        yield [0] + list(pr) + [0]

# Calculate the cost of each tour
def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Find the shortest tour
shortest_tour = None
shortest_cost = float('inf')
for tour in generate_tours():
    cost = calculate_tour_cost(tour)
    if cost < shortest_cost:
        shortest_tour, shortest_cost = tour, cost

# Print the result
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_cost:.2f}")