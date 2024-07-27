import math
from itertools import permutations

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all distances between cities
distance_matrix = {}
for i in range(20):
    for j in range(20):
        distance_matrix[(i, j)] = euclidean_distance(i, j)

def initial_tour():
    # Simple greedy approach as initial tour
    unvisited = set(cities.keys())
    unvisited.remove(0)
    tour = [0]
    current = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[(current, x)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(0) # To complete the tour and return to the depot
    return tour

def total_cost_of_tour(tour):
    total_cost = sum(distance_matrix[(tour[i-1], tour[i])] for i in range(1, len(tour)))
    return total_cost

# Perform initial tour finding
tour = initial_tour()
total_cost = total_cost_of_tour(tour)

# Outputting results
print("Tour:", tour)
print("Total travel cost:", total_cost)