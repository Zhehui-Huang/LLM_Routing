import itertools
import math

# Define the cities and their coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to compute the Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Precompute distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = distance(cities[i], cities[j])

# Generate all combinations of 8 cities including the depot city 0
city_indices = list(cities.keys())
combinations = [comb for comb in itertools.combinations(city_indices, 8) if 0 in comb]

# Function to find a tour using a nearest neighbor approach starting from the depot
def nearest_neighbor_tour(cities):
    start_city = 0
    unvisited = set(cities)
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[(current_city, city)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # Close the tour
    return tour

# Function to calculate the total cost of the tour
def tour_cost(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Function to perform the 2-opt swap
def two_opt(tour):
    n = len(tour)
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                if distances[(tour[i], tour[i-1])] + distances[(tour[j], tour[j+1])] > distances[(tour[i], tour[j])] + distances[(tour[i-1], tour[j+1])]:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improvement = True
    return tour

# Finding the optimal tour among all combinations
best_tour = None
best_cost = float('inf')

for cities_comb in combinations:
    tour = nearest_neighbor_tour(cities_comb)
    tour = two_opt(tour)
    cost = tour_cost(tour)
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost))