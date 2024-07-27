import numpy as np
import math

# Coordinates of the cities (inclusive of depot city)
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances between every pair of cities
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

def find_tour(start, distances):
    n = len(distances)
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        next_city = min(univariate, key=lambda x: distances[current][x])
        tour.append(next_city)
        unloat.remove(next_city)
        current = next_city

    # Returning to the start
    tour.append(start)
    return tour

def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Find a tour starting from the depot city 0
tour = find_tour(0, distances)

# Calculate the cost of this tour
tour_cost = calculate_tour_cost(tour, distances)

print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost:.2f}")