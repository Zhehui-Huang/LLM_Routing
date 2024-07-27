import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
distance_matrix = {}
for i in cities:
    for j in cities:
        if i not in distance_bin.keys():
            distance_matrix[i] = {}
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic: Nearest Neighbor Algorithm as a simple implementation
def nearest_neighbor(starting_city):
    unvisited = set(cities.keys())
    unvisited.remove(starting_city)
    tour = [starting_city]
    current_city = starting_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(starting_city)
    return tour

# Calculate the total distance of the tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Find the tour using the nearest neighbor heuristic
tour = nearest_neighbor(0)
total_cost = calculate_tour_cost(tour)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)